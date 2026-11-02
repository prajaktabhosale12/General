# General

## Idea → Web App prompt

Run `/idea <your idea>` in Claude Code from this repo, for example:

```
/idea A web app where neighbours lend and borrow tools, with ratings and pickup scheduling
```

It goes through 5 phases: visualise, brainstorm, refine requirements, plan, then execute.
It stops at a checkpoint after each phase and waits for your approval.
The prompt is in [`.claude/commands/idea.md`](.claude/commands/idea.md). Outside Claude Code,
paste that file into a chat and replace `$ARGUMENTS` with your idea.
