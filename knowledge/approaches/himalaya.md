# Himalaya CLI

> A terminal email client for managing your real Gmail, Outlook, or any IMAP inbox — without building an MCP server or writing API integration code. If the MCP Email Server feels like too much infrastructure, Himalaya is your lightweight alternative.

## What It Is

[Himalaya](https://github.com/pimalaya/himalaya) is an open-source CLI email client written in Rust. It connects to real email accounts via IMAP (reading) and SMTP (sending) — the same protocols as the MCP Email Server — but packages everything as a simple terminal command you can call from anywhere.

There's an official **agent skill** for Himalaya on skills.sh, which means your AI agent (Claude Code, Cursor, Codex) can learn to drive Himalaya commands and use them to build email workflows without you writing any integration code.

**skills.sh:** https://skills.sh/moltbot/moltbot/himalaya  
**Repo:** https://github.com/pimalaya/himalaya

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  Your AI Agent (Claude Code, Cursor, Codex, etc.)    │
│  Reads Himalaya skill → runs himalaya CLI commands   │
└──────────────┬───────────────────────────────────────┘
               │ Shell commands (e.g. himalaya message list)
               ▼
┌──────────────────────────────────────────────────────┐
│  himalaya CLI binary (Rust, local)                   │
│  - Parses commands                                   │
│  - Manages account config (~/.config/himalaya/)      │
│  - Handles IMAP/SMTP connections                     │
│  - Outputs structured JSON or plain text             │
└──────────────┬───────────────────────────────────────┘
               │ IMAP (read) / SMTP (send) over TLS
               ▼
┌──────────────────────────────────────────────────────┐
│  Your real email server                              │
│  Gmail · Outlook/M365 · Any IMAP/SMTP provider      │
└──────────────────────────────────────────────────────┘
```

**Key things to understand:**

1. **It's a local CLI binary** — no cloud service, no MCP server process, no Python runtime needed. Just a single Rust binary on your machine.
2. **Connects to your real inbox** — unlike AgentMail (which creates new agent-owned addresses), Himalaya reads the Gmail or Outlook account you already have.
3. **Simple setup via interactive wizard** — run `himalaya account configure` and answer prompts. No manual JSON editing or GCP project required.
4. **Agent skill teaches AI to use it** — install the Himalaya skill and your AI agent knows all the right commands, flags, and patterns to automate email tasks.
5. **JSON output** — by default outputs JSON, making it easy to pipe into other tools or parse in scripts.

**Comparison to MCP Email Server:** Both use IMAP/SMTP. The difference is delivery mechanism — Himalaya is a CLI your agent calls via shell, while the MCP Email Server is an MCP server Claude Desktop talks to natively. Himalaya is simpler to set up and works in any coding environment (not just Claude Desktop).

## Capabilities

- **List messages** — browse inbox, sent, any folder
- **Read messages** — full content with headers, body, attachments
- **Send emails** — compose and send via SMTP
- **Reply and forward** — with proper threading
- **Folder/mailbox management** — list, switch, create folders
- **Flag management** — mark as read/unread, flagged, deleted
- **Attachment handling** — download and save attachments
- **Search** — filter messages by subject, sender, date, flags
- **Multiple accounts** — configure and switch between accounts
- **Backends** — IMAP, SMTP, Notmuch, Sendmail

## Limitations

- **Gmail requires App Password** — same as the MCP Email Server. You need 2FA enabled, then generate a 16-character App Password at myaccount.google.com/apppasswords. No OAuth flow.
- **No full-text body search** — search is by metadata fields (sender, subject, date), not full content search across all emails.
- **Local only** — credentials stored in config file on your machine. Not a cloud service.
- **CLI-first** — no GUI. This is a terminal tool.
- **Active development** — API and config format may change between versions. Pin to a stable version.
- **Not an MCP server** — to use with Claude Desktop natively, you'd still need to wrap it in an MCP server (or use the MCP Email Server approach instead).

## Getting Started

### Step 1: Install Himalaya

```bash
# macOS
brew install himalaya

# Linux
curl -sSf https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh | sh

# cargo
cargo install himalaya
```

### Step 2: Configure an account

Run the interactive wizard:

```bash
himalaya account configure
```

Answer the prompts:
- Account name (e.g. `gmail`)
- Email address
- Choose backend: `IMAP` for reading, `SMTP` for sending
- IMAP host: `imap.gmail.com`, port `993`
- SMTP host: `smtp.gmail.com`, port `587`
- Password: use your Gmail App Password (not your regular password)

> **Gmail App Password:** Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords), create one, copy the 16-character code.

### Step 3: Test it

```bash
himalaya message list                    # List inbox messages
himalaya message read <id>               # Read a specific message
himalaya message send                    # Compose and send
himalaya folder list                     # List all folders
himalaya --account work message list     # Use a specific account
```

### Step 4: Install the agent skill

```bash
npx skills add moltbot/moltbot --skill himalaya
```

Once installed, your AI agent (Claude Code, Cursor, etc.) knows all Himalaya commands and can build email automation scripts on top of your real inbox.

## Install the Skill

```bash
npx skills add moltbot/moltbot --skill himalaya
```

## Our Assessment

**Setup: ~10 minutes.** Simpler than the GWS CLI (no GCP project needed) and doesn't require running a background process like the MCP Email Server. Good fit for developers who prefer CLI tools and want their agent to script against their real inbox.

**Best for:** Hackathon teams building automation tools on top of existing Gmail/Outlook accounts, who want lightweight CLI-based access without the MCP server setup overhead, and who are using Claude Code, Cursor, or Codex (not Claude Desktop).

**Not the right choice if** you're using Claude Desktop — use the MCP Email Server instead, which integrates natively. Also not the right choice if you need your agent to have its own email identity — use AgentMail for that.

## Links

- [Himalaya repo](https://github.com/pimalaya/himalaya)
- [Himalaya docs](https://pimalaya.org/himalaya/)
- [skills.sh skill](https://skills.sh/moltbot/moltbot/himalaya)
- [Gmail App Passwords](https://myaccount.google.com/apppasswords)
