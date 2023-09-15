import os
import asyncpg
import asyncpg.connection

from typing import Annotated
from fastapi import Depends
from passwordmanager.vault import VaultRepository, PostgresVaultRepository


async def db_connection() -> asyncpg.connection.Connection:
    return await asyncpg.connect(
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB"),
        host=os.getenv("POSTGRES_HOST", "postgres"),
    )


def vault_repository(
    db_connection: Annotated[asyncpg.connection.Connection, Depends(db_connection)]
) -> VaultRepository:
    return PostgresVaultRepository(db_connection)
