from typing import Any, Mapping, Optional, Sequence, Union

from google.auth import crypt
from google.auth import exceptions

def from_dict(data: Mapping[str, str], require: Optional[Sequence[str]] = None, use_rsa_signer: bool = True) -> crypt.Signer: ...
def from_filename(filename: str, require: Optional[Sequence[str]] = None, use_rsa_signer: bool = True) -> tuple[Mapping[str, str], crypt.Signer]: ...
