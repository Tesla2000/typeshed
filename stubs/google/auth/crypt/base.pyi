import abc
from typing import Any, Mapping, Optional, Union

class Verifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def verify(self, message: Union[str, bytes], signature: Union[str, bytes]) -> bool: ...

class Signer(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def key_id(self) -> str | None: ...
    @abc.abstractmethod
    def sign(self, message: Union[str, bytes]) -> bytes: ...

class FromServiceAccountMixin(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def from_string(cls, key: str, key_id: str | None = None) -> 'Signer': ...
    @classmethod
    def from_service_account_info(cls, info: Mapping[str, str]) -> 'Signer': ...
    @classmethod
    def from_service_account_file(cls, filename: str) -> 'Signer': ...
