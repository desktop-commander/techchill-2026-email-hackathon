# AgentMail

> API-first email platform built specifically for AI agents. Give your agent its own inbox — no OAuth, no IMAP config, just an API key and a dedicated email address.

## What It Is

[AgentMail](https://agentmail.to) is a managed email platform designed for AI agents. Instead of connecting to your personal Gmail or Outlook, you create fresh, programmable inboxes via API. Your agent gets its own email identity (e.g. `support@yourdomain.agentmail.to`) and can send, receive, reply, and organise messages entirely through code.

**Docs:** https://docs.agentmail.to  
**Console:** https://console.agentmail.to  
**skills.sh:** https://skills.sh/agentmail-to/agentmail-skills/agentmail

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  Your AI Agent (Claude Code, Cursor, Codex, etc.)    │
│  Uses AgentMail SDK or REST API                      │
└──────────────┬───────────────────────────────────────┘
               │ HTTPS API calls (SDK or raw REST)
               ▼
┌──────────────────────────────────────────────────────┐
│  AgentMail Platform (cloud)                          │
│  - Manages inboxes (create, delete, list)            │
│  - Routes inbound mail to your inbox                 │
│  - Queues outbound mail                              │
│  - Fires webhooks on new messages                    │
│  - Semantic search, auto-labeling (AI-native)        │
└──────────────┬───────────────────────────────────────┘
               │ Real email delivery (SMTP/DKIM/SPF)
               ▼
┌──────────────────────────────────────────────────────┐
│  The actual internet email system                    │
│  Recipients get real emails, can reply back          │
└──────────────────────────────────────────────────────┘
```

**Key things to understand:**

1. **Agents get their own email identity** — this is NOT about reading your personal Gmail. AgentMail creates fresh inboxes your agent owns and controls programmatically.
2. **No OAuth complexity** — sign up, get an API key, start creating inboxes. No Google Cloud project, no App Passwords, no IMAP config.
3. **Cloud-hosted** — your email data lives on AgentMail's servers, not your local machine. The tradeoff: zero setup friction, but you're trusting a third party.
4. **Webhooks for real-time** — configure a webhook and your agent is notified the moment a reply arrives. No polling needed.
5. **AI-native features** — semantic search, automatic labeling, and structured data extraction are built in. Useful for things like "find all emails about invoices" without writing your own parser.

**How an AI agent would use it:**
- Agent receives task: "Handle incoming support requests"
- Agent calls `inboxes.create()` → gets `support@project.agentmail.to`
- User publishes that address on a website
- When someone emails it, AgentMail fires a webhook → agent wakes up
- Agent calls `messages.get()` → reads the email
- Agent calls `messages.reply()` → sends a response
- Agent calls `messages.update()` with labels → marks it handled

## Capabilities

- **Create/delete inboxes on demand** — auto-generated addresses or custom usernames
- **Send emails** — with plain text, HTML, labels
- **Reply to messages** — with proper threading (replies appear in the sender's thread)
- **List and read messages** — paginated, filterable
- **Label management** — add/remove labels for workflow state (e.g. `replied`, `escalated`)
- **Webhooks** — real-time notification on inbound messages
- **Semantic search** — AI-powered search across inbox content
- **Attachments** — Base64 encoded, handled via API
- **Draft creation** — create drafts for human-approval workflows
- **Multi-tenant isolation** — pods for SaaS platforms
- **Idempotent operations** — safe retries via `client_id`
- **SDKs** — TypeScript/Node.js and Python, identical API surface

## Limitations

- **Not your personal inbox** — this is for agent-owned addresses, not for reading your own Gmail or Outlook. Use the MCP Email Server or GWS CLI for that.
- **Cloud-hosted** — email data goes through AgentMail's servers. Not ideal for sensitive personal or enterprise email.
- **Real-time webhooks need a public server** — if you're running locally without a public URL, you'll need ngrok or similar. Alternatively, poll with `messages.list()` on a schedule.
- **Free tier limits** — 3 inboxes, 3,000 emails/month. Enough for a hackathon, but plan accordingly.
- **New platform** — docs and SDK are solid but the platform is young. Expect rough edges.
- **Deliverability depends on their infrastructure** — sending from `@agentmail.to` addresses may hit spam filters compared to established domains.

## Getting Started

### Step 1: Create an account

Go to [console.agentmail.to](https://console.agentmail.to), sign up, and generate an API key.

### Step 2: Install the SDK

```bash
# TypeScript/Node.js
npm install agentmail

# Python
pip install agentmail
```

### Step 3: Create an inbox and send your first email

**TypeScript:**
```typescript
import { AgentMailClient } from "agentmail";

const client = new AgentMailClient({ apiKey: process.env.AGENTMAIL_API_KEY });

// Create an inbox
const inbox = await client.inboxes.create({ username: "my-agent" });
console.log("Created:", inbox.inboxId); // my-agent@agentmail.to

// Send an email
await client.inboxes.messages.send({
  inboxId: inbox.inboxId,
  to: "someone@example.com",
  subject: "Hello from my agent",
  text: "This is a test email from my AI agent.",
  html: "<p>This is a test email from my AI agent.</p>",
});

// List received messages
const messages = await client.inboxes.messages.list({ inboxId: inbox.inboxId });
console.log("Messages:", messages);
```

**Python:**
```python
import os
from agentmail import AgentMail

client = AgentMail(api_key=os.getenv("AGENTMAIL_API_KEY"))

# Create an inbox
inbox = client.inboxes.create(username="my-agent")
print(f"Created: {inbox.inbox_id}")

# Send an email
client.inboxes.messages.send(
    inbox_id=inbox.inbox_id,
    to="someone@example.com",
    subject="Hello from my agent",
    text="This is a test email from my AI agent.",
)

# List received messages
messages = client.inboxes.messages.list(inbox_id=inbox.inbox_id)
print(messages)
```

### Step 4: Install the agent skill (optional but recommended)

```bash
npx skills add agentmail-to/agentmail-skills --skill agentmail
```

This gives your AI coding assistant (Claude Code, Cursor, Codex) built-in knowledge of the AgentMail API patterns, so it can help you write the integration code correctly.

## Install the Skill

```bash
npx skills add agentmail-to/agentmail-skills --skill agentmail
```

## Our Assessment

**Setup: ~5 minutes.** Fastest path to a working agent email address. No GCP project, no IMAP config, no App Password dance. Sign up → API key → create inbox → send email.

**Best for:** Projects where your AI agent needs its own email identity — customer support bots, outreach agents, automated notification senders, anything where the agent is a participant in email conversations rather than a reader of someone else's inbox.

**Not the right choice if** you need to read or process an existing Gmail/Outlook inbox. For that, see the [MCP Email Server](mcp-email-server.md) or [Google Workspace CLI](google-workspace-cli.md) approaches.

## Links

- [AgentMail docs](https://docs.agentmail.to)
- [Console / sign up](https://console.agentmail.to)
- [skills.sh skill](https://skills.sh/agentmail-to/agentmail-skills/agentmail)
- [GitHub](https://github.com/agentmail-to/agentmail-js)
