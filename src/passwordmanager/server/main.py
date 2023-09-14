import uuid
import pathlib

from typing import Annotated
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from passwordmanager.vault import VaultRepository, JSONVaultRepository

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=pathlib.Path("./src/passwordmanager/server/static")),
    name="static",
)

templates = Jinja2Templates(
    directory=pathlib.Path("./src/passwordmanager/server/templates")
)


def vault_repository() -> VaultRepository:
    return JSONVaultRepository("/data/vaults")


@app.get("/", response_class=HTMLResponse)
async def get_vaults(
    request: Request,
    vault_repository: Annotated[VaultRepository, Depends(vault_repository)],
):
    vaults = await vault_repository.get_all()

    return templates.TemplateResponse(
        "index.html", {"request": request, "vaults": vaults}
    )


@app.post("/vaults/new", response_class=HTMLResponse)
async def create_vault(
    request: Request,
    vault_repository: Annotated[VaultRepository, Depends(vault_repository)],
):
    await vault_repository.create(str(uuid.uuid4()))
    vaults = await vault_repository.get_all()

    return templates.TemplateResponse(
        "vaults.html", {"request": request, "vaults": vaults}
    )
