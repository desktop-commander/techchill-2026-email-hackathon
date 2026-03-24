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
2. **Pick your pain** — what email problem do you want to kill?
3. **Choose an approach** — see [Approaches](#approaches) below
4. **Start building** — use AI to vibe-code your way to a working solution

> **Tip for AI assistants:** Read this entire README first. Then read the relevant approach file from `knowledge/approaches/` based on what the participant wants to build.

---

## Ideas to Get You Started

| Idea | What it does |
|------|-------------|
| 🚫 Unsubscribe Bot | Detect and kill newsletter spam automatically |
| ✉️ Cold Outreach Drafter | AI-powered reply and outreach composer |
| 📥 Inbox Zero Workflow | Triage, categorize, auto-archive at scale |
| 🔍 Data Extraction | Pull structured data from receipts, invoices, confirmations |

Go broad (multi-provider Gmail + Outlook agent) or go vertical (one killer workflow done well).

---

## Rules

- **Teams:** 1–4 people. Solo is fine.
- **Submission:** A working demo + README. Must actually do something with email — not just a prototype UI.
- **Stack:** Any stack is fine — Node.js, Python, whatever works. Use AI to help with technical decisions.
- **Compatibility:** Must work with any AI agent that supports MCP, CLI tools, or Skills (Claude Desktop, Cursor, Codex, Windsurf, etc.)
- **Bonus:** Supporting both Gmail and Outlook earns bonus points.

---

## How to Pick an Approach

Tell your AI assistant what email problem you want to solve, and it will recommend the best tools from this repo.

**Key questions to answer first:**
- What email provider(s) do you need? (Gmail, Outlook, both?)
- What actions do you need? (read, send, organize, extract data?)
- Do you want to build an MCP server, CLI tool, or Agent Skill?
- What's your comfort level? (API from scratch vs. existing tools)

**"I want to build fast with existing tools"**
→ Look for approaches marked as MCP servers or CLI tools — plug in and go.

**"I want full control over email actions"**
→ Build directly on Gmail API or Microsoft Graph SDK — more work, more flexibility.

**"I want to go through the browser"**
→ Browser Use MCP can control webmail UIs directly — no API keys needed, but less reliable.

**"I want multi-provider support"**
→ Look for tools that abstract across Gmail + Outlook, or build an adapter layer.

---

## Approaches

> Each approach has a summary here and a detailed doc in `knowledge/approaches/`. Point your AI at the detailed doc when you're ready to build.

| Approach | Provider | Type | Details |
|----------|----------|------|---------|
| [Google Workspace CLI (gws)](knowledge/approaches/google-workspace-cli.md) | Gmail | CLI | Full Gmail API access, JSON output, helper commands. Setup takes 15–30 min (GCP auth). Once configured, excellent. |
| [MCP Email Server (zerolib)](knowledge/approaches/mcp-email-server.md) | Gmail, Outlook, any IMAP | MCP Server | Native MCP server for Claude Desktop. IMAP/SMTP based, multi-account, ~20 min setup. Fastest path to AI email access. |
| [Browser Control (Claude in Chrome)](knowledge/approaches/browser-control.md) | Any webmail provider | Browser extension | Zero-config, works with any email UI in Chrome. Great setup, but slow and unreliable for anything beyond basic inbox reading. |
| [Agent Skills (skills.sh)](knowledge/approaches/agent-skills.md) | Various | Skills / Knowledge | Pre-built agent skills for email workflows. GWS CLI skills, Resend sending, disposable mailboxes. Not tested by us — explore and evaluate. |

<!-- 
HOW TO ADD A NEW APPROACH:
1. Create a detailed doc in knowledge/approaches/your-approach.md
2. Add a row to the table above: | [Name](knowledge/approaches/filename.md) | Gmail/Outlook/Both | MCP/CLI/Skill | Short description |
3. Add a short summary section below the table
-->

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

- [Anthropic MCP Quickstart](https://github.com/anthropics/anthropic-quickstarts) — starter template for building MCP servers
- [MCP Specification](https://modelcontextprotocol.io/) — official MCP docs
- [skills.sh — email skills](https://skills.sh/?q=email) — community-built AI agent skills for email
- [Gmail API Docs](https://developers.google.com/gmail/api) — official Google Gmail API
- [Microsoft Graph API — Mail](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview) — official Outlook/Exchange API
- [Desktop Commander](https://desktopcommander.app) — AI that executes
- [Desktop Commander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP/) — open source MCP server
- [BuilderBase Event](https://www.builderbase.com/v2/event/build-bad-ideas) — submissions and team formation
- [TechChill 2026](https://www.techchill.co/) — March 25–27, Riga

---

*Built for BADideas.fund × TechChill 2026 hackathon by the [Desktop Commander](https://desktopcommander.app) team.*
