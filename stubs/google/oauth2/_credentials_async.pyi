from _typeshed import Incomplete
from typing import Any, Mapping

from google.oauth2 import credentials as oauth2_credentials

class Credentials(oauth2_credentials.Credentials):
    token: Incomplete
    expiry: Incomplete
    async def refresh(self, request: Any) -> None: ...
    async def before_request(self, request: Any, method: str, url: str, headers: Mapping[str, str]) -> None: ...

class UserAccessTokenCredentials(oauth2_credentials.UserAccessTokenCredentials):
    pass
