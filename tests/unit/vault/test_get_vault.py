import json
import pytest

from passwordmanager.vault import Vault, JSONVaultRepository


@pytest.mark.vault
async def test_json_vault_repository_get_returns_none_when_vault_does_not_exist(
    vaults_directory: str,
):
    vault_id = "vault-id"
    repository = JSONVaultRepository(vaults_directory)

    vault = await repository.get(vault_id)

    assert vault is None


@pytest.mark.vault
async def test_json_vault_repository_get_returns_vault(vaults_directory: str):
    vault_id = "vault-id"
    vault = {
        "accounts": [
            {
                "name": "account-name",
                "username": "account-username",
                "password": "account-password",
            }
        ]
    }
    with open(f"{vaults_directory}/{vault_id}.json", "w") as data:
        json.dump(vault, data)

    repository = JSONVaultRepository(vaults_directory)

    vault = await repository.get(vault_id)

    assert isinstance(vault, Vault)


@pytest.mark.vault
async def test_json_vault_repository_get_returns_correct_vault(vaults_directory: str):
    vault_id = "vault-id"
    vault = {
        "accounts": [
            {
                "name": "account-name",
                "username": "account-username",
                "password": "account-password",
            }
        ]
    }
    with open(f"{vaults_directory}/{vault_id}.json", "w") as data:
        json.dump(vault, data)

    repository = JSONVaultRepository(vaults_directory)

    vault = await repository.get(vault_id)

    assert vault.id == "vault-id"
    assert len(vault.accounts) == 1
    assert vault.accounts[0].name == "account-name"
    assert vault.accounts[0].username == "account-username"
    assert vault.accounts[0].password == "account-password"
