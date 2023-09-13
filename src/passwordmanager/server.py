import uuid

from sanic import Sanic, Request
from passwordmanager.vault import JSONVaultRepository

app = Sanic("passwordmanager")


@app.get("/")
@app.ext.template("index.html")
async def get_vaults(request: Request):
    vault_repository = JSONVaultRepository("/data/vaults")
    vaults = await vault_repository.get_all()

    return {"vaults": vaults}


@app.post("/vaults/new")
@app.ext.template("vaults.html")
async def create_vault(request: Request):
    vault_repository = JSONVaultRepository("/data/vaults")

    await vault_repository.create(str(uuid.uuid4()))
    vaults = await vault_repository.get_all()

    return {"vaults": vaults}
