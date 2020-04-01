import requests


def test_get_homepage():
    url = "https://mubu.com/"
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/80.0.3987.149 Safari/537.36 "
               }
    resp = requests.get(url, headers=headers, verify=False)
    assert resp.status_code == 200


if __name__ == "__main__":
    test_get_homepage()
