# Agent Skills (skills.sh)

> Community-built skills that teach AI agents how to work with email. Install with a single command. Many available — explore and pick what fits your use case.

## What It Is

[skills.sh](https://skills.sh) is an open directory of reusable AI agent skills — essentially instruction sets that teach agents (Claude Code, Cursor, Codex, Windsurf, etc.) how to use specific tools and APIs. You install a skill with `npx skills add <repo>` and it becomes available context for your AI agent.

**Directory:** https://skills.sh/?q=email

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  AI Agent (Claude Code, Cursor, Codex, etc.)         │
│  Reads skill instructions as context                 │
└──────────────┬───────────────────────────────────────┘
               │ Follows skill's instructions to run commands
               ▼
┌──────────────────────────────────────────────────────┐
│  Installed Skill (SKILL.md in your project)          │
│  - Procedural knowledge: "how to do X"               │
│  - Command reference, flags, examples                │
│  - Best practices and error handling                 │
└──────────────┬───────────────────────────────────────┘
               │ Agent executes the CLI/API commands described
               ▼
┌──────────────────────────────────────────────────────┐
│  Underlying Tool (gws CLI, Resend API, npm package)  │
│  The skill doesn't replace the tool — it teaches     │
│  the agent how to use it effectively                 │
└──────────────────────────────────────────────────────┘
```

**The key thing to understand:** Skills are NOT tools themselves. They're knowledge files (SKILL.md) that tell an AI agent how to use an existing tool. A Gmail skill doesn't connect to Gmail — it teaches the agent the right `gws` commands, flags, and patterns to use with the Google Workspace CLI.

## Interesting Email-Related Skills

> **We haven't tested these skills ourselves.** Explore them and evaluate what fits your use case.

### Google Workspace CLI Skills (111 skills, 445K+ total installs)

The `googleworkspace/cli` repo ships with a large library of skills. Email-relevant ones include:

| Skill | What it teaches the agent | Installs |
|-------|--------------------------|----------|
| [gws-gmail](https://skills.sh/googleworkspace/cli/gws-gmail) | Core Gmail operations — read, search, manage messages | 8.4K |
| [gws-gmail-triage](https://skills.sh/googleworkspace/cli/gws-gmail-triage) | Inbox triage workflow | 6.3K |
| [gws-gmail-send](https://skills.sh/googleworkspace/cli/gws-gmail-send) | Sending emails via CLI | 6.3K |
| [gws-gmail-watch](https://skills.sh/googleworkspace/cli/gws-gmail-watch) | Watching for new emails in real-time | 5.9K |
| [gws-workflow-email-to-task](https://skills.sh/googleworkspace/cli/gws-workflow-email-to-task) | Convert Gmail messages into Google Tasks entries | 4.6K |
| [recipe-create-gmail-filter](https://skills.sh/googleworkspace/cli/recipe-create-gmail-filter) | Create Gmail filters programmatically | 4.6K |
| [recipe-save-email-attachments](https://skills.sh/googleworkspace/cli/recipe-save-email-attachments) | Download and save email attachments | 4.4K |
| [recipe-label-and-archive-emails](https://skills.sh/googleworkspace/cli/recipe-label-and-archive-emails) | Bulk label and archive emails | 4.3K |
| [recipe-save-email-to-doc](https://skills.sh/googleworkspace/cli/recipe-save-email-to-doc) | Save email content to Google Docs | 4.3K |
| [recipe-draft-email-from-doc](https://skills.sh/googleworkspace/cli/recipe-draft-email-from-doc) | Draft emails from Google Doc content | 4.4K |
| [recipe-email-drive-link](https://skills.sh/googleworkspace/cli/recipe-email-drive-link) | Email Google Drive file links | 4.4K |
| [gws-workflow-weekly-digest](https://skills.sh/googleworkspace/cli/gws-workflow-weekly-digest) | Generate weekly email digest | 4.5K |
| [persona-exec-assistant](https://skills.sh/googleworkspace/cli/persona-exec-assistant) | Executive assistant persona across Gmail, Calendar, Drive | 4.5K |

**Note:** These skills require the Google Workspace CLI (`gws`) to be installed and authenticated. See [our GWS CLI approach doc](google-workspace-cli.md) for setup.

Install all GWS skills: `npx skills add googleworkspace/cli`

### Resend Skills — Transactional Email Sending

| Skill | What it teaches the agent | Installs |
|-------|--------------------------|----------|
| [send-email](https://skills.sh/resend/resend-skills/send-email) | Send single or batch emails via Resend API (Node.js, Python, Go, etc.) | — |

Resend is a developer-focused email sending API. This skill teaches agents how to send transactional emails with proper error handling, idempotency keys, and retry logic. Good for outbound email workflows (cold outreach, notifications) but doesn't help with reading/receiving email.

**Requires:** Resend API key and a verified sending domain.

### Agent Email CLI — Disposable Mailboxes

| Skill | What it teaches the agent | Installs |
|-------|--------------------------|----------|
| [agent-email-cli](https://skills.sh/zaddy6/agent-email-skill/agent-email-cli) | Create and read disposable email accounts for agent workflows | 19.8K |

This is interesting — it lets agents create throwaway mailboxes on the fly, read incoming messages, and manage multiple accounts. Useful for testing, sign-up flows, or building agents that need their own email addresses. The agent can create a mailbox with `agent-email create`, then poll for new messages with `agent-email read`.

**Requires:** `npm install -g @zaddy6/agentemail`

**Caveat:** Very new (first seen 3 days ago), only 1 GitHub star. Snyk security audit shows a warning. Use with caution.

## Getting Started

```bash
# Install any skill into your project
npx skills add <owner/repo> --skill <skill-name>

# Examples:
npx skills add googleworkspace/cli --skill gws-gmail
npx skills add resend/resend-skills --skill send-email
npx skills add zaddy6/agent-email-skill --skill agent-email-cli
```

This creates a `SKILL.md` file in your project that your AI agent reads as context.

## Our Assessment

**We haven't tested these skills.** The listings above are based on what's available on skills.sh and what looked potentially relevant. Many of the email-related skills on skills.sh are more about procedural knowledge (how to compose good emails, email marketing best practices) rather than actual email API integration.

The most promising ones for the hackathon are:
- **GWS CLI skills** — if you're already using the Google Workspace CLI, these give your agent pre-built workflows (triage, filter creation, email-to-task conversion)
- **Agent Email CLI** — interesting if you need disposable mailboxes for testing or agent-owned email accounts
- **Resend** — solid if your project is about sending emails rather than reading them

**Best for hackathon teams who:** want to enhance their AI agent's knowledge about how to use email tools effectively, or want pre-built workflow patterns they can build on top of.

## Links

- [skills.sh — email skills](https://skills.sh/?q=email) — browse the full directory
- [skills.sh docs](https://skills.sh/docs) — how skills work
- [Google Workspace CLI skills (111 skills)](https://skills.sh/googleworkspace/cli)
- [Resend email skills](https://skills.sh/resend/resend-skills/send-email)
- [Agent Email CLI](https://skills.sh/zaddy6/agent-email-skill/agent-email-cli)
