import os
import unittest

from config import Config
from utils.json_read import read_json_file


class TestReadJsonFile(unittest.TestCase):

    def test_output_data(self):
        """
        Проверка корректности возвращаемых данных при чтении файла
        """
        path = os.path.abspath(os.path.join(Config.dir_path, "tests", "files", "test_images.json"))
        data = read_json_file(path=path)

        assert isinstance(data, dict)
