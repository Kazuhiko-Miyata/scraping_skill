import requests # ライブラリのインポート

url = 'https://www.python.org/' # 変数urlにPython公式ページのURLを格納 
r = requests.get(url) # 変数rにリクエスト結果を格納

r.url # アクセスしたURLの確認

if r.status_code == 200:  # アクセスに成功したらprint()関数を実行して、それ以外だったらraiseで意図的にエラーを返す
  print('アクセスに成功した時の処理を実行')
else:
  raise

print(r.text) # リクエスト結果の取得
