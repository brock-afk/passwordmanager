import json

from io import StringIO
from .interface import Vault, VaultRepository

__all__ = ["JSONVaultRepository"]


class JSONVaultRepository(VaultRepository):
    def __init__(self, data: StringIO):
        self.data = data

    @property
    def vaults(self) -> dict:
        return json.load(self.data)

    async def get(self, id: str) -> Vault | None:
        vault = self.vaults.get(id)

        if vault is None:
            return None

        return Vault(
            id=id,
            accounts=[
                Vault.Account(
                    name=account["name"],
                    username=account["username"],
                    password=account["password"],
                )
                for account in vault["accounts"]
            ],
        )

    async def create(self, id: str) -> Vault:
        pass

    async def delete(self, id: str) -> Vault:
        pass

    def save(self) -> None:
        json.dump(self.vaults, self.data)
