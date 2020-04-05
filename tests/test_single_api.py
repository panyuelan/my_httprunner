import os
import unittest
from my_httprunner.loader import load_yaml


class TestSingleApi(unittest.TestCase):

    def test_loading_single_api(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "homepage.yml")
        loaded_json = load_yaml(single_api_yaml)
        return loaded_json

    def test_single_api(self):
        pass
