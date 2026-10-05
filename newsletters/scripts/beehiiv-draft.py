#!/usr/bin/env python3
"""Create an Artificially Designed issue as a Beehiiv DRAFT.

Reads the API key from BEEHIIV_API_KEY. Nothing is published: status is
always "draft", so the post lands in Beehiiv for Lex to finalize and send.

    BEEHIIV_API_KEY=... python3 scripts/beehiiv-draft.py \
        --body 2026-10-05-issue-17-beehiiv-body.html \
        --title "Artificially Designed Issue 17: The Record" \
        --subtitle "Last week was about fences. This week is about whether you can say why an agent went where it went."

Add --publication pub_xxx to skip publication lookup.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = "https://api.beehiiv.com/v2"


def call(method, path, token, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(API + path, data=data, method=method)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        try:
            body = json.loads(body)
        except ValueError:
            pass
        return e.code, body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--body", required=True, help="inline-styled HTML file")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default=None)
    ap.add_argument("--publication", default=os.environ.get("BEEHIIV_PUBLICATION_ID"))
    args = ap.parse_args()

    token = os.environ.get("BEEHIIV_API_KEY")
    if not token:
        sys.exit("BEEHIIV_API_KEY is not set. Add it to the environment's API credentials.")

    pub = args.publication
    if not pub:
        status, body = call("GET", "/publications", token)
        if status != 200:
            sys.exit("Could not list publications (HTTP %s): %s" % (status, body))
        pubs = body.get("data", [])
        if len(pubs) != 1:
            for p in pubs:
                print(p.get("id"), p.get("name"))
            sys.exit("Pass --publication with one of the ids above.")
        pub = pubs[0]["id"]
        print("publication:", pub, pubs[0].get("name"))

    payload = {
        "title": args.title,
        "body_content": open(args.body).read(),
        "status": "draft",
    }
    if args.subtitle:
        payload["subtitle"] = args.subtitle

    status, body = call("POST", "/publications/%s/posts" % pub, token, payload)
    if status != 201:
        sys.exit("Create failed (HTTP %s): %s" % (status, body))

    post_id = body.get("data", {}).get("id")
    print("draft created:", post_id)

    # Creation is asynchronous, so confirm it finished building.
    for attempt in range(10):
        time.sleep(3)
        st, b = call("GET", "/publications/%s/posts/%s" % (pub, post_id), token)
        if st == 200:
            print("confirmed in Beehiiv as:", b.get("data", {}).get("status", "draft"))
            return
        if st == 404:
            sys.exit("Background creation failed: %s" % b)
        print("still building (HTTP %s), retrying" % st)
    print("created, but still building. Check Beehiiv in a minute.")


if __name__ == "__main__":
    main()
