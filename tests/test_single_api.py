import os
import unittest
from my_httprunner.loader import load_yaml
from my_httprunner.runner import run_yaml


class TestSingleApi(unittest.TestCase):

    def test_run_single_api_yaml(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "homepage.yml")
        resp = run_yaml(single_api_yaml)
        self.assertEqual(resp, True)

    def test_run_single_with_jsonpath(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "login.yml")
        resp = run_yaml(single_api_yaml)
        self.assertEqual(resp, True)

