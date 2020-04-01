import requests
import unittest


class Demo(unittest.TestCase):
    def test_get_homepage(self):
        url = "https://mubu.com/"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.149 Safari/537.36 "
        }
        resp = requests.get(url, headers=headers, verify=False)
        assert resp.status_code == 200

