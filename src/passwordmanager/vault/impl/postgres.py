import asyncpg.connection

from ..interface import Vault, VaultRepository

__all__ = ["PostgresVaultRepository"]


class PostgresVaultRepository(VaultRepository):
    def __init__(self, db_connection: asyncpg.connection.Connection) -> None:
        self.db_connection = db_connection

    async def get_all(self) -> list[Vault]:
        result = await self.db_connection.fetch(
            """
            SELECT id, name, description
            FROM vault
            """
        )

        return [
            Vault(
                id=vault["id"],
                name=vault["name"],
                description=vault["description"],
                accounts=[],
            )
            for vault in result
        ]

    async def get(self, vault_id: str) -> Vault | None:
        pass

    async def create(self, name: str, description: str) -> Vault:
        result = await self.db_connection.fetchrow(
            """
            INSERT INTO vault (name, description, created_at, updated_at)
            VALUES ($1, $2, CLOCK_TIMESTAMP(), CLOCK_TIMESTAMP())
            RETURNING id, name, description
            """,
            name,
            description,
        )

        return Vault(
            id=result["id"],
            name=result["name"],
            description=result["description"],
            accounts=[],
        )
