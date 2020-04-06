import jsonpath

from my_httprunner.loader import load_yaml
from requests import sessions

from my_httprunner.validate import is_api, is_testcase

session = sessions.session()


def run_yaml(yml_file):
    load_content = load_yaml(yml_file)
    result = []
    if is_api(load_content):
        res = run_api(load_content)
        result.append(res)
    elif is_testcase(load_content):
        for api_info in load_content:
            res = run_api(api_info)
            result.append(res)
    else:
        raise Exception("YMAL format invlid:{}".format(yml_file))

    print("result: {}".format(result))
    return result


def run_api(api_info):
    """
    :param api_info:
        {
            "request": {},
            "validate": {}
        }
    :return:
    """
    request = api_info["request"]
    method = request.pop("method")
    url = request.pop("url")
    reps = session.request(method=method, url=url, **request)

    validator_mapping = api_info["validate"]
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
