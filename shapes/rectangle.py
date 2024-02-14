from PIL import ImageDraw, Image

from shapes.base_shape import ShapeBase


class Rectangle(ShapeBase):
    """
    Класс для создания прямоугольника
    """

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.X_upper_left = kwargs["X_upper_left"]
        self.Y_upper_left = kwargs["Y_upper_left"]
        self.X_lower_right = kwargs["X_lower_right"]
        self.Y_lower_right = kwargs["Y_lower_right"]

    def __get_coordinates(self, y_size: int) -> tuple:
        """
        Метод высчитывает границы прямоугольника по переданным координатам и размерам листа
        :param y_size: размеры листа по оси y
        :return: кортеж с границами прямоугольника
        """
        x1 = self.X_upper_left
        y1 = y_size - self.Y_upper_left
        x2 = self.X_lower_right
        y2 = y_size - self.Y_lower_right

        return x1, y1, x2, y2

    def draw(
            self,
            image: Image,
            draw: ImageDraw
    ) -> None:
        """
        Метод рисует прямоугольник по переданным параметрам
        :param image: объект изображения
        :param draw: объект ImageDraw для рисования
        :return: None
        """
        coordinates = self.__get_coordinates(y_size=image.size[1])

        draw.rectangle((coordinates), fill=self.color, width=self.line_width, outline=self.outline)
