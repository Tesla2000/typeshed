import enum
from _typeshed import Incomplete
from dataclasses import dataclass, field
from pathlib import Path
from requests.adapters import HTTPAdapter


def _get_mds_root_crt_path() -> Path: ...
def _get_mds_client_combined_cert_path() -> Path: ...

@dataclass
class MdsMtlsConfig:
    ca_cert_path: Path = field(default_factory=_get_mds_root_crt_path)
    client_combined_cert_path: Path = field(default_factory=_get_mds_client_combined_cert_path)

class MdsMtlsMode(enum.Enum):
    STRICT = 'strict'
    NONE = 'none'
    DEFAULT = 'default'

def should_use_mds_mtls(mds_mtls_config: MdsMtlsConfig = MdsMtlsConfig()) -> bool: ...

class MdsMtlsAdapter(HTTPAdapter):
    ssl_context: Incomplete
    def __init__(self, mds_mtls_config: MdsMtlsConfig = MdsMtlsConfig(), *args, **kwargs) -> None: ...
    def init_poolmanager(self, *args, **kwargs) -> None: ...
    def proxy_manager_for(self, *args, **kwargs) -> None: ...
    def send(self, request: Incomplete, **kwargs) -> Incomplete: ...
