import uuid

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from passwordmanager.vault import JSONVaultRepository

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_vaults(request: Request):
    vault_repository = JSONVaultRepository("/data/vaults")
    vaults = await vault_repository.get_all()

    return templates.TemplateResponse(
        "index.html", {"request": request, "vaults": vaults}
    )


@app.post("/vaults/new")
async def create_vault(request: Request):
    vault_repository = JSONVaultRepository("/data/vaults")

    await vault_repository.create(str(uuid.uuid4()))
    vaults = await vault_repository.get_all()

    return templates.TemplateResponse(
        "vaults.html", {"request": request, "vaults": vaults}
    )
