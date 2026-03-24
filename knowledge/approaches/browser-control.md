# Browser Control (Claude in Chrome)

> Control any webmail UI directly through Chrome — no APIs, no credentials, no config. Claude reads the page and clicks buttons like a human would. Works with any email provider.

## What It Is

Claude in Chrome is a browser extension that lets Claude read and interact with any web page open in Chrome — including your email. Instead of connecting through IMAP or a vendor API, Claude operates your email the way a person would: looking at what's on screen, clicking buttons, typing in search bars, reading results.

**Extension:** Available via Claude Desktop settings under Computer Use

## How It Works (Architecture)

```
┌──────────────────────────────────────────────────────┐
│  Claude (Claude Desktop / Cowork)                    │
│  Reads accessibility tree, sends interaction commands │
└──────────────┬───────────────────────────────────────┘
               │ Chrome extension protocol
               ▼
┌──────────────────────────────────────────────────────┐
│  Claude in Chrome extension                          │
│  - Exposes page accessibility tree (DOM structure)   │
│  - Each element tagged with a reference ID           │
│  - Can click, type, execute JS on the page           │
└──────────────┬───────────────────────────────────────┘
               │ Reads/interacts with the live page
               ▼
┌──────────────────────────────────────────────────────┐
│  Any webmail UI in Chrome                            │
│  Gmail · Outlook · Yahoo · ProtonMail · Hey ·        │
│  Fastmail · corporate portals · anything in Chrome   │
└──────────────────────────────────────────────────────┘
```

**The key things to understand:**

1. **No email protocol involved** — this doesn't use IMAP, SMTP, or any API. It literally reads what's visible on screen in Chrome and clicks UI elements.
2. **Accessibility tree, not screenshots** — Claude doesn't "see" the page visually. It reads a structured tree of elements (headings, rows, buttons, links), each tagged with a reference ID. It parses this tree to find senders, subjects, dates, etc.
3. **No credentials needed** — if you're logged into your email in Chrome, Claude can see it. Your browser session handles all authentication.
4. **Provider-agnostic** — works with Gmail, Outlook, Yahoo, ProtonMail, Hey, Fastmail, corporate webmail, anything that loads in Chrome.
5. **Maintained by Anthropic** — the extension is first-party, not a third-party MCP server from GitHub.

**How an AI agent uses it:**
- User opens Gmail in Chrome, connects Claude in Chrome extension
- User says: "Show me my inbox"
- Claude reads the page's accessibility tree → parses inbox rows → extracts sender, subject, date, preview
- User says: "Open the email from Sarah"
- Claude clicks the email row by reference ID → reads the full email content from the new page
- User says: "Search for emails about the invoice"
- Claude clicks the search bar, types the query, reads results (this part is unreliable — see Limitations)

**For hackathon builders:** Browser control is a viable approach if you want to build something that works across ALL email providers without any configuration. The tradeoff is speed and reliability. Best used for simple read-only tasks, or as a fallback when no API/MCP option exists for a provider.

## Capabilities

- View inbox contents — sender, subject, date, preview text
- Navigate between email views (inbox, sent, folders)
- Open individual emails to read full content
- Use the search bar to find emails (unreliable — see Limitations)
- Click through pages of results
- Execute JavaScript on the page for targeted data extraction
- **Works with any webmail provider** — Gmail, Outlook, Yahoo, ProtonMail, Hey, Fastmail, corporate portals, custom webmail

## Limitations

- **Slow.** Every interaction requires reading the DOM, which can be thousands of elements. Gmail's inbox tree exceeded 50,000 characters in our testing and needed retries with reduced depth. Near-instant IMAP responses this is not.
- **Prone to errors.** Webmail UIs are complex, JS-heavy apps not designed for programmatic access. Gmail's search didn't respond to URL navigation, form input alone didn't trigger search, JS execution fallback still didn't fully work. Each step is a new failure point.
- **Not suited for bulk operations.** You only see what's on screen. Analyzing many emails means scrolling, clicking "next page," re-reading DOM each time. No way to say "give me 100 emails from this sender" in one call.
- **Searching is unreliable.** We tried three methods to search Gmail — URL hash navigation, form input with button click, JS-triggered navigation — none filtered correctly on first attempt.
- **Sending is fragile.** Composing by clicking "Compose," filling fields, hitting "Send" is brittle. One UI change, one unexpected modal, one missed click breaks the flow.
- **Extension can disconnect.** Initial connection failed in our testing, required manual reconnection. Mid-task disconnection means lost progress.
- **Page size limits.** Gmail's DOM is massive. First attempt exceeded 50K character output limit. Required reducing tree depth, targeting specific elements, and using JS extraction.

## Getting Started

The simplest setup of any approach — no credentials, no config files, no terminal.

1. **Install the extension** — enable Claude in Chrome via Claude Desktop settings under Computer Use, or install from Chrome Web Store.
2. **Connect** — open Claude Desktop (or Cowork) and ensure the extension shows as connected. Reconnect if needed.
3. **Open your email** — navigate to your webmail in Chrome and log in normally.
4. **Ask Claude** — "Read my inbox" and Claude will parse the page contents.

That's it. No GCP projects, no App Passwords, no JSON config files.

## Security Notes

- **No stored credentials** — Claude never sees your password. It uses your existing browser session.
- **First-party extension** — maintained by Anthropic, not a third-party GitHub repo.
- **Session-scoped** — access only exists while the extension is connected and the email tab is open. Close the tab = access gone.
- **Full visual access** — Claude sees everything on the page, including sensitive content. No way to limit to "metadata only."
- **Prompt injection risk** — malicious emails in the DOM could embed hidden instructions. HTML-based prompts may be more effective than plain-text IMAP content.
- **Browser session scope** — Claude could theoretically navigate to other Google services (Drive, Calendar) using your session. The access scope is broader than just email.

## Our Assessment

**Setup: 9/10.** Install extension, log into email, done. As close to zero-friction as it gets.

**Functionality: 5/10.** Reading the inbox works, but everything beyond that is a struggle. Searching was unreliable across multiple attempts. Doesn't scale beyond a handful of emails.

**Reliability: 4/10.** Too many moving parts. Extension disconnections, DOM size limits, unpredictable JS UI responses, inconsistent search behavior.

**Speed: 3/10.** Noticeably slower than MCP/CLI for every operation. Multiple tool calls and retries just to read the inbox.

**Best for hackathon teams who:** want to build something that works across ALL email providers without any setup, are okay with read-only or light interaction, or want to combine browser control with another approach as a fallback for providers that don't support IMAP.

**Not recommended for:** bulk operations, sending emails, anything requiring reliability or speed, or submissions that need to demonstrate "working demo" quality under time pressure.

**The honest take:** Use a dedicated MCP server or CLI for your core functionality. Use browser control only if you specifically need the "any provider" angle, or as a cool demo of multi-provider support alongside a more reliable primary approach.

## Links

- [Claude in Chrome](https://claude.ai) — available via Claude Desktop settings under Computer Use
- [MCP Protocol](https://modelcontextprotocol.io)
