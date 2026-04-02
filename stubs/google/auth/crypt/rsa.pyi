from google.auth.crypt import base
from typing import Union, Any

from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

RSA_KEY_MODULE_PREFIX: str

class RSAVerifier(base.Verifier):
    def __init__(self, public_key: Union["rsa.key.PublicKey", RSAPublicKey]) -> None:
        ...
    def verify(self, message: bytes, signature: bytes) -> bool:
        ...
    @classmethod
    def from_string(cls, public_key: str | bytes) -> RSAVerifier:
        ...

class RSASigner(base.Signer, base.FromServiceAccountMixin):
    def __init__(self, private_key: Union["rsa.key.PrivateKey", RSAPrivateKey], key_id: str | None = None) -> None:
        ...
    @property
    def key_id(self) -> str | None:
        ...
    def sign(self, message: bytes) -> bytes:
        ...
    @classmethod
    def from_string(cls, key: str | bytes, key_id: str | None = None) -> RSASigner:
        ...