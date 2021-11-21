import os
import json
import urllib.request as request

WEB_HOOK_URL = os.environ["WEB_HOOK_URL"]
GITHUB_API = os.environ["GITHUB_API"]


def lambda_handler(event, context):

    print(getLastCommitDate())
    return "hoge"


def getLastCommitDate():
    last_commit_date = request.Request(GITHUB_API)
    with request.urlopen(GITHUB_API) as res:
        hoge = res.read()
        hoge = hoge.decode()

        fuga = hoge["commit"]["committer"]["date"]
        print(fuga)
    return hoge
