from PIL import ImageDraw, Image

from shapes.base_shape import ShapeBase


class Square(ShapeBase):
    """
    Класс для создания квадрата
    """

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.X_upper_left = kwargs["X_upper_left"]
        self.Y_upper_left = kwargs["Y_upper_left"]
        self.side_length = kwargs["side_length"]

    def __get_coordinates(self, y_size: int) -> tuple:
        """
        Метод высчитывает границы квадрата по переданным координатам и размерам листа
        :param y_size: размеры листа по оси y
        :return: кортеж с границами квадрата
        """
        x1 = self.X_upper_left
        y1 = y_size - self.Y_upper_left
        x2 = x1 + self.side_length
        y2 = y1 + self.side_length

        return x1, y1, x2, y2

    def draw(
            self,
            image: Image,
            draw: ImageDraw
    ) -> None:
        """
        Метод рисует квадрат по переданным параметрам
        :param image: объект изображения
        :param draw: объект ImageDraw для рисования
        :return: None
        """
        coordinates = self.__get_coordinates(y_size=image.size[1])

        draw.rectangle((coordinates), fill=self.color, width=self.line_width, outline=self.outline)
