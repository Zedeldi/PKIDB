from pathlib import Path
from typing import Any, Iterable, Optional

from pkidb.db import BaseDatabase


class FileDatabase(BaseDatabase):
    """File implementation for database."""

    def __init__(self, path: Path | str = Path("data")) -> None:
        """Initialise instance."""
        self._path = Path(path)

    def _get_path(self, key: Iterable[Any]) -> Path:
        """Get full path from key."""
        path = self._path
        for part in key:
            path /= part
        return path

    def get(self, key: Iterable[Any]) -> Any:
        """Get value referenced by specified key."""
        path = self._get_path(key)
        try:
            with open(path, "r") as fd:
                value = fd.read()
        except FileNotFoundError:
            return None
        return value

    def set(self, key: Iterable[Any], value: Any) -> None:
        """Set specified key to value."""
        path = self._get_path(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as fd:
            fd.write(value)

    def list(self, parent: Iterable[Any] = []) -> Optional[tuple[Any, ...]]:
        """Return children of parent key."""
        path = self._get_path(parent)
        if not path.exists():
            return None
        if path.is_file():
            return tuple()
        return tuple(path.relative_to(self._path).name for path in path.iterdir())
