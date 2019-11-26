from fastapi import FastAPI
from starlette.requests import Request
from views import auth_demo


app = FastAPI()
import cors  # NOQA


app.include_router(auth_demo.router)
