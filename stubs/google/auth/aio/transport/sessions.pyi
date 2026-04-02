import abc
import asyncio
from contextlib import asynccontextmanager
import functools
import time
from typing import Any, Callable, Mapping, Optional, TYPE_CHECKING, Union

from google.auth import _exponential_backoff, exceptions
from google.auth.aio import transport
from google.auth.aio.credentials import Credentials
from google.auth.aio.transport import mtls
from google.auth.exceptions import TimeoutError
import google.auth.transport._mtls_helper


if TYPE_CHECKING:
    import aiohttp
    from aiohttp import ClientTimeout

else:
    try:
        import aiohttp
        from aiohttp import ClientTimeout
    except (ImportError, AttributeError):
        ClientTimeout = None


try:
    from google.auth.aio.transport.aiohttp import Request as AiohttpRequest

    AIOHTTP_INSTALLED = True
except ImportError:
    AIOHTTP_INSTALLED = False


@asynccontextmanager
async def timeout_guard(timeout: float) -> Any:
    ...


class AsyncAuthorizedSession:
    def __init__(self, credentials: Credentials, auth_request: Optional[transport.Request] = None) -> None:
        ...
    async def configure_mtls_channel(self, client_cert_callback: Optional[Callable[[], tuple[bytes, bytes]]] = None) -> None:
        ...
    async def request(self, method: str, url: str, data: Optional[bytes] = None, headers: Optional[Mapping[str, str]] = None, max_allowed_time: float = ..., timeout: Union[float, ClientTimeout] = ..., total_attempts: Optional[int] = ..., **kwargs: Any) -> transport.Response:
        ...
    async def get(self, url: str, data: Optional[bytes] = None, headers: Optional[Mapping[str, str]] = None, max_allowed_time: float = ..., timeout: Union[float, ClientTimeout] = ..., total_attempts: Optional[int] = ..., **kwargs: Any) -> transport.Response:
        ...
    async def post(self, url: str, data: Optional[bytes] = None, headers: Optional[Mapping[str, str]] = None, max_allowed_time: float = ..., timeout: Union[float, ClientTimeout] = ..., total_attempts: Optional[int] = ..., **kwargs: Any) -> transport.Response:
        ...
    async def put(self, url: str, data: Optional[bytes] = None, headers: Optional[Mapping[str, str]] = None, max_allowed_time: float = ..., timeout: Union[float, ClientTimeout] = ..., total_attempts: Optional[int] = ..., **kwargs: Any) -> transport.Response:
        ...
    async def patch(self, url: str, data: Optional[bytes] = None, headers: Optional[Mapping[str, str]] = None, max_allowed_time: float = ..., timeout: Union[float, ClientTimeout] = ..., total_attempts: Optional[int] = ..., **kwargs: Any) -> transport.Response:
        ...
    async def delete(self, url: str, data: Optional[bytes] = None, headers: Optional[Mapping[str, str]] = None, max_allowed_time: float = ..., timeout: Union[float, ClientTimeout] = ..., total_attempts: Optional[int] = ..., **kwargs: Any) -> transport.Response:
        ...
    @property
    def is_mtls(self) -> bool:
        ...
    async def close(self) -> None:
        ...
