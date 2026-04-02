from typing import Any, Union

from google.auth.crypt.base import Signer, Verifier
from google.auth.crypt.es import EsSigner, EsVerifier
from google.auth.crypt.es256 import ES256Signer, ES256Verifier
from google.auth.crypt.rsa import RSASigner, RSAVerifier


__all__ = [
    "EsSigner",
    "EsVerifier",
    "ES256Signer",
    "ES256Verifier",
    "RSASigner",
    "RSAVerifier",
    "Signer",
    "Verifier",
]

EsSigner: type[EsSigner]
EsVerifier: type[EsVerifier]
ES256Signer: type[ES256Signer]
ES256Verifier: type[ES256Verifier]
Signer: type[Signer]
Verifier: type[Verifier]
RSASigner: type[RSASigner]
RSAVerifier: type[RSAVerifier]
