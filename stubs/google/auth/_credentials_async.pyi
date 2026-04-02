import abc
from google.auth import credentials
from typing import Any, Mapping, Sequence

class Credentials(credentials.Credentials, metaclass=abc.ABCMeta):
    async def before_request(self, request: Any, method: str, url: str, headers: Mapping[str, str]) -> None: ...

class CredentialsWithQuotaProject(credentials.CredentialsWithQuotaProject):
    def with_quota_project(self, quota_project_id: str) -> 'CredentialsWithQuotaProject': ...

class AnonymousCredentials(credentials.AnonymousCredentials, Credentials):
    pass

class ReadOnlyScoped(credentials.ReadOnlyScoped, metaclass=abc.ABCMeta):
    pass

class Scoped(credentials.Scoped):
    def with_scopes(self, scopes: Sequence[str], default_scopes: Sequence[str] | None = None) -> 'Scoped': ...

def with_scopes_if_required(credentials: Credentials, scopes: Sequence[str]) -> Credentials: ...

class Signing(credentials.Signing, metaclass=abc.ABCMeta):
    pass