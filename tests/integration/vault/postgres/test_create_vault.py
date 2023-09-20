import pytest
import asyncpg.connection

from passwordmanager.vault.interface import Vault
from passwordmanager.vault.impl.postgres import PostgresVaultRepository


@pytest.mark.postgres
async def test_create_vault_inserts_into_vault_table(
    postgres_connection: asyncpg.connection.Connection,
):
    vault_repository = PostgresVaultRepository(postgres_connection)

    await vault_repository.create("vault_name", "vault_description")

    result = await postgres_connection.fetch(
        """
        SELECT id
        FROM vault
        """
    )

    assert len(result) == 1


@pytest.mark.postgres
async def test_create_vault_returns_vault(
    postgres_connection: asyncpg.connection.Connection,
):
    vault_repository = PostgresVaultRepository(postgres_connection)

    vault = await vault_repository.create("vault_name", "vault_description")

    assert isinstance(vault, Vault)
