import os
import unittest
from my_httprunner.runner import run_yaml


class TestSingleApi(unittest.TestCase):

    def test_run_single_api_yaml(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "homepage.yml")
        result = run_yaml(single_api_yaml)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], True)

    def test_run_single_with_jsonpath(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "login.yml")
        result = run_yaml(single_api_yaml)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], True)

