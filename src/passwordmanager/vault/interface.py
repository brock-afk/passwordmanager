from dataclasses import dataclass
from abc import ABC, abstractmethod

__all__ = ["Vault", "VaultRepository"]


@dataclass
class Vault:
    @dataclass
    class Account:
        name: str
        username: str
        password: str

    id: str
    accounts: list[Account]


class VaultRepository(ABC):
    class VaultExists(Exception):
        pass

    @abstractmethod
    async def get_all(self) -> list[Vault]:
        pass

    @abstractmethod
    async def get(self, id: str) -> Vault:
        pass

    @abstractmethod
    async def create(self, id: str) -> Vault:
        pass

    @abstractmethod
    async def delete(self, id: str) -> Vault:
        pass
