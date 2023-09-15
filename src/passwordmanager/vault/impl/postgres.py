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
        result = await self.db_connection.fetchrow(
            """
            INSERT INTO vault (name, description, created_at, updated_at)
            VALUES ($1, $2, CLOCK_TIMESTAMP(), CLOCK_TIMESTAMP())
            RETURNING id
            """,
            vault_id,
            "description",
        )

        return Vault(
            id=result["id"],
            accounts=[],
        )
