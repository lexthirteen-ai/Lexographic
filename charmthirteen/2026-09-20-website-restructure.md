# charmthirteen.com restructure, Sept 20 2026 spec

Build record for the restructure Lex specified on 2026-09-20 and the follow-ups from
2026-09-21. The site lives in the Lovable project "Charmthirteen Build Studio"
(8b8eddc5-1231-47f2-a57f-83e90b40417b), not in this repository. Nothing below is live
on charmthirteen.com until Lex presses Publish in Lovable.

## Spec as executed

- Two entryways: Build (/build) and Training (/workshops, label only, URL kept for indexing).
- /services, /systems, /advisory are permanent server 301s to /build. The pages are deleted.
- Cut from the site: coaching packages ($399 / $999 / $1,799) and Prompt & Agent Systems
  Coaching, "running it as your PM", "pricing research", the Founder Advisory teaser and the
  /advisory page, the outcome cards 01/02/03, the AI Readiness & Workflow Assessment CTA,
  The Lean Clinic, Practice & Protocol. No certification language anywhere.
- Build ladder in two lanes with published prices, typed only in src/data/build.ts.
- Positioning line shipped without the em dash the spec carried: "They rent you a digital
  employee forever. We build one you own, plus training to run it, and we're a phone call
  away if you need help." Outcome line: "Safe, efficient, and usable. In that order."
- Products: Orinyx (reframed as "We build AI products too. Orinyx is one of ours.") and
  Stellar Agents Ascension ($129) with a /stellar sales page and a /stellar/access page
  (noindex) on top of the purchase backend committed 2026-09-20.
- Consulting pages (/healthcare-ai-consulting, /ai-governance-consulting) kept as the SEO
  authority pages, engagements and price lines aligned to the Build ladder.
- Blog: the September draft published, a One Slot Rule post added, five-per-page
  pagination at /blog and /blog/page/N.

## Lovable commits, in order

| Pass | Commit | Scope |
|---|---|---|
| 1 | 44caa614 | src/data/build.ts, /build page and route, 301 routes, old pages deleted, FAQ data |
| 2 | d2050173 | Home, Nav, Footer, About, both consulting pages, Solutions, SolutionDetail, FAQ page |
| 3 | b4ac92cb | Training relabel, Lean Clinic removed, Products, src/data/stellar.ts, /stellar, /stellar/access |
| 4 | d81413af | sitemap, llms.txt rewrite, metadata sweep, FAQ prices from data, Footer Stellar link |
| 5 | 82b80b59 | draft post published, One Slot Rule post, pagination, stale Claude Loves Lovable line |

Lovable project knowledge was rewritten to carry the two-entryway rules (permanent 301s,
prices only in src/data, the removed offers that must not come back, no certification
language, blog publish rules).

## Verification (in the Lovable sandbox, reported by the agent and spot-checked by file reads)

- /services, /systems, /advisory answer HTTP 301 with location /build.
- Every route title is 60 characters or fewer, every description 155 or fewer.
- JSON-LD parses on /build (Service, FAQPage), /stellar (Product), /products (ItemList),
  /faq (FAQPage), /workshops (seven Course nodes), /healthcare-ai-consulting (Service).
- Sitemap lists /build and /stellar, not the three legacy routes or /stellar/access.
- llms.txt starts with "# charmthirteen", lists /build and /stellar, and carries no
  mention of The Lean Clinic or Practice & Protocol.
- Every changed page: one h1, no console errors, 320px reflow with no page scroll.
- The Lovable preview is auth-gated (HTTP 401 from outside), so live-URL checks on
  charmthirteen.com happen after Publish.

## Why the blog posts were missing

- "How to design an AI agent workflow that holds" (2026-09-14) was staged on 2026-09-13
  with status "draft", which hides it from the index, sitemap, RSS and Blog JSON-LD. Fixed
  in pass 5 by publishing it.
- The One Slot Rule was published as Artificially Designed Issue 11, "The Slot" (Aug 24,
  beehiiv) and never as a blog post. Pass 5 adds /blog/one-slot-rule dated 2026-08-24,
  attributed to the issue.
- The "vault governance piece" (2026-09-14 batch) exists only on Lex's Mac in
  content-engine/batches/2026-09-14-vault-governance-piece/ and was never sent to Lovable.
  It needs Lex to send its lovable-message.txt.

## Sunday SEO routine

- Routine id: trig_01YUhpzCC5k5GwgRd8CfgvFk, name "Sunday SEO/GEO/AEO audit (asael)".
- Schedule: CRON_TZ=America/Chicago 0 7 * * 0. Next run 2026-09-27 07:06 CT.
- Fresh session per fire, push notification on.
- Writes Outputs/charmthirteen/<date>-seo-geo-aeo-audit.md to agents-vault and pushes,
  posts the Sunday implementation list in chat, appends the OpenSEO research log.
- Gap: this org's API cannot attach connectors to a Routine, so its sessions have no
  OpenSEO tools until Lex attaches OpenSEO and Claude Code Remote in the claude.ai
  Routines UI. The prompt degrades honestly (crawl and vault steps still run).
- paimon governance/registry.json still marks sunday-seo-audit PROPOSED-NOT-ARMED. The
  registrar's SCHEDULE audit-log line is owed before that flips.

## OpenSEO

- Project context updated 2026-09-21: business overview, current goal, key pages
  (/build, /stellar, /products added; /services removed), research log entry (0 credits).
- Search Console 2026-08-21 to 09-18: 9 clicks, about 480 impressions, home at position
  3.2 on brand terms, /healthcare-ai-consulting at 58, four non-brand queries.
- Post-publish: run_site_audit, inspect_urls on the new and redirected URLs, and price the
  Build-lane keyword seeds listed in the project goal (under the 500-credit ceiling).

## Hand-off to Lex

1. Press Publish in Lovable, then review /build, /stellar, /blog and /blog/one-slot-rule live.
2. Lovable Project Settings, Secrets: STRIPE_PRICE_STELLAR_ASCENSION, GITHUB_RELEASE_TOKEN,
   STELLAR_DOWNLOAD_SECRET. The buy button, download and GitHub invite fail until set. The
   private repo needs a release with a stellar-agents-ascension-*.zip asset.
3. claude.ai Routines: open "Sunday SEO/GEO/AEO audit (asael)", attach OpenSEO and Claude
   Code Remote, then Run now to cover the missed 2026-09-20 audit.
4. Search Console and Bing: request indexing for /build, /stellar, /blog/one-slot-rule,
   /blog/ai-agent-workflow-design, /workshops/claude-loves-lovable, /solutions, /philosophy.
5. Send the vault governance piece's lovable-message.txt if it belongs on the blog.
6. Decide the Chart Smarter "CE-Eligible* pending accreditation partnership" line.
7. Owned backlinks from the 09-13 audit are still open (GitHub READMEs, beehiiv footer,
   Luma, LinkedIn company page, orinyx.io footer).
