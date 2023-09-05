import json
import pytest

from io import StringIO
from passwordmanager.vault import Vault, JSONVaultRepository


@pytest.mark.vault
async def test_json_vault_repository_get_returns_none_when_vault_does_not_exist():
    repository = JSONVaultRepository(StringIO("{}"))

    vault = await repository.get("vault-id")

    assert vault is None


@pytest.mark.vault
async def test_json_vault_repository_get_returns_vault():
    vaults = {
        "vault-id": {
            "accounts": [
                {
                    "name": "account-name",
                    "username": "account-username",
                    "password": "account-password",
                }
            ]
        }
    }
    repository = JSONVaultRepository(StringIO(json.dumps(vaults)))

    vault = await repository.get("vault-id")

    assert isinstance(vault, Vault)


@pytest.mark.vault
async def test_json_vault_repository_get_returns_correct_vault():
    vaults = {
        "vault-id": {
            "accounts": [
                {
                    "name": "account-name",
                    "username": "account-username",
                    "password": "account-password",
                }
            ]
        }
    }
    repository = JSONVaultRepository(StringIO(json.dumps(vaults)))

    vault = await repository.get("vault-id")

    assert vault.id == "vault-id"
    assert len(vault.accounts) == 1
    assert vault.accounts[0].name == "account-name"
    assert vault.accounts[0].username == "account-username"
    assert vault.accounts[0].password == "account-password"
