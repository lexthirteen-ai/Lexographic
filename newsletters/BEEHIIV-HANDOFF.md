# Handoff: put issue 17 into Beehiiv

Paste this whole file as the first message to a session running on the MacBook
(one started with `claude remote-control`, so it has browser control).

---

## The task

Put Artificially Designed issue 17 into Beehiiv as a **draft**. Do not send it,
do not schedule it. Lex finalizes and sends it herself.

## Get the files

```
git fetch origin claude/fervent-ptolemy-4d9iz3
git checkout claude/fervent-ptolemy-4d9iz3
cd newsletters
```

| File | What it is |
|---|---|
| `2026-10-05-issue-17-beehiiv-ready.md` | **The source of truth.** Beehiiv field values above the first rule, body below it. |
| `2026-10-05-issue-17-beehiiv-body.html` | Same body as inline-styled HTML, if pasting rich text misbehaves. |
| `2026-10-05-issue-17.md` | The working draft, with a notes block at the bottom. Reference only, do not paste. |
| `2026-10-05-issue-17-diagrams.html` | The three diagrams to export. |

## Steps

1. Open `https://app.beehiiv.com/` in Lex's browser. **Hand the login to her**, then take
   it back once she is in.
2. Find the most recent published issue, **Issue 16: The Fence**, and **duplicate it**.
   Duplicating is what preserves her template, which is the whole reason to do this in the
   browser rather than through the API.
3. Clear the duplicated body and fill it from `2026-10-05-issue-17-beehiiv-ready.md`:
   - Post title, subject line, preview text and header image spec are the labelled field
     values above the first rule. They go in Beehiiv's own fields, not in the body.
   - Everything below the first rule is the body. Eight sections, each heading starting
     with an emoji. Keep the emoji, they are the house format.
   - Keep the horizontal rules between sections.
   - The Prompt for Productivity block is a code block. Keep it as one.
4. Export the three diagrams from the artifact at
   https://claude.ai/artifact/JSxQTiB3xcDPydb7sz5jcK (each has its own download button),
   upload them, and place each one **after the sentence named below**, displayed at 600 wide.

   | File | Goes after |
   |---|---|
   | `charmthirteen-issue17-03-watch-versus-know.jpg` | "I went looking for **why** and could not find it." |
   | `charmthirteen-issue17-01-inhaler-contradiction.jpg` | "A reviewer scanning for invention finds nothing wrong." |
   | `charmthirteen-issue17-02-three-test-questions.jpg` | "Does it catch a hidden contradiction?" |

5. Save as a draft. Send Lex the Beehiiv draft URL.

## Do not edit her copy

The body is final and has been checked against her voice rules. Do not rewrite, tighten,
or "improve" any sentence. In particular:

- **No em dashes anywhere.** If you introduce one, that is a defect.
- Never the construction "it's not X, it's Y", including split across two sentences.
- Do not touch the line "**The scored exam has not been taken yet, so there is no
  independent grade to report.**" It is a deliberate integrity statement.
- Do not add a CHARM explanation. CHARM is named and not explained on purpose.
- Paimon is Lex's own agent and must not appear anywhere in the post.

If something looks like an error, leave it and tell her rather than fixing it silently.

## Two open items to mention, not solve

- The Kansas City dates came from aggregators and are unconfirmed against each organiser.
- Cosmo Hacks is ages 13 to 18, which does not cover all of "middle and high schoolers".
  The copy currently states the range rather than promising the hackathon to everyone.
