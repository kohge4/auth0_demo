#language: ja
機能: JWT認証機能のテスト

  シナリオ: GET auth/test のテストをする(permissionを持っている場合)

    前提 サーバーが立ち上がっている
    かつ live_list.jsonがセットされている
    かつ リクエスト用のJWTを準備する(permission有り)
    かつ JWKを用意する
    もし auth/test にGETでリクエストする(permission有り)
    ならば ステータスコードが200
    かつ jsonでデータが返される
    かつ live_listの配列の数が変わらない
    

  シナリオ: GET auth/test のテストをする(permissionを持っていない場合)

    前提 サーバーが立ち上がっている
    かつ live_list.jsonがセットされている
    かつ リクエスト用のJWTを準備する(permission無し)
    かつ JWKを用意する
    もし auth/test にGETでリクエストする(permission無し)
    ならば ステータスコードが403
