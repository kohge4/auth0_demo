from fastapi import APIRouter, Depends
import requests

from models.querymodels import GetResponse
from auth import auth0
from settings import URL


router = APIRouter()


autho = auth0.JWTBearer(
    auth_config=auth0.auth_config,
    permission=auth0.Permission.READ_API
)


# テスト用にJWTの有効期限を無視
auth_test = auth0.JWTBearer(
    auth_config=auth0.auth_config,
    permission=auth0.Permission.READ_API,
    verify_exp=False
)


@router.get("/auth/demo", response_model=GetResponse, dependencies=[Depends(autho)])
def auth_get():
    r = requests.get(URL).json()
    return r


@router.get("/auth/test", response_model=GetResponse, dependencies=[Depends(auth_test)])
def auth_test_get():
    r = requests.get(URL).json()
    return r


@router.get("/auth/pass", response_model=GetResponse)
def auth_get():
    r = requests.get(URL).json()
    return r
