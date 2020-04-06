import os
import unittest
import subprocess


class TestCli(unittest.TestCase):
    def test_panrun_single_yaml(self):
        pass
        # single_api_yaml = os.path.join(
        #     os.path.dirname(__file__), "tests", "api", "login.yml")
        # project_root_dir = os.path.dirname(os.path.dirname(__file__))
        # subprocess.run("python -m my_httprunner.cli {}".format(single_api_yaml), cwd=project_root_dir)
