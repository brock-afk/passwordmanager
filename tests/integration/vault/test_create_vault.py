import pytest

from passwordmanager.vault import JSONVaultRepository


@pytest.mark.vault
async def test_create_vault_without_accounts(vaults_directory: str):
    vault_repository = JSONVaultRepository(vaults_directory)
    vault = await vault_repository.create("vault_id")

    assert vault.id == "vault_id"
    assert vault.accounts == []


@pytest.mark.vault
async def test_create_vault_raises_vault_exists_if_vault_exists(vaults_directory: str):
    vault_repository = JSONVaultRepository(vaults_directory)
    await vault_repository.create("vault_id")

    with pytest.raises(JSONVaultRepository.VaultExists):
        await vault_repository.create("vault_id")
