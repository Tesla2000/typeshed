from _typeshed import Incomplete
from datetime import datetime
from typing import Any, Mapping

from google.auth import credentials

TOKEN_EXCHANGE_TYPE: str
ACCESS_TOKEN_TOKEN_TYPE: str
SERVICE_ACCOUNT_TOKEN_TYPE: str
JWT_LIFETIME: datetime.timedelta

class ServiceAccountCredentials(credentials.Credentials):
    def __init__(self, signer: Any, service_identity_name: str, project: str, audience: str, token_uri: str, ca_cert_path: str | None) -> None: ...
    def refresh(self, request: Any) -> None: ...
    def with_gdch_audience(self, audience: str) -> 'ServiceAccountCredentials': ...
    @classmethod
    def from_service_account_info(cls, info: Mapping[str, Any]) -> 'ServiceAccountCredentials': ...
    @classmethod
    def from_service_account_file(cls, filename: str) -> 'ServiceAccountCredentials': ...
