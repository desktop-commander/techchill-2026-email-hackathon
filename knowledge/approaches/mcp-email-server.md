# MCP Email Server (zerolib-email)

> MCP server that gives AI assistants direct email access via IMAP/SMTP. Works with Gmail, Outlook, and any IMAP provider. Read, filter, send, reply — all through Claude Desktop or any MCP-compatible agent.

## What It Is

[mcp-email-server](https://github.com/ai-zerolab/mcp-email-server) is an open-source MCP server written in Python that lets AI assistants read, search, and send emails through standard IMAP and SMTP protocols. It's distributed via PyPI and launched using `uvx` (Astral UV package runner).

**Repo:** https://github.com/ai-zerolab/mcp-email-server

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  AI Agent (Claude Desktop, Cursor, etc.)             │
│  Sends structured MCP tool calls                     │
└──────────────┬───────────────────────────────────────┘
               │ MCP protocol (stdio)
               ▼
┌──────────────────────────────────────────────────────┐
│  mcp-email-server (local Python process)             │
│  - Translates MCP calls → IMAP/SMTP commands         │
│  - Manages connections to mail servers                │
│  - Returns structured data back to agent             │
│  - Credentials stored in local config (plaintext)    │
└──────────────┬───────────────────────────────────────┘
               │ IMAP (read) / SMTP (send) over TLS
               ▼
┌──────────────────────────────────────────────────────┐
│  Email Servers                                       │
│  Gmail · Outlook/M365 · Any IMAP/SMTP provider      │
└──────────────────────────────────────────────────────┘
```

**The key things to understand:**

1. **It's a native MCP server** — unlike the Google Workspace CLI (which is a CLI you call via shell), this speaks the MCP protocol directly. Claude Desktop talks to it natively, no shell wrapper needed.
2. **Uses IMAP/SMTP, not vendor APIs** — it connects to any email provider that supports IMAP (reading) and SMTP (sending). This means Gmail, Outlook, Yahoo, self-hosted — anything with standard email protocols.
3. **Runs locally** — the server is a local Python process on your machine. No cloud service, no data routed through third parties. Your credentials and email data stay on your machine.
4. **Config lives in Claude Desktop's config file** — credentials are stored as environment variables in the MCP server config JSON. Claude Desktop launches the server process on startup.
5. **Metadata-first design** — you can list subjects and senders without loading full email bodies, then fetch specific emails when needed. This is smart for large inboxes.

**How an AI agent uses it:**
- Claude sees the MCP tools: `list_emails_metadata`, `get_emails_content`, `send_email`, `download_attachment`, etc.
- User says: "Show me unread emails from today"
- Claude calls `list_emails_metadata` with filters → gets list of subjects, senders, dates
- User says: "Read the one from Sarah"
- Claude calls `get_emails_content` with that email's ID → gets full body
- User says: "Reply saying I'll be there at 3pm"
- Claude calls `send_email` with proper threading headers → reply shows up correctly in conversation view

**For hackathon builders:** This is the fastest path to "AI reads my email" — it's already an MCP server, so you can use it as-is or fork it to add new capabilities. You could wrap it in a higher-level agent that does triage, auto-categorization, or smart replies. Or extend the server itself with new tools.

## Capabilities

- Read emails with filtering by sender, subject, date, read/unread status, flagged status
- View full email content and metadata (threading, recipients, attachments list)
- Send emails with proper threading and reply headers
- Download attachments (opt-in, disabled by default)
- Paginated browsing through large inboxes (tested against 5,000+ emails)
- Multi-account support — configure multiple email accounts and switch between them
- Works with Gmail (via App Passwords), Outlook/Microsoft 365, and any custom IMAP/SMTP server
- Supports self-signed certificates for private mail servers
- Proper email threading — replies show up correctly in conversation view
- Credentials are masked in the list-accounts API response

## Limitations

- **No OAuth flow** — Gmail requires generating an App Password manually (need 2FA enabled). No browser-based "Sign in with Google."
- **No granular permissions** — once connected, the agent has full read and send access. You can't restrict to read-only or specific folders.
- **No full-text search** — filtering is by field (sender, subject, date), not full-text across email bodies. You'd have to fetch emails and scan through them.
- **Plaintext credential storage** — your App Password sits in a JSON config file with no encryption.
- **Auto-update risk** — the recommended config uses `@latest`, pulling newest version on every restart. Pin to a specific version (e.g., `@0.6.2`) for safety.
- **Prompt injection surface** — incoming emails become AI input. Malicious emails could contain hidden instructions. Known risk across all MCP tools processing untrusted data.

## Getting Started

**Prerequisites:** macOS or Linux, Python 3.10+, `uv` installed (`brew install uv` on macOS).

### Step 1: Generate a Gmail App Password

Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords), create a new app password, copy the 16-character code. You need 2FA enabled for this option to appear.

### Step 2: Add to Claude Desktop config

Open `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) and add:

