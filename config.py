import os


class Config:
    """
    Основные параметры конфигурации
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_root_folder: str
    output_folder: str
