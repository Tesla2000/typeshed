from typing import Any

from google.auth import credentials
from google.auth import crypt

IAM_RETRY_CODES: set[int]

class Signer(crypt.Signer):
    def __init__(self, request: Any, credentials: credentials.Credentials, service_account_email: str) -> None: ...
    @property
    def key_id(self) -> None: ...
    def sign(self, message: bytes) -> bytes: ...