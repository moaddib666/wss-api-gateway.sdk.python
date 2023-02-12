import os

from margay.sdk.auth import JWTAuth
from margay.sdk.client import Client

if __name__ == "__main__":
    token = input("Auth token:")
    if not token:
        app_secret = os.getenv("MARGAY_AUTH_SECRET", "SuperSecret")
        token = JWTAuth(app_secret).issue_token("JohnSnow")
    client = Client("ws://127.0.0.1:8080", token)
    client.run()
