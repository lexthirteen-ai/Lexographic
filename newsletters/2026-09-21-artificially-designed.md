# Artificially Designed, September 21, 2026

**SUBJECT LINE:** your pinned plugin isn't pinned

**PREVIEW TEXT:** Four coding agents, one bypass, and two vendors who decided not to fix it.

---

## Section 1: Personal Intro

Last Tuesday I gave a coordinator agent a brief, closed my laptop, and went to make dinner. When I came back there were four finished subagent threads and a summary waiting, and I read the summary. Just the summary.

I did not look at what any of them had installed to get the work done, or what they fetched, or where they fetched it from. I read the top-level output the way you skim an invoice from a contractor you already like, and I approved it.

Then the Plugin4Shell writeups started landing on Wednesday, and I went back and looked properly, and I want to be honest that the looking took about forty minutes and I did not enjoy any of it.

This issue is about that gap. Not about agents being dangerous, because I am still using them today. About the distance between what I handed off and what I actually reviewed, and how fast that distance grew without me ever deciding it should.

---

## Section 2: Theme Exploration

Two things happened this month that belong in the same sentence, though most of the coverage kept them apart.

The first is that vibe coding quietly became vibe managing. Cursor shipped its version on September 10, Claude Code shipped Projects in beta on the 17th, and both work the same way. A coordinator agent takes your brief, plans the work, delegates it to parallel threads, reviews what comes back, and keeps running after you close the laptop. The unit of work stopped being a prompt and became an assignment.

The second is Plugin4Shell, published this week by the research team at Air. It hit all four major coding agents, and the mechanism is almost rude in how simple it is. These tools pin plugins to a commit hash so that reviewed code stays reviewed code. An attacker creates a branch named identically to that forty character hash, makes it the default branch, and git quietly resolves the branch instead of the commit. Your pinned plugin was never pinned. Plugin auto-update means the swap arrives without a single click from you.

Put those two together and you get the real story, which is that we went from reading every suggestion before accepting it to reading a summary of work done by agents that fetch their own tools, and we did it in about six months, and the trust surface moved right along with us.

This is not hypothetical. OpenAI's own testing agents flooded RubyGems with more than two thousand junk packages on September 13, which is an ordinary task reaching shared infrastructure nobody scoped it to touch. Dario Amodei spent September 12 and 13 warning that coordinated agent swarms could take significant portions of the internet inside six to twelve months without identity and permission controls built at the harness level.

A handoff with no gate at the end of it is not really delegation, and the word does a lot of quiet work covering the difference.

---

## Section 3: Tool Spotlight

**TOOL:** Lovable WhatsApp Business connector

**WHAT IT DOES:** Connects a Lovable app to WhatsApp Business so it can send and receive real customer messages, with no separate backend to build.

**WHO IT'S FOR:** A founder with a working Lovable MVP who needs appointment reminders, intake follow-ups, or order updates, and has no engineer to wire up messaging.

**THE HONEST TAKE:** It landed September 15 and it genuinely removes the backend step, which is the hard part for most non-technical builders. What it does not remove is WhatsApp Business template approval, opt-in rules, or your own consent and retention obligations if the messages touch anything health related. Good for shipping real operations, not a shortcut around compliance.

**TRY IT FOR:** One appointment reminder flow, sent to yourself, start to finish, before it touches a single real customer.

---

## Section 4: Prompt for Productivity

**THE PROMPT**

```
I handed this task to an AI agent and approved the result without
reviewing the intermediate steps.

TASK I GAVE IT: [paste the brief]
WHAT CAME BACK: [paste or summarize the output you approved]
TOOL: [Claude Code, Codex, Cursor, Lovable, other]

Work backward and tell me:
1. What files, repos, packages, or plugins this task most likely
   required it to install or fetch.
2. Which of those came from sources I never explicitly named.
3. What it could have done that would not appear in the output I read.
4. The single checkpoint that, had it existed, would have caught
   the most.

Do not reassure me. If the honest answer to any of these is "you
cannot tell from here," say that, and tell me what I would need to
look at instead.
```

**WHEN TO USE IT**

After any agent run where you read the summary and not the steps, which for most of us is most of them.

**WHAT IT DOES**

It reconstructs the blast radius of a handoff you have already made, which is a more useful question than whether the output looks correct. That last line is load bearing, because the standard failure of asking an AI to audit an AI is a confident and comforting answer.

**TIP**

Run it against your most routine recurring task rather than your scariest one. The scary ones you are already watching.

---

## Section 5: Quick Wins

- Open Claude Code and check your version. Anything below 2.1.179 is exposed, and updating is the whole fix.
- On Codex, the patch landed in 0.146.0.
- Gemini CLI was deprecated instead of patched, so its Plugin4Shell exposure is permanent. Anything you install into it from a repo you do not control can be swapped under you, and auto-update means silently. Antigravity is unaffected if you need somewhere to move that work.
- Copilot has no vendor fix. Turn off plugin auto-update and go look at what is already installed.

---

## Section 6: Behind the Scenes

I shipped Stellar Agents this week, and the timing was not planned.

Six agents that run a one person practice. Carina plans the week, Aurora triages the inbox, Lyra drafts, Vesper checks the draft, Selene keeps the record, and Mira audits the other five and reports what drifted. They are free, they install into Claude Code, Codex, and a few other tools, and they live at [github.com/lexthirteen-ai/stellar-agents](https://github.com/lexthirteen-ai/stellar-agents).

The rule I kept returning to while building them is the one this whole issue circles. Every star stops one step before anything goes out. The pipeline ends at STAGED, and a human carries it across in the real tool. That last step is where I want to still be standing.

If you want the smallest possible taste, run `ai-tell-check` on something you have already written. Vesper names the tells and never rewrites a word.

---

## Section 7: Uncomfortable Question

What has an agent installed on your machine in the last month? Not what you installed. What did something you delegated to decide it needed, fetch on your behalf, and never mention. And if you wanted to check tonight, would you know where to look?

---

## Section 8: CTA

Clock In to AI is one hour, live, and you leave having built one real thing you can use at work tomorrow and having caught an AI mistake with your own eyes. That second half is this entire issue, compressed. [Come sit in](https://luma.com/u4nc3gjy).

---

*P.S. On October 28 at 8:30 CDT I'm running [Claude Loves Lovable: Brand Before You Build](https://members.centralexchange.org/events/details/virtual-claude-loves-lovable-brand-before-you-build-26154?calendarMonth=2026-10-01) with Central Exchange, on why your Lovable app keeps coming back a generic purple gradient. Free for CX members, $25 otherwise.*

---

## ISSUE SUMMARY

**Theme:** You are already managing agents you cannot see, and this week's news is what that costs.

**Pillar:** Vibe Coding / AI Fluency and Productivity

**Word count:** ~1,000

**Visual direction:** Soft System mode. A desk at night with one lamp on and a laptop closed, implied hand-off rather than activity, warm light against a dark room. Nothing on screen. 1200x600px for the Beehiiv header.

**Sources:** [air.security original research](https://www.air.security/blog-posts/plugin4shell) · [The Register](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335) · [Help Net Security](https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/) · [Claude Code changelog](https://code.claude.com/docs/en/changelog) · [Lovable changelog](https://docs.lovable.dev/changelog)
