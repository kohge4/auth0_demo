import json

import responses
from behave import given, when, then
from starlette.testclient import TestClient

import main
from settings import URL


app = main.app


@given('サーバーが立ち上がっている')
def step_impl(context):
    context.client = TestClient(app)


@given('live_list.jsonがセットされている')
def step_impl(context):
    with open('json_for_test/live_list.json') as f:
        context.basic_queries = json.load(f)


@given('リクエスト用のJWTを準備する(permission有り)')
def step_impl(context):
    with open('json_for_test/jwt.txt') as f:
        context.jwt = f.read()


@given('リクエスト用のJWTを準備する(permission無し)')
def step_impl(context):
    with open('json_for_test/jwt_without_permission.txt') as f:
        context.jwt_without_permission = f.read()


@given('JWKを用意する')
def step_impl(context):
    with open('json_for_test/jwk.json') as f:
        context.jwk = json.load(f)


@when('auth/test にGETでリクエストする(permission有り)')
def stem_impl(context):
    with responses.RequestsMock() as resp:
        resp.add(
            responses.GET,
            "https://dev-928ngan9.auth0.com/.well-known/jwks.json",
            json=context.jwk
        )
        resp.add(
            responses.GET,
            URL,
            json=context.basic_queries
        )
        r_get = context.client.get("/auth/test", headers={"Authorization": context.jwt})
        context.get_data = r_get.json()
        context.statuscode = r_get.status_code
        context.resp = list(resp.calls)


@when('auth/test にGETでリクエストする(permission無し)')
def stem_impl(context):
    with responses.RequestsMock() as resp:
        resp.add(
            responses.GET,
            "https://dev-928ngan9.auth0.com/.well-known/jwks.json",
            json=context.jwk
        )
        r_get = context.client.get("/auth/test", headers={"Authorization": context.jwt_without_permission})
        context.statuscode = r_get.status_code
        context.resp = list(resp.calls)


@then('ステータスコードが200')
def step_impl(context):
    assert context.statuscode == 200, " リクエストを正常に処理できませんでした"


@then('jsonでデータが返される')
def step_impl(context):
    assert isinstance(context.get_data, dict), "datatypeが違います"


@then('live_listの配列の数が変わらない')
def step_impl(context):
    live_list = context.get_data
    assert len(live_list['live_list']) == 1, 'dataの数が適切ではありません'


@then('ステータスコードが403')
def step_impl(context):
    assert context.statuscode == 403, " リクエストを正常に処理できませんでした"
