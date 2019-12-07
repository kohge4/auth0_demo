# python(fastAPI) で auth0 のRBAC を実現するコード

- auth0 の JWT を持たせて エンドポイント /auth/demo にアクセスすると動作します。SPAのバックエンド用のコードなので単体ではうまく動作しないですが,python の環境がある状態で

pipenv install -d 

behave  

の順にコマンドラインで操作するとテストの結果を確認できます

- インターン先で Auth0 の技術検証を担当していたときに書いたコードです。

下記は関連する発表資料と技術ブログです

発表資料: https://speakerdeck.com/kohge4/python-fastapi-deshu-karetaspaniren-zheng-ji-neng-wotukeru

JX通信社技術ブログ: https://tech.jxpress.net/entry/2019/12/05/161941

