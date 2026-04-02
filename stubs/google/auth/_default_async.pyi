import google.auth.transport
from typing import Any, Optional, Sequence, Tuple

from google.auth.credentials import Credentials

def load_credentials_from_file(filename: str, scopes: Optional[Sequence[str]] = None, default_scopes: Optional[Sequence[str]] = None, quota_project_id: Optional[str] = None, request: Optional[google.auth.transport.Request] = None) -> Tuple[Credentials, Optional[str]]: ...
def default_async(scopes: Optional[Sequence[str]] = None, request: Optional[google.auth.transport.Request] = None, quota_project_id: Optional[str] = None) -> Tuple[Credentials, Optional[str]]: ...