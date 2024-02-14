import os

from config import Config

from utils.json_read import read_json_file
from services.data.config import ConfigSaveService
from services.draw import DrawShapesService
from services.image import ImageService
from services.shapes import ShapesCreateService


def draw_shapes():
    """
    Сохранение параметров ввода / вывода данных, создание нового изображения и зарисовка фигур по параметрам
    """

    ConfigSaveService.input_output_data()

    path = os.path.abspath(os.path.join(Config.data_root_folder, "images.json"))
    data = read_json_file(path=path)

    image_size = data.get("image_size", None)

    image = ImageService.create_image(**image_size)

    draw = ImageService.create_draw(image)

    figures_list = ShapesCreateService.create_figures(data=data)

    DrawShapesService.draw(figures=figures_list, image=image, draw=draw)

    ImageService.save_image(image, Config.output_folder, "images.jpg")


if __name__ == '__main__':
    draw_shapes()
