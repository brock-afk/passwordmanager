import pathlib

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from passwordmanager.server.routers import vaults

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=pathlib.Path("./src/passwordmanager/server/static")),
    name="static",
)
app.include_router(vaults.router)
