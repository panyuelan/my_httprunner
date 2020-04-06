import jsonpath

from my_httprunner.loader import load_yaml
import requests


def run_yaml(file_path):
    load_json = load_yaml(file_path)

    request = load_json["request"]
    method = request.pop("method")
    url = request.pop("url")
    kwargs = request
    reps = requests.request(method=method, url=url, **kwargs)

    validator_mapping = load_json["validate"]
    for key in validator_mapping:
        if "$" in key:
           actual_value = extract_json_field(reps, key)
        else:
           actual_value = getattr(reps, key)
        expected_value = validator_mapping[key]
        assert actual_value == expected_value
    return True


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]
