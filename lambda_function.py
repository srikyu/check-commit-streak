import os
import json
import urllib.request as request

WEB_HOOK_URL = os.environ["WEB_HOOK_URL"]
GITHUB_API = os.environ["GITHUB_API"]


def lambda_handler(event, context):

    print(getLastCommitDate())
    return "hoge"


# 最終コミット日付を取得する
def getLastCommitDate():
    with request.urlopen(GITHUB_API) as res:
        api_result = res.read()
        decode_result = json.loads(api_result.decode('utf-8'))
        last_commit_date = decode_result[0]["commit"]["committer"]["date"]

    return last_commit_date

# 最終コミット日付と今日の日付を比較して連続で更新されているのかチェックする


def checkDateStreak(last_commit_date):
    if
