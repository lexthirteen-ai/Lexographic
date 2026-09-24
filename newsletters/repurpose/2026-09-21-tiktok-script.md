# TikTok Script: Your AI coding tool might already be hacked

Source: Artificially Designed, September 21, 2026. Flavor: spicy take. Target: 60 seconds.

## Hook (first 2 seconds)

"Your AI coding tool might already be hacked, and nothing on your screen would tell you."

## Full script (estimated 60s)

**Hook:** [Direct to camera, no intro, start mid-thought] "Your AI coding tool might already be hacked, and nothing on your screen would tell you."

**Pain:** "If you're building with Claude Code, Codex, Copilot, or Gemini CLI, you've probably installed a plugin at some point. You checked it once, it looked fine, you moved on. And every one of those tools pins plugins to a commit hash, which is supposed to mean the code you approved is the code that keeps running."

**Reframe:** "Researchers at Air published this last week. That pin does not hold. An attacker makes a branch, names it the exact same forty character hash your tool pinned, and sets it as the default. Git sees a branch and a commit with the same name, and picks the branch. So you get their code, under your approved hash. And because plugins auto-update, it lands without you clicking anything. They called it Plugin4Shell. It hit all four major coding agents."

**Takeaway:** "So go check your version right now. Claude Code patched it in 2.1.179. Codex in 0.146.0. Copilot has no fix yet, so turn off plugin auto-update. And Gemini CLI got deprecated instead of patched, which means it stays exposed."

**CTA:** "I write about this stuff every week in Artificially Designed. Link in bio."

## B-roll / overlay

- 0-2s. Talking head only. Let the line land cold. **Essential.**
- 12-25s. Screen recording of a terminal showing `git checkout <hash>` resolving to a branch. Sells the mechanism better than words. **Nice to have.**
- 25-32s. Text overlay: "Plugin4Shell" with the four tool names stacked underneath. **Essential**, since the name is the searchable hook.
- 40-55s. Text overlay of the version numbers, on screen the whole time you say them. People will screenshot this. **Essential.**
- 55-60s. Talking head, no overlay. Soft close.

## Caption

Four AI coding tools, one bypass, and two vendors who decided not to fix it. Check your version number tonight.

## Hashtags

#vibecoding #aiforfounders #founderlife #aitools #devtools #artificiallydesigned

## Production notes

- Estimated film time: 15 minutes, one or two takes.
- The version numbers are the whole payload. Say them slowly and keep them on screen.
- Do not soften "hacked" in the hook. The specificity is what stops the scroll, and the body of the script earns it back.
