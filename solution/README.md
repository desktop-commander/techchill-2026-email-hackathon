`# Email Classifier MCP

> AI-powered email importance classifier that works directly in your real inbox.
> Built for the TechChill 2026 Hackathon — Desktop Commander Track.

Give Claude Desktop the ability to read your inbox, classify every email by importance, and tell you exactly what needs attention right now.

---

## What It Does

This MCP server connects to your real Gmail or Outlook inbox via IMAP and gives Claude a set of email intelligence tools:

| Tool | What it does |
|------|-------------|
| `classify_inbox` | Fetch + classify recent emails, sorted by priority |
| `classify_single_email` | Deep-classify one email with full body analysis |
| `get_inbox_summary` | Natural-language briefing: what needs attention today |
| `list_mailboxes` | List all folders in your account |
| `fetch_email_content` | Read a specific email's full content |
| `mark_email_seen` | Mark email as read |
| `mark_email_flagged` | Star/flag an email for follow-up |
| `test_connection` | Verify IMAP credentials work |

### Classification labels

| Label | Meaning |
|-------|---------|
| 🔴 URGENT | Immediate attention needed — deadlines, emergencies, requests from real people |
| 🟠 IMPORTANT | Read today — meaningful messages that deserve a response |
| 🟡 NORMAL | Standard correspondence, no rush |
| 🔵 LOW | FYI only, no action needed |
| 📰 NEWSLETTER | Marketing, subscriptions, digests |
| 🗑️ SPAM | Unsolicited, suspicious, or phishing |

---

## Setup

### Prerequisites

- Python 3.10 or higher
- `uv` package manager: `brew install uv` (macOS) or `pip install uv`
- Claude Desktop
- Gmail or Outlook account

### Step 1 — Get an App Password (Gmail)

1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Sign in, create a new App Password (name it "Email Classifier MCP")
3. Copy the 16-character code — this is your `EMAIL_PASSWORD`

> **Gmail requires 2FA to be enabled** for App Passwords to appear.
>
> **Outlook users:** Use your regular password. No App Password needed.

### Step 2 — Configure credentials

```bash
cp .env.example .env
```

Edit `.env` and fill in:
```
ANTHROPIC_API_KEY=sk-ant-...
EMAIL_USER=you@gmail.com
EMAIL_PASSWORD=abcd efgh ijkl mnop   # your 16-char Gmail App Password
EMAIL_IMAP_HOST=imap.gmail.com
EMAIL_IMAP_PORT=993
EMAIL_USE_SSL=true
```

### Step 3 — Install dependencies

```bash
cd /path/to/email-classifier-mcp
uv venv
uv pip install -r requirements.txt
```

### Step 4 — Add to Claude Desktop

Open `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)
or `%APPDATA%\Claude\claude_desktop_config.json` (Windows) and add:

```json
{
  "mcpServers": {
    "email-classifier": {
      "command": "uv",
      "args": [
        "--directory", "/ABSOLUTE/PATH/TO/email-classifier-mcp",
        "run", "python", "src/server.py"
      ],
      "env": {
        "ANTHROPIC_API_KEY": "your_key_here",
        "EMAIL_USER": "you@gmail.com",
        "EMAIL_PASSWORD": "your_app_password",
        "EMAIL_IMAP_HOST": "imap.gmail.com",
        "EMAIL_IMAP_PORT": "993",
        "EMAIL_USE_SSL": "true"
      }
    }
  }
}
```

> Replace `/ABSOLUTE/PATH/TO/email-classifier-mcp` with the actual full path on your machine.

### Step 5 — Restart Claude Desktop

Fully quit Claude Desktop (Cmd+Q on macOS) and reopen it.

---

## Usage

Once connected, just talk to Claude naturally:

```
"Classify my inbox"
"What emails need my attention today?"
"Give me an inbox summary"
"Show me my unread emails sorted by priority"
"Classify email UID 12345"
"Flag the email from Sarah as important"
```

### Example output from `classify_inbox`

```json
[
  {
    "uid": "4821",
    "subject": "Contract needs your signature by EOD",
    "from": "legal@company.com",
    "label": "URGENT",
    "label_emoji": "🔴",
    "confidence": 95,
    "reasoning": "Legal contract with explicit end-of-day deadline requiring action.",
    "suggested_action": "Sign and reply today",
    "key_points": ["EOD deadline", "Contract signature required"]
  },
  {
    "uid": "4820",
    "subject": "Your weekly newsletter",
    "from": "noreply@substack.com",
    "label": "NEWSLETTER",
    "label_emoji": "📰",
    "confidence": 99,
    "reasoning": "Automated newsletter from a subscription service.",
    "suggested_action": "Read at leisure or unsubscribe",
    "key_points": ["Subscription newsletter", "No action required"]
  }
]
```

---

## Outlook / Microsoft 365

Replace the IMAP settings in your config:

```json
"EMAIL_IMAP_HOST": "outlook.office365.com",
"EMAIL_IMAP_PORT": "993",
"EMAIL_PASSWORD": "your_regular_outlook_password"
```

---

## Architecture

```
Claude Desktop
     │  MCP protocol (stdio)
     ▼
server.py  ←─── 8 MCP tools
     │
     ├── email_client.py  ←── IMAP connection to your real inbox
     │        │
     │        └── imaplib (standard library) → Gmail / Outlook
     │
     └── classifier.py   ←── Anthropic API (claude-sonnet-4-6)
              │
              └── 6-label classification + inbox summary
```

Everything runs **locally on your machine**. Email data never leaves your computer except for the snippet sent to the Anthropic API for classification.

---

## Security Notes

- Your email password is stored in the Claude Desktop config file or `.env` — both are local only
- Only email subject, sender, date, and a short snippet (≤400 chars) are sent to the Anthropic API
- Full email bodies are never sent externally
- Consider using a dedicated email account for testing rather than your primary inbox

---

## Project Structure

```
email-classifier-mcp/
├── src/
│   ├── server.py         # MCP server — all tool definitions and handlers
│   ├── email_client.py   # IMAP client — connects to the real inbox
│   └── classifier.py     # AI classifier — Anthropic API integration
├── requirements.txt
├── .env.example
└── README.md
```

---

*Built at TechChill 2026 Hackathon · Desktop Commander × BADideas.fund track*
