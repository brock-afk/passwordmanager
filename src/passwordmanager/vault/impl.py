import os
import json

from .interface import Vault, VaultRepository

__all__ = ["JSONVaultRepository"]


class JSONVaultRepository(VaultRepository):
    def __init__(self, vaults_directory: str):
        self.vaults_directory = vaults_directory

    async def get(self, vault_id: str) -> Vault | None:
        try:
            with open(f"{self.vaults_directory}/{vault_id}.json", "r") as data:
                vault = json.load(data)
        except FileNotFoundError:
            return None

        return Vault(
            id=vault_id,
            accounts=[
                Vault.Account(
                    name=account["name"],
                    username=account["username"],
                    password=account["password"],
                )
                for account in vault["accounts"]
            ],
        )

    async def create(self, vault_id: str) -> Vault:
        if os.path.exists(f"{self.vaults_directory}/{vault_id}.json"):
            raise self.VaultExists("A vault with this ID already exists.")

        with open(f"{self.vaults_directory}/{vault_id}.json", "w") as data:
            json.dump({"accounts": []}, data)

        self.save(vault_id, {"accounts": []})

        return Vault(id=vault_id, accounts=[])

    async def delete(self, id: str) -> Vault:
        pass

    def save(self, vault_id: str, vault: dict) -> None:
        with open(f"{self.vaults_directory}/{vault_id}.json", "w") as data:
            json.dump(vault, data)
