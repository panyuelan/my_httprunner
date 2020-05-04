import jsonpath
import re
from my_httprunner.loader import load_yaml
from requests import sessions

from my_httprunner.validate import is_api, is_testcase

session = sessions.session()
variables_mapping = {}
variable_regex_compile = re.compile(r".*\$(\w+).*")


def run_yaml(yml_file):
    """
    :param yml_file: filepath
    :return:
    """
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
            "validate": {}，
            "extract": {}
        }
    :return:
    """
    request = api_info["request"]
    global variables_mapping
    parse_request = parse_content(request, variables_mapping)

    method = parse_request.pop("method")
    url = parse_request.pop("url")
    reps = session.request(method=method, url=url, **parse_request)

    validator_mapping = api_info["validate"]
    for key in validator_mapping:
        if "$" in key:
            actual_value = extract_json_field(reps, key)
        else:
            actual_value = getattr(reps, key)
        expected_value = validator_mapping[key]
        assert actual_value == expected_value

    extractor_mapping = api_info.get("extract", {})
    for var_name in extractor_mapping:
        var_expr = extractor_mapping[var_name]
        var_value = extract_json_field(reps, var_expr)
        print("var_value --{}".format(var_value))
        variables_mapping[var_name] = var_value
    return True


def parse_content(content, variables_map):
    """
    :param content:
        content的可能是list，dict，str，other
    :param variables_map:
        变量
    :return:
    """
    if isinstance(content, dict):
        parsed_content = {}
        for key, value in content.items():
            parsed_value = parse_content(value, variables_map)
            parsed_content[key] = parsed_value
        return parsed_content

    elif isinstance(content, list):
        parsed_content = []
        for item in content:
            parsed_value = parse_content(item, variables_map)
            parsed_content.append(parsed_value)
        return parsed_content

    elif isinstance(content, str):
        matched = variable_regex_compile.match(content)
        if matched:
            replaced_content = replace_var(content, variables_map)
            return replaced_content
        else:
            return content
    else:
        return content


def replace_var(content, variables_map):
    """
    将变量，根据variables_map，进行替换
    :param content:
    :param variables_map:
    :return:
    """
    matched = variable_regex_compile.match(content)
    if not matched:
        return content
    var_name = matched[1]
    value = variables_map[var_name]
    replaced_content = content.replace("${}".format(var_name), str(value))
    return replaced_content


def extract_json_field(resp, json_field):
    """
    利用jsonpath 根据json_field公式取resp中的值
    :param resp:  接口请求返回的response
    :param json_field： 需要查找的字段key  $.code
    :return:
    """
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]
