class GoogleAuthError(Exception):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def retryable(self) -> bool: ...

class TransportError(GoogleAuthError):
    pass

class RefreshError(GoogleAuthError):
    pass

class UserAccessTokenError(GoogleAuthError):
    pass

class DefaultCredentialsError(GoogleAuthError):
    pass

class MutualTLSChannelError(GoogleAuthError):
    pass

class ClientCertError(GoogleAuthError):
    @property
    def retryable(self) -> bool: ...

class OAuthError(GoogleAuthError):
    pass

class ReauthFailError(RefreshError):
    def __init__(self, message: str | None = None, **kwargs) -> None: ...

class ReauthSamlChallengeFailError(ReauthFailError):
    pass

class MalformedError(DefaultCredentialsError, ValueError):
    pass

class InvalidResource(DefaultCredentialsError, ValueError):
    pass

class InvalidOperation(DefaultCredentialsError, ValueError):
    pass

class InvalidValue(DefaultCredentialsError, ValueError):
    pass

class InvalidType(DefaultCredentialsError, TypeError):
    pass

class OSError(DefaultCredentialsError, EnvironmentError):
    pass

class TimeoutError(GoogleAuthError):
    pass

class ResponseError(GoogleAuthError):
    pass