
# 校验从yaml读取的api的格式


def is_api(content):
    """
    校验content的格式是否是单个api的格式
    判断content中类型是否是字典，判断request和validate是否在content中，
    有一个条件不满足返回False
    :param content:
    :return:
    """
    if not isinstance(content, dict):
        return False
    if "request" not in content:
        return False
    if "validate" not in content:
        return False
    return True


def is_testcase(content):
    """
    校验content的格式是否是list，多个api的合集
    并校验list中的单个api格式是否正确，不正确返回False
    :param content:
    :return:
    """
    if not isinstance(content, list):
        return False
    for item in content:
        if not is_api(item):
            return False
    return True
