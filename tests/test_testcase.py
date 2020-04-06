import os
import unittest
from my_httprunner.loader import load_yaml
from my_httprunner.runner import run_yaml


class TestSingleApi(unittest.TestCase):

    def test_loader_single_testcase(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "testcase", "mubu_login.yml")
        result = load_yaml(single_api_yaml)
        self.assertIsInstance(result, list)

    def test_run_single_api_yaml(self):
        testcase_yaml = os.path.join(os.path.dirname(__file__), "testcase", "mubu_login.yml")
        result = run_yaml(testcase_yaml)
        self.assertEqual(len(result), 2)

