import abc
from _typeshed import Incomplete

DEFAULT_RETRYABLE_STATUS_CODES: tuple[int, ...]
DEFAULT_REFRESH_STATUS_CODES: tuple[int, ...]
DEFAULT_MAX_REFRESH_ATTEMPTS: int

class Response(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def status(self) -> int: ...
    @property
    @abc.abstractmethod
    def headers(self) -> dict[str, str]: ...
    @property
    @abc.abstractmethod
    def data(self) -> bytes: ...

class Request(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, url: str, method: str = 'GET', body: bytes | None = None, headers: dict[str, str] | None = None, timeout: int | None = None, **kwargs) -> Response: ...
