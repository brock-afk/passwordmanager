import os
import uuid
import pathlib
import asyncpg
import asyncpg.connection

from typing import Annotated
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from passwordmanager.vault import VaultRepository, PostgresVaultRepository

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=pathlib.Path("./src/passwordmanager/server/static")),
    name="static",
)

templates = Jinja2Templates(
    directory=pathlib.Path("./src/passwordmanager/server/templates")
)


async def db_connection() -> asyncpg.connection.Connection:
    return await asyncpg.connect(
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB"),
        host=os.getenv("POSTGRES_HOST", "postgres"),
    )


def vault_repository(
    db_connection: Annotated[asyncpg.connection.Connection, Depends(db_connection)]
) -> VaultRepository:
    return PostgresVaultRepository(db_connection)


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
