from pathlib import Path

class WgServerConfig:
    _path: Path

    def __init__(self, path: Path) -> None:
        """Открывает по указанному пути wireguard конфиг"""
        ...

    def initialize(self) -> None:
        ...