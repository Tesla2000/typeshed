import abc
from typing import Any, Mapping, Optional, Sequence, Union


REAUTH_ORIGIN: str
SAML_CHALLENGE_MESSAGE: str
WEBAUTHN_TIMEOUT_MS: int

def get_user_password(text: str) -> str:
    ...

class ReauthChallenge(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...
    @property
    @abc.abstractmethod
    def is_locally_eligible(self) -> bool:
        ...
    @abc.abstractmethod
    def obtain_challenge_input(self, metadata: Mapping[str, Any]) -> Any:
        ...

class PasswordChallenge(ReauthChallenge):
    @property
    def name(self) -> str:
        ...
    @property
    def is_locally_eligible(self) -> bool:
        ...
    def obtain_challenge_input(self, unused_metadata: Any) -> dict[str, str]:
        ...

class SecurityKeyChallenge(ReauthChallenge):
    @property
    def name(self) -> str:
        ...
    @property
    def is_locally_eligible(self) -> bool:
        ...
    def obtain_challenge_input(self, metadata: Mapping[str, Any]) -> dict[str, Any] | None:
        ...
    def _obtain_challenge_input_webauthn(self, metadata: Mapping[str, Any], webauthn_handler: Any) -> dict[str, Any]:
        ...
    def _unpadded_urlsafe_b64recode(self, s: str) -> str:
        ...

class SamlChallenge(ReauthChallenge):
    @property
    def name(self) -> str:
        ...
    @property
    def is_locally_eligible(self) -> bool:
        ...
    def obtain_challenge_input(self, metadata: Mapping[str, Any]) -> None:
        ...

AVAILABLE_CHALLENGES: dict[str, ReauthChallenge]
