import http.client
import TokenLib
import utils
import json


def test():
    token = TokenLib.getAccessToken()
    conn = http.client.HTTPSConnection("plugoon.azure-api.net")
    payload = ''
    headers = {
        'Authorization': f'Bearer {token}'
    }
    conn.request("GET", "/api/repo", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    jsonObject = json.loads(data.decode("utf-8"))
    print(jsonObject[0]["name"])

class Backend:
    conn = http.client.HTTPSConnection("localhost", 7071)
    token: str = ""

    def __init__(self) -> None:
        self.token = TokenLib.getAccessToken()
        utils.log("Backend.init", f"init with token: {self.token}")

    @classmethod
    def repo_get(self) -> any:
        payload = ""
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        self.conn.request("GET", "/repo", payload, headers)
        res = self.conn.getresponse()
        data = res.read()
        utils.log("repo_get", data)
