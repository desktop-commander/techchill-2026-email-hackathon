# test_manual.py
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Add solution folder to path if needed
import sys
sys.path.insert(0, ".")

from server import _dispatch

async def main():
    # Test connection
    result = await _dispatch("test_connection", {})
    print("Connection:", result)

    # List mailboxes
    result = await _dispatch("list_mailboxes", {})
    print("Mailboxes:", result)

    # Classify inbox (last 5 emails)
    result = await _dispatch("classify_inbox", {"limit": 5})
    import json
    print(json.dumps(result, indent=2))

asyncio.run(main())
