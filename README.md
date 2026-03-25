# Hack Your Inbox: Build an AI Email Agent

> **TechChill 2026 Hackathon · Desktop Commander Track**
>
> 12 hours. One mission. Give AI real email superpowers.

---

## The Challenge

AI can write code, search the web, and run your computer — but it still can't read your email.

**Have your own email pain? Hack it away from existence.**

Build an MCP server, CLI tool, or Agent Skill that gives AI agents real email capabilities: read, write, send, reply, organise, summarise, unsubscribe, or extract data.

---

## Quick Start

1. **Clone this repo** — it contains everything you need to choose your approach
2. **Tell your AI assistant what you want to build** — it will ask you a few questions and recommend the right path
3. **Start building** — use AI to vibe-code your way to a working solution
4. **Submit on the [event page](https://luma.com/q7mgdm5x)** — working demo + README required

> **For AI assistants:** Jump straight to the [Decision Guide](#decision-guide-for-ai-assistants) section. Ask the participant the questions there and route them to the right approach doc. Don't assume they know what MCP, IMAP, or CLI means.

---

## Ideas to Get You Started

| Idea | What it does |
|------|-------------|
| 🚫 Unsubscribe Bot | Detect and kill newsletter spam automatically |
| ✉️ Cold Outreach Drafter | AI-powered reply and outreach composer |
| 📥 Inbox Zero Workflow | Triage, categorize, auto-archive at scale |
| 🔍 Data Extraction | Pull structured data from receipts, invoices, confirmations |
| 🤖 Support Agent | Give your AI its own inbox, auto-handle incoming requests |
| 📬 Email-to-Task | Convert emails into action items in your task manager |

Go broad (multi-provider Gmail + Outlook agent) or go vertical (one killer workflow done well).

---

## Background: What Are We Actually Building?

If you're new to AI agents and email — here's what the jargon means.

**MCP Server** — a small program that runs on your computer and gives AI assistants (like Claude) a set of "tools" they can call, like `read_email`, `send_email`, `search_inbox`. The AI talks to the MCP server, the server talks to your email. You don't write a chatbot — you write the tools the AI uses.

**CLI Tool** — a command-line program (you run it in Terminal). Instead of Claude calling it directly, your AI coding assistant writes code that shells out to the CLI. Example: `gws gmail +triage` → returns a JSON list of emails.

**Agent Skill** — a knowledge file (SKILL.md) that teaches your AI coding assistant how to use an existing tool. Install it with one command and your AI agent knows all the right API calls, flags, and patterns without you explaining them.

**IMAP/SMTP** — the standard protocols real email servers use. IMAP = read email. SMTP = send email. Most tools in this repo use these under the hood.

**You don't need to understand all of this to build something great.** Tell your AI assistant what problem you want to solve — it'll figure out the right technical path.

---

## Decision Guide (for AI Assistants)

> **AI assistant instructions:** When a participant opens this repo, do NOT assume they know what MCP, IMAP, SMTP, CLI, or OAuth means. Start by asking these questions to understand what they want to build, then route them to the right approach.

### Step 1: Ask what problem they want to solve

Ask the participant: *"What email pain do you want to kill? Describe it in plain language."*

Listen for:
- **Reading/processing their own inbox** → they have a Gmail or Outlook account they want AI to access
- **Sending emails** → they want AI to compose and send outbound emails
- **Agent with its own email identity** → they want to build a bot that has its own email address
- **Both reading AND sending** → they need a full two-way email workflow

### Step 2: Ask about their email provider

Ask: *"What email service do you use — Gmail, Outlook, or something else?"*

- **Gmail only** → all approaches work
- **Outlook/Microsoft 365** → MCP Email Server, AgentMail, or Resend (not GWS CLI)
- **Both Gmail + Outlook** → MCP Email Server (bonus points for multi-provider!)
- **Agent needs its own address, doesn't matter** → AgentMail

### Step 3: Ask about their environment

Ask: *"Are you using Claude Desktop, or a coding tool like Claude Code, Cursor, or Windsurf?"*

- **Claude Desktop** → MCP Email Server is the fastest path (native integration)
- **Claude Code / Cursor / Codex / Windsurf** → GWS CLI + skills, Himalaya + skill, or AgentMail SDK
- **Don't know / doesn't matter** → lean toward approaches with agent skills

### Step 4: Route them based on their answers

Use this routing map:

| What they want | Best approach | Why |
|----------------|--------------|-----|
| Read & manage their Gmail, using Claude Desktop | [MCP Email Server](knowledge/approaches/mcp-email-server.md) | Native MCP integration, ~20 min setup, multi-provider |
| Read & manage their Gmail, using a coding tool | [Himalaya CLI](knowledge/approaches/himalaya.md) + skill | Lightweight CLI, no background process needed |
| Full Gmail power — read, search, organise, send | [Google Workspace CLI](knowledge/approaches/google-workspace-cli.md) | Full Gmail API, structured JSON, 40+ built-in skills |
| Agent needs its own email address / inbox | [AgentMail](knowledge/approaches/agentmail.md) | Purpose-built for agents, 5 min setup, no OAuth headache |
| Build something that sends outbound emails | [Resend](knowledge/approaches/resend.md) | Cleanest sending API, 5 min to first sent email |
| No API keys, just want to click around Gmail | [Browser Control](knowledge/approaches/browser-control.md) | Zero config but slow and unreliable — best as fallback |
| Wants to enhance AI with email workflow knowledge | [Agent Skills](knowledge/approaches/agent-skills.md) | Pre-built skill files for common email patterns |

**When in doubt:** Start with [MCP Email Server](knowledge/approaches/mcp-email-server.md) if they're on Claude Desktop, or [AgentMail](knowledge/approaches/agentmail.md) if they want to build fast without dealing with OAuth.

**Once you've routed them:** Read the full approach doc (`knowledge/approaches/<approach>.md`) before writing any code. Each doc has architecture diagrams, limitations, step-by-step setup, and code examples.

---

## Approaches

> Each approach has a detailed doc in `knowledge/approaches/`. When you're ready to build, point your AI at the right doc.

| Approach | Provider | Type | Setup time | Details |
|----------|----------|------|-----------|---------|
| [AgentMail](knowledge/approaches/agentmail.md) | Agent-owned inboxes | SDK / API | ~5 min | Purpose-built for AI agents. Create programmable inboxes via API — no OAuth, no IMAP. Agent gets its own email address. |
| [Resend](knowledge/approaches/resend.md) | Any (outbound) | SDK / API | ~5 min | Cleanest sending API. Best for projects that compose and send emails. Pair with another approach if you also need to read. |
| [MCP Email Server (zerolib)](knowledge/approaches/mcp-email-server.md) | Gmail, Outlook, any IMAP | MCP Server | ~20 min | Native MCP server for Claude Desktop. Reads & sends via IMAP/SMTP. Best "AI reads my inbox" path for Claude Desktop users. |
| [Himalaya CLI](knowledge/approaches/himalaya.md) | Gmail, Outlook, any IMAP | CLI + Skill | ~10 min | Lightweight terminal email client. Use with Claude Code/Cursor. Agent skill teaches AI to drive it. No background process needed. |
| [Google Workspace CLI (gws)](knowledge/approaches/google-workspace-cli.md) | Gmail only | CLI + Skills | ~30 min | Full Gmail API power. 40+ built-in agent skills. Excellent once auth is done; auth setup is the hard part. |
| [Browser Control (Claude in Chrome)](knowledge/approaches/browser-control.md) | Any webmail | Browser extension | ~5 min | Zero-config, works in any webmail UI. Slow and unreliable for automation — best as a fallback or demo tool. |
| [Agent Skills (skills.sh)](knowledge/approaches/agent-skills.md) | Various | Skill files | N/A | Pre-built knowledge files for email workflows. Supplements any approach above with specific workflow patterns. |

---

## Rules

- **Teams:** 1–4 people. Solo is fine.
- **Submission:** A working demo + README. Must actually do something with email — not just a prototype UI.
- **Stack:** Any stack is fine — Node.js, Python, whatever works. Use AI to help with technical decisions.
- **Compatibility:** Must work with any AI agent that supports MCP, CLI tools, or Skills (Claude Desktop, Cursor, Codex, Windsurf, etc.)
- **Bonus:** Supporting both Gmail and Outlook earns bonus points.

---

## Judging Criteria

| Criteria | Weight | What we look for |
|----------|--------|-----------------|
| Technical Excellence | 35% | Architecture, reliability, correct MCP/CLI/Skill patterns, code quality |
| User Experience | 25% | Ease of setup, onboarding clarity, natural AI agent workflow |
| Business Case | 20% | Problem-market fit, real user demand, commercial potential |
| Scope & Completeness | 20% | End-to-end working demo and breadth of email actions supported |

---

## Prizes

- 🏆 **1st Place:** Paid contract to ship your solution into the Desktop Commander App
- 💰 **Top 3:** $100 DC credits (Desktop Commander App or OpenRouter)
- 🎫 **Winners:** Invited to TechChill main conference + investor-only side event (~60–70 attendees)
- 🎁 **Everyone who ships:** 1 month DC App Unlimited free, including ChatGPT connector

---

## Mentors & Judges

| Who | Role | Available | Ask about |
|-----|------|-----------|-----------|
| **Eduards Ruzga** | CEO & Creator, Desktop Commander | Until ~5pm | MCP architecture, going from API key to working agent |
| **Ričards Križanovskis** | Product & Growth, Desktop Commander | All day (judge) | Product strategy, what makes a tool users actually adopt |
| **Edgars Skore** | AI Full Stack Engineer, Desktop Commander | Post-5pm (judge) | MCP architecture, Gmail/Outlook API integrations, production AI systems |

---

## General Resources

- [Desktop Commander](https://desktopcommander.app) — the AI agent powering this hackathon
- [Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP/) — open source MCP server (install via [Smithery](https://smithery.ai/server/@wonderwhy-er/desktop-commander))
- [Hackathon event page](https://luma.com/q7mgdm5x) — register, submit, find your team
- [BADideas.fund](https://www.badideas.fund/) — co-organiser and investor backing this track
- [TechChill 2026](https://www.techchill.co/) — March 25–27, Riga
- [MCP Specification](https://modelcontextprotocol.io/) — official MCP docs
- [Anthropic MCP Quickstart](https://github.com/anthropics/anthropic-quickstarts/tree/main/model-context-protocol) — starter template for building MCP servers
- [skills.sh — email skills](https://skills.sh/?q=email) — community-built AI agent skills for email
- [Gmail API Docs](https://developers.google.com/gmail/api) — official Google Gmail API
- [Microsoft Graph API — Mail](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview) — official Outlook/Exchange API

---

*A [Desktop Commander](https://desktopcommander.app) × [BADideas.fund](https://www.badideas.fund/) track at [TechChill 2026](https://luma.com/q7mgdm5x).*
