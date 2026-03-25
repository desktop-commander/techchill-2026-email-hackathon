# Resend

> The cleanest API for sending transactional emails from code. If your project is about *sending* emails — outreach, notifications, automated replies — Resend gets you from zero to working in under 10 minutes.

## What It Is

[Resend](https://resend.com) is a developer-focused email sending API. It handles outbound email delivery (SMTP infrastructure, DKIM signing, deliverability) so you don't have to. You call their API or SDK, pass a message, and Resend delivers it.

There's an official **agent skill** for Resend on skills.sh that teaches your AI agent how to send emails correctly — including proper retry logic, idempotency, and handling bounces.

**skills.sh (sending):** https://skills.sh/resend/resend-skills/send-email  
**skills.sh (deliverability):** https://skills.sh/resend/email-best-practices/email-best-practices  
**Docs:** https://resend.com/docs  
**Dashboard:** https://resend.com

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  Your AI Agent / Application                         │
│  Calls Resend SDK or REST API                        │
└──────────────┬───────────────────────────────────────┘
               │ HTTPS API calls
               ▼
┌──────────────────────────────────────────────────────┐
│  Resend API (cloud)                                  │
│  - Accepts email send requests                       │
│  - Handles DKIM signing, SPF, DMARC                  │
│  - Manages delivery, retries, bounces                │
│  - Fires webhooks on delivery events                 │
└──────────────┬───────────────────────────────────────┘
               │ SMTP delivery
               ▼
┌──────────────────────────────────────────────────────┐
│  Recipients' inboxes                                 │
│  Gmail, Outlook, or any email provider               │
└──────────────────────────────────────────────────────┘
```

**Key things to understand:**

1. **Sending only** — Resend sends emails. It does not read, receive, or manage inboxes. If you need to read replies, pair it with another approach.
2. **API key, no OAuth** — sign up, verify a sending domain (or use their sandbox for testing), get an API key. Done.
3. **SDK available in every language** — Node.js, Python, Ruby, PHP, Go, Rust, Elixir, Java. Pick yours.
4. **Built for developers** — clean API, good error messages, webhooks for delivery events (delivered, bounced, complained, opened, clicked).
5. **Free tier** — 3,000 emails/month, 1 domain. More than enough for a hackathon.

**What "verified sending domain" means:** To send from `you@yourdomain.com`, you need to add DNS records (DKIM, SPF) to your domain. Resend gives you the records and guides you through it. Without a custom domain, you can still test-send using Resend's sandbox (`onboarding@resend.dev → your@email.com`).

## Capabilities

- **Send single emails** — to, from, subject, plain text, HTML
- **Send to multiple recipients** — to, cc, bcc
- **HTML email templates** — React Email component library, or raw HTML
- **Attachments** — base64 or path-based
- **Reply-to headers** — route replies to a different address
- **Tags** — attach metadata to emails for tracking
- **Scheduled sending** — send at a future time
- **Batch sending** — send up to 100 emails in a single API call
- **Idempotency keys** — safe to retry without duplicate sends
- **Webhooks** — delivery, bounce, complaint, open, click events
- **Domain management** — add and verify multiple sending domains
- **Email logs** — full send history in dashboard

## Limitations

- **Sending only** — cannot read, receive, or parse incoming emails. If your use case involves replies, you need a separate receiving solution (AgentMail handles both send and receive).
- **Requires verified domain for production** — testing works without a domain, but sending to arbitrary recipients requires DNS verification. Budget ~15 minutes for DNS setup.
- **DNS propagation** — after adding DNS records, it can take minutes to hours to propagate before Resend confirms verification.
- **No IMAP/SMTP passthrough** — this is an API service, not a mail server. You can't point Himalaya or an IMAP client at it.
- **Volume limits on free tier** — 3,000 emails/month, 100 emails/day. Enough for a hackathon, but check limits if you're building something viral.

## Getting Started

### Step 1: Create an account

Go to [resend.com](https://resend.com), sign up, and generate an API key from the dashboard.

### Step 2: Install the SDK

```bash
# Node.js
npm install resend

# Python
pip install resend
```

### Step 3: Send your first email

**TypeScript/Node.js:**
```typescript
import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

const { data, error } = await resend.emails.send({
  from: 'onboarding@resend.dev',       // sandbox address — works without domain setup
  to: ['you@youremail.com'],
  subject: 'Hello from my agent',
  html: '<p>This email was sent by an AI agent.</p>',
  text: 'This email was sent by an AI agent.',
});

if (error) {
  console.error('Send failed:', error);
} else {
  console.log('Sent! ID:', data.id);
}
```

**Python:**
```python
import resend
import os

resend.api_key = os.environ["RESEND_API_KEY"]

params = {
  "from": "onboarding@resend.dev",
  "to": ["you@youremail.com"],
  "subject": "Hello from my agent",
  "html": "<p>This email was sent by an AI agent.</p>",
  "text": "This email was sent by an AI agent.",
}

email = resend.Emails.send(params)
print(email)
```

### Step 4: Install the agent skills (optional but recommended)

```bash
# Core sending skill — teaches your agent how to use the Resend SDK correctly
npx skills add resend/resend-skills --skill send-email

# Deliverability skill — teaches your agent about SPF/DKIM/DMARC, spam, compliance
npx skills add resend/email-best-practices --skill email-best-practices
```

## Install the Skills

```bash
npx skills add resend/resend-skills --skill send-email
npx skills add resend/email-best-practices --skill email-best-practices
```

## Our Assessment

**Setup: ~5 minutes** to first sent email (using sandbox). ~20 minutes if you add a custom domain with DNS verification.

**Best for:** Projects focused on outbound email — cold outreach drafters, notification senders, automated reply generators, digest senders, anything where the agent composes and sends emails as its core action.

**Pair with:**
- **AgentMail** — if you also need to receive and process replies (AgentMail handles both sides, but Resend has better deliverability for high-volume sending)
- **MCP Email Server or Himalaya** — if you need to read an existing inbox *and* send from it (those handle both IMAP reading and SMTP sending together)

**Not the right choice if** you need to read or manage an existing inbox. Resend is purely a sending API.

## Links

- [Resend docs](https://resend.com/docs)
- [Resend dashboard](https://resend.com)
- [send-email skill](https://skills.sh/resend/resend-skills/send-email)
- [email-best-practices skill](https://skills.sh/resend/email-best-practices/email-best-practices)
- [React Email](https://react.email) — companion library for building HTML email templates as React components
