import os
from pathlib import Path

from PIL import Image, ImageDraw


class ImageService:
    """
    Сервис для создания и сохранения изображения
    """

    @classmethod
    def create_image(cls, X_length: int = 250, Y_length: int = 250, background_color: str = 'white') -> Image:
        """
        Метод создает пустое изображение нужного размера
        :param X_length: размеры листа по оси x
        :param Y_length: размеры листа по оси y
        :param background_color: цвет фона изображения
        :return: объект изображения
        """
        image = Image.new('RGB', (X_length, Y_length), background_color)

        return image

    @classmethod
    def create_draw(cls, image: Image) -> ImageDraw:
        """
        Метод создает объект ImageDraw для рисования фигур
        :param image: объект изображения
        :return: объект ImageDraw
        """
        draw = ImageDraw.Draw(image)

        return draw

    @classmethod
    def save_image(cls, image_obj: Image, path: str, image_name: str) -> None:
        """
        Метод сохраняет изображение под указанным именем и директорией
        :param image_obj: объект изображения для сохранения
        :param path: директория для сохранения картинки
        :param image_name: название файла изображения
        :return: None
        """
        Path(path).mkdir(parents=True, exist_ok=True)
        path = os.path.abspath(os.path.join(path, image_name))

        image_obj.save(path, quality=95)
