from logger import logger

from config import Config
from utils.json_read import read_json_file


class ConfigSaveService:
    """
    Сервис для сохранения параметров конфигурации
    """

    @classmethod
    def input_output_data(cls) -> None:
        """
        Метод сохраняет параметры по вводу и выводу данных
        """
        data = {}

        try:
            # TODO Поменять файл!!!
            data = read_json_file(path="./config-dev.json")

        except FileNotFoundError:
            logger.error("файл с конфигурацией не найден")

        data_root_folder = data.get("data_root_folder", None)
        output_folder = data.get("output_folder", None)

        if data_root_folder and output_folder:
            Config.data_root_folder = data_root_folder
            Config.output_folder = output_folder

        else:
            logger.error("Конфигурация не найдена!")
