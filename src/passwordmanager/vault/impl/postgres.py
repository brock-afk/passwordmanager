import asyncpg.connection

from ..interface import Vault, VaultRepository


class PostgresVaultRepository(VaultRepository):
    def __init__(self, db_connection: asyncpg.connection.Connection) -> None:
        self.db_connection = db_connection

    async def get_all(self) -> list[Vault]:
        result = await self.db_connection.fetch(
            """
            SELECT id
            FROM vault
            """
        )

        return [
            Vault(
                id=vault["id"],
                accounts=[],
            )
            for vault in result
        ]

    async def get(self, vault_id: str) -> Vault | None:
        pass

    async def create(self, vault_id: str) -> Vault:
        pass
