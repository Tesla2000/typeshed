from google.oauth2.webauthn_handler import WebAuthnHandler

class WebauthnHandlerFactory:
    handlers: list[WebAuthnHandler]
    def __init__(self) -> None:
        ...
    def get_handler(self) -> WebAuthnHandler | None:
        ...