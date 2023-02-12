import socket
from datetime import datetime, timedelta, timezone

import jwt


class JWTAuth:
    encoder = jwt.encode

    def __init__(self, secret: str):
        self.secret = secret

    def issue_token(self, client: str) -> str:
        return self.encoder(self.get_claims(client), self.secret, algorithm="HS256")

    @staticmethod
    def get_claims(client: str, ttl_hours=24) -> dict:
        return {
            "Audience": "localhost",
            "ExpiresAt": datetime.now(tz=timezone.utc) + timedelta(hours=ttl_hours),
            "Id": client,
            "IssuedAt": datetime.now(tz=timezone.utc),
            "Issuer": f"MargayPythonSDK-{socket.gethostname()}",
            "Subject": "client",
        }
