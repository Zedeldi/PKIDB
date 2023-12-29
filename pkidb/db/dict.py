from typing import Any, Iterable, Optional

from benedict import benedict

from pkidb.db import BaseDatabase


class DictDatabase(BaseDatabase):
    """Dictionary implementation for database."""

    def __init__(self) -> None:
        """Initialise instance."""
        self._data = benedict()

    def get(self, key: Iterable[Any]) -> Any:
        """Get value referenced by specified key."""
        return self._data.get(key)

    def set(self, key: Iterable[Any], value: Any) -> None:
        """Set specified key to value."""
        self._data.set(key, value)

    def list(self, parent: Iterable[Any] = []) -> Optional[tuple[Any, ...]]:
        """Return children of parent key."""
        if not parent:
            return tuple(self._data.keys())
        value = self._data.get(parent)
        if not value:
            return None
        elif not isinstance(value, dict):
            return tuple()
        return tuple(value.keys())
