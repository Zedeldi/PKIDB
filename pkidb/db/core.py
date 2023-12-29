from abc import ABC, abstractmethod
from typing import Any, Iterable, Optional


class BaseDatabase(ABC):
    """Base abstract class for database."""

    @abstractmethod
    def get(self, key: Iterable[Any]) -> Any:
        """Get value referenced by specified key."""
        ...

    @abstractmethod
    def set(self, key: Iterable[Any], value: Any) -> None:
        """Set specified key to value."""
        ...

    @abstractmethod
    def list(self, parent: Iterable[Any] = []) -> Optional[tuple[Any, ...]]:
        """Return children of parent key."""
        ...
