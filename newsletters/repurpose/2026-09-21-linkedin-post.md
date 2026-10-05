# LinkedIn: 5 questions to ask before your next AI-built feature ships

Source: Artificially Designed, September 21, 2026. Format: long-form post.

---

Last week researchers published a flaw that hit all four major AI coding agents at once. The vulnerability is worth an afternoon of your attention, and what it reveals about how we are all working now is worth rather more than that.

Here is the mechanism, in plain terms. These tools pin plugins to a commit hash, so the code you reviewed stays the code that runs. An attacker creates a branch named identically to that forty character hash and makes it the default branch. Git resolves the branch instead of the commit. Your pinned plugin was never pinned, and because plugins auto-update, the swap arrives with no action from you.

Claude Code patched it in 2.1.179 and Codex in 0.146.0. Copilot has no vendor fix. Google deprecated Gemini CLI rather than patching it.

But go update your tools and the underlying thing is still true. In the last six months we moved from reading every suggestion before accepting it to reading a summary of work done by agents that fetch their own tools. Cursor and Claude Code both shipped coordinator-plus-subagent project features within a week of each other. The unit of work stopped being a prompt and became an assignment.

Most founders I work with made that shift without noticing, which means they never decided what their review step should be.

So before your next AI-built feature ships, five questions:

1. What did it install or fetch to build this? Not what you installed. What it decided it needed.

2. Where did those come from? A package you named is a different risk from one it chose.

3. Is auto-update on for any of it? That is the difference between a decision you made once and a decision that keeps getting remade without you.

4. Did anyone read the diff, or only the summary? These are not the same review, and the summary is the one that feels sufficient.

5. What is the one gate between this and production that a human actually has to walk through?

That last one is the only question that changes anything. The others describe your exposure. This one decides whether you have a process or just a habit.

None of this is an argument against building with agents. I shipped a set of six of them last week and I use them daily. What I'd argue is that delegation and distance look identical right up until something goes wrong, and the thing that separates them is a gate you put there on purpose.

What's your actual review step before an AI-built change ships? I'm genuinely curious how many people have one.

---

**Posting notes**

- Best window: Monday or Tuesday, 8 to 10 AM CDT.
- The numbered list is the screenshot-able asset. Keep the line breaks generous so it renders cleanly in the feed.
- The closing question is a real one, so reply to responses rather than letting them sit.
- Pair with the carousel a day or two later rather than the same day.
