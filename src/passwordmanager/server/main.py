from fastapi import FastAPI
from passwordmanager.server.routers import vaults

app = FastAPI()

app.include_router(vaults.router)
