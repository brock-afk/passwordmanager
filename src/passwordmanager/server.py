from sanic import Sanic, Request, json
from passwordmanager.vault import JSONVaultRepository

app = Sanic("passwordmanager")


@app.get("/vaults")
async def get_vaults(request: Request):
    vault_repository = JSONVaultRepository("/data/vaults")
    vaults = await vault_repository.get_all()

    return json({"vaults": vaults})
