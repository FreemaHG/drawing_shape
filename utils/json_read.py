import json


def read_json_file(path: str) -> dict:
    """
    Функция читает json-файл, возвращая данные в виде словаря
    :param path: полный путь с файлом
    :return: словарь с извлеченными данными
    """

    with open(path) as json_file:
        data = json.load(json_file)

        return data
