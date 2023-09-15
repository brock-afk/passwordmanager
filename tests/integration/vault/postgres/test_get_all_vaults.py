import pytest
import asyncpg.connection

from passwordmanager.vault.interface import Vault
from passwordmanager.vault.impl.postgres import PostgresVaultRepository


@pytest.mark.postgres
async def test_get_all_vaults_returns_list_of_vaults(
    postgres_connection: asyncpg.connection.Connection,
):
    await postgres_connection.execute(
        """
        INSERT INTO vault (name, description, created_at, updated_at)
        VALUES ($1, $2, CLOCK_TIMESTAMP(), CLOCK_TIMESTAMP())
        """,
        "vault_name",
        "vault_description",
    )

    vault_repository = PostgresVaultRepository(postgres_connection)

    vaults = await vault_repository.get_all()

    assert len(vaults) == 1
    for vault in vaults:
        assert isinstance(vault, Vault)