```json
{
  "mcpServers": {
    "zerolib-email": {
      "command": "uvx",
      "args": ["mcp-email-server@0.6.2", "stdio"],
      "env": {
        "MCP_EMAIL_SERVER_ACCOUNT_NAME": "gmail",
        "MCP_EMAIL_SERVER_EMAIL_ADDRESS": "you@gmail.com",
        "MCP_EMAIL_SERVER_USER_NAME": "you@gmail.com",
        "MCP_EMAIL_SERVER_PASSWORD": "your-app-password",
        "MCP_EMAIL_SERVER_IMAP_HOST": "imap.gmail.com",
        "MCP_EMAIL_SERVER_IMAP_PORT": "993",
        "MCP_EMAIL_SERVER_SMTP_HOST": "smtp.gmail.com",
        "MCP_EMAIL_SERVER_SMTP_PORT": "465"
      }
    }
  }
}
```

> **Important:** Pin the version (`@0.6.2`) instead of using `@latest`. A compromised future release could silently change behavior.

### Step 3: Restart Claude Desktop

Fully quit and reopen (not just close the window).

### Step 4: Test it

Ask Claude: "List my latest 5 emails" and verify it connects.

## Security Notes

- **Local-only architecture** — no data sent to developer's servers. Codebase is public Python, 200+ GitHub stars, actively maintained.
- **Plaintext credentials** — your password lives in a JSON file on disk. Use a dedicated email account, not your primary one.
- **Prompt injection risk** — emails become AI input. Malicious emails could try to manipulate the agent.
- **MCP ecosystem maturity** — in September 2025, a different MCP email server (Postmark MCP) was caught silently BCC'ing outgoing emails to an attacker. This project shows no signs of similar behavior, but it's a reminder to review what you install.
- **Our recommendations:** Use a dedicated email account, pin the version, keep attachment downloads disabled, periodically review releases.

## Our Assessment

**Setup: ~20 minutes.** Requires generating Gmail App Password, installing `uv`, hand-editing JSON config, restarting Claude Desktop. You need to be comfortable with terminal and config files.

**Functionality: Strong.** Reading, filtering, sending with proper threading — all worked on first try. Metadata-first design is smart for large inboxes. Test email sent and delivered within seconds.

**Security: Needs caution.** Local-only is good, but plaintext credentials and no OAuth are gaps. Follow the recommendations above.

**Best for hackathon teams who:** want the fastest path to "AI reads my email" without building from scratch, plan to use Claude Desktop or another MCP-compatible agent, and want multi-provider support (Gmail + Outlook) out of the box.

## Links

- [Repository](https://github.com/ai-zerolab/mcp-email-server)
- [PyPI](https://pypi.org/project/mcp-email-server/)
- [Gmail App Passwords](https://myaccount.google.com/apppasswords)
- [MCP Protocol](https://modelcontextprotocol.io)
