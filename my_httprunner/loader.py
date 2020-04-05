import yaml


def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        result = yaml.load(file.read(), Loader=yaml.FullLoader)
    return result
