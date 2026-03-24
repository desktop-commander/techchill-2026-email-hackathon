# Google Workspace CLI (gws)

> Unified CLI for Gmail, Drive, Calendar, and 40+ Google Workspace APIs. JSON output, helper commands, and built-in AI agent skills.

## What It Is

The Google Workspace CLI (`gws`) is a command-line tool maintained by the Google Workspace team that provides terminal access to all Google Workspace APIs. It dynamically generates its command surface from Google's Discovery Service — meaning it auto-supports new API endpoints as Google adds them.

**Repo:** https://github.com/googleworkspace/cli

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  Your AI Agent (Claude, Cursor, Codex, etc.)         │
│  Runs gws commands via terminal / shell              │
└──────────────┬───────────────────────────────────────┘
               │ CLI commands (e.g. gws gmail +triage)
               ▼
┌──────────────────────────────────────────────────────┐
│  gws CLI binary (Rust)                               │
│  - Parses commands                                   │
│  - Reads cached API schemas from Discovery Service   │
│  - Manages OAuth tokens (encrypted, OS keyring)      │
│  - Formats output (JSON / table / YAML / CSV)        │
└──────────────┬───────────────────────────────────────┘
               │ HTTPS REST API calls
               ▼
┌──────────────────────────────────────────────────────┐
│  Google Workspace APIs                               │
│  Gmail API · Drive API · Calendar API · etc.         │
│  (Google's servers)                                  │
└──────────────────────────────────────────────────────┘
```

**The key things to understand:**

1. **It's a local CLI binary** — written in Rust, runs on your machine. Not a cloud service, not an MCP server. You install it and call it from your terminal.
2. **It talks to Google's REST APIs over HTTPS** — every `gws` command translates into a Google Workspace API call. `gws gmail messages list` → `GET https://gmail.googleapis.com/gmail/v1/users/me/messages`.
3. **Auth is OAuth 2.0** — you create a Google Cloud project, get OAuth credentials, and the CLI handles token refresh. Tokens are encrypted with AES-256-GCM and stored in your OS keyring. The CLI never sees your Google password.
4. **Auto-generated commands** — the CLI reads Google's Discovery Service (a machine-readable API catalog) and generates its command surface automatically. This means it covers every Gmail API endpoint without manual coding.
5. **All output is structured JSON by default** — this is what makes it powerful for AI agents. Your agent runs a command, gets JSON back, parses it, decides what to do next.
6. **Helper commands (prefixed with `+`)** — shortcuts for common workflows. `+triage` shows a formatted inbox summary, `+send` composes an email, `+reply` replies to a message. These wrap multiple API calls into one.

**How an AI agent would use it:**
- Agent receives user instruction: "Check my inbox and summarize unread emails"
- Agent runs: `gws gmail +triage` → gets JSON list of unread emails
- Agent processes JSON, generates summary
- Agent runs: `gws gmail messages get --id <id> --format full` → reads full email body if needed
- Agent composes response, optionally runs: `gws gmail +reply --message-id <id> --body "..."`

**For hackathon builders:** You can build an MCP server or Agent Skill that wraps `gws` commands. Your tool calls `gws` via shell, parses the JSON output, and exposes email actions to any AI agent. This is the "glue" approach — gws handles the Google API complexity, you build the intelligence layer on top.

## Capabilities

**Gmail (our focus):**
- Email triage — view unread summaries with sender, subject, date (`gws gmail +triage`)
- Send emails — compose and send with recipients, subject, body
- Reply to messages — reply by message ID
- Watch for new emails — real-time monitoring
- Full Gmail API — list, get, modify, trash, manage messages, labels, drafts, threads

**Also supports:** Google Drive, Calendar, Sheets, Docs, Slides, Chat, Admin, Identity — all from the same CLI.

**Key features:**
- Structured JSON output — easy to pipe, parse, integrate with AI agents
- Auto-pagination (`--page-all`) for large result sets
- Dry-run mode — preview API requests before executing
- Helper commands — simplified workflows prefixed with `+` (e.g., `+send`, `+triage`, `+reply`)
- 40+ built-in AI agent skill definitions
- Multiple output formats: JSON (default), table, YAML, CSV

## Limitations

- **Gmail only** — no Outlook/Exchange support. Multi-provider requires pairing with another tool.
- **Complex auth setup (15–30 min)** — requires creating a Google Cloud project, enabling APIs, configuring OAuth consent screen, creating OAuth credentials, downloading client secret JSON. Multiple steps require navigating the Google Cloud Console UI manually.
- **OAuth consent screen is manual** — cannot be fully automated via CLI, you must visit the Cloud Console in a browser.
- **Permission gotchas** — if using an existing GCP project, you may hit PERMISSION_DENIED on API enablement. Creating a fresh project avoids this.
- **Testing mode limitation** — OAuth apps in "Testing" mode only work for explicitly added test users. Fine for personal/hackathon use, but broader deployment requires Google's verification process.
- **npm install can be messy** — may require sudo. Homebrew is the cleaner path on macOS.
- **Not an officially supported Google product** — it's maintained by the GWS team but without official support guarantees.

## Getting Started

### Step 1: Install

**macOS/Linux (recommended):**
```bash
brew install googleworkspace-cli
```

**Other options:**
- npm (requires Node.js 18+): `npm install -g @googleworkspace/cli`
- Cargo (from source): `cargo install --git https://github.com/googleworkspace/cli --locked`
- Pre-built binaries: [GitHub Releases](https://github.com/googleworkspace/cli/releases)

### Step 2: Set Up Authentication

This is the hard part. Budget 15–30 minutes.

1. **Create a Google Cloud project** — go to [console.cloud.google.com](https://console.cloud.google.com). Create a new project (avoid reusing existing ones to prevent permission issues).
2. **Enable APIs** — enable the Gmail API (and any other Workspace APIs you need) in your project.
3. **Configure OAuth consent screen** — go to APIs & Services → OAuth consent screen. Select "External" user type, provide app name and support email.
4. **Create OAuth Client ID** — go to APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID → Desktop app. Download the JSON file.
5. **Place credentials** — save the JSON to `~/.config/gws/client_secret.json`
6. **Authenticate** — run `gws auth login`. A browser window opens for Google sign-in.

> **Tip:** If `gws auth setup` partially fails, don't panic — create a fresh GCP project and do it manually. The CLI itself works great once auth is done.

### Step 3: Test It

```bash
gws gmail +triage              # View unread emails
gws gmail +send --to user@example.com --subject "Test" --body "Hello"
gws gmail +reply --message-id ID --body "Got it"
gws gmail +watch               # Watch for new emails
gws drive files list           # List Drive files
gws calendar events list       # List calendar events
gws auth login                 # Re-authenticate if needed
```

## Our Assessment

**Setup:** Doable but complex. The auth dance is the main barrier — not the CLI itself. A technically comfortable person should get through it in 15–30 min.

**Once configured:** Excellent. Reliable, full-featured Gmail access. Structured JSON output and helper commands make it a strong foundation for building email automation tools or integrating email into AI agent workflows.

**Best for hackathon teams who:** want full Gmail API power, are comfortable with a GCP setup process, and plan to build a CLI-based or MCP-based tool that needs read/write/send/organize capabilities.

## Links

- [Official repo](https://github.com/googleworkspace/cli)
- [Gmail API docs](https://developers.google.com/gmail/api)
- [Google Cloud Console](https://console.cloud.google.com)
