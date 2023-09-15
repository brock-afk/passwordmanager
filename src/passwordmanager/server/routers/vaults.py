import uuid
import pathlib

from typing import Annotated
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, Depends, APIRouter
from passwordmanager.vault import VaultRepository
from passwordmanager.server.dependencies import vault_repository

router = APIRouter()

templates = Jinja2Templates(
    directory=pathlib.Path("./src/passwordmanager/server/templates")
)


@router.get("/", response_class=HTMLResponse)
@router.get("/vaults", response_class=HTMLResponse)
async def get_vaults(
    request: Request,
    vault_repository: Annotated[VaultRepository, Depends(vault_repository)],
):
    vaults = await vault_repository.get_all()

    return templates.TemplateResponse(
        "index.html", {"request": request, "vaults": vaults}
    )


@router.post("/vaults/new", response_class=HTMLResponse)
async def create_vault(
    request: Request,
    vault_repository: Annotated[VaultRepository, Depends(vault_repository)],
):
    await vault_repository.create(str(uuid.uuid4()))
    vaults = await vault_repository.get_all()

    return templates.TemplateResponse(
        "vaults.html", {"request": request, "vaults": vaults}
    )
