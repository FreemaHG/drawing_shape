import os
import unittest

from config import Config
from services.shapes import ShapesCreateService
from shapes.circle import Circle
from utils.json_read import read_json_file


class TestCreateShapes(unittest.TestCase):

    def setUp(self) -> None:
        path = os.path.abspath(os.path.join(Config.dir_path, "tests", "files", "test_images.json"))
        self.data = read_json_file(path)

    def test_create_base_shape(self):
        """
        Проверка корректности создания свойств по умолчанию для базовой модели фигуры
        """
        figures = ShapesCreateService.create_figures(data=self.data)

        self.assertTrue(figures[0].line_width == 5)
        self.assertTrue(figures[0].color == "red")
        self.assertTrue(figures[0].outline == (0, 0, 0))
        self.assertTrue(figures[0].transparency is None)

    def test_create_circle(self):
        """
        Проверка корректности создания круга
        """
        figures = ShapesCreateService.create_figures(data=self.data)

        self.assertTrue(isinstance(figures[0], Circle))
        self.assertTrue(figures[0].X_center == 45)
        self.assertTrue(figures[0].Y_center == 20)
        self.assertTrue(figures[0].Radius == 9)
