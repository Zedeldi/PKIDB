import base64
import hashlib
from dataclasses import dataclass, field
from typing import Optional

import rsa


@dataclass
class Data:
    """Dataclass to handle user input."""

    key: str
    n: int
    e: int
    value: Optional[str] = None
    signature: Optional[str | bytes] = None
    public_key: rsa.PublicKey = field(init=False, default=None)
    fingerprint: str = field(init=False)
    keypath: tuple[str, str] = field(init=False)
    signature_path: tuple[str, str] = field(init=False)

    def __post_init__(self) -> None:
        """Post initialisation setup."""
        self.public_key = rsa.PublicKey(self.n, self.e)
        self.fingerprint = hashlib.sha256(str(self.n).encode()).hexdigest()
        if isinstance(self.signature, str):
            self.signature = base64.b64decode(self.signature)
        self.keypath = (self.fingerprint, self.key)
        self.signature_path = (self.fingerprint, f"{self.key}.sig")

    @property
    def signature_encoded(self) -> str:
        """Return Base64-encoded signature."""
        return base64.b64encode(self.signature).decode()

    def verify(self) -> bool:
        """Verify signature of value with public key."""
        if not self.value or not self.signature:
            return False
        try:
            rsa.verify(self.value.encode(), self.signature, self.public_key)
            return True
        except rsa.VerificationError:
            return False
