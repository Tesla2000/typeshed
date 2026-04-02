import abc
from _typeshed import Incomplete

class _BaseAuthorizedSession(metaclass=abc.ABCMeta):
    credentials: Incomplete
    def __init__(self, credentials) -> None: ...
    @abc.abstractmethod
    def request(self, method: str, url: str, data: bytes | None = None, headers: dict[str, str] | None = None, max_allowed_time: int | None = None, timeout: int | None = 120, **kwargs) -> Incomplete: ...
    @abc.abstractmethod
    def close(self) -> None: ...