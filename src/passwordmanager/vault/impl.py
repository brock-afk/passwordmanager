import json

from .interface import Vault, VaultRepository

__all__ = ["JSONVaultRepository"]


class JSONVaultRepository(VaultRepository):
    def __init__(self, data: str):
        self.vaults: dict = json.loads(data)

    def get(self, id: str) -> Vault | None:
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

    def create(self, id: str) -> Vault:
        pass

    def delete(self, id: str) -> Vault:
        pass

    def save(self) -> None:
        pass
