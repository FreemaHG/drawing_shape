from PIL import ImageDraw, Image

from shapes.base_shape import ShapeBase


class Circle(ShapeBase):
    """
    Класс для создания круга
    """

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.X_center = kwargs["X_center"]
        self.Y_center = kwargs["Y_center"]
        self.Radius = kwargs["Radius"]

    def __get_coordinates(self, y_size: int) -> tuple:
        """
        Метод высчитывает границы круга по координатам, радиусу круга и размерам листа
        :param y_size: размеры листа по оси y
        :param circle: экземпляр круга с координатами и радиусом
        :return: кортеж с границами круга
        """
        _half_radius = self.Radius / 2

        x1 = self.X_center - _half_radius
        y1 = y_size - (self.Y_center + _half_radius)
        x2 = self.X_center + _half_radius
        y2 = y_size - (self.Y_center - _half_radius)

        return x1, y1, x2, y2

    def draw(self, image: Image, draw: ImageDraw) -> None:
        """
        Метод рисует круг по заданным координатам
        :param image: объект изображения
        :param draw: объект ImageDraw для рисования
        :return: None
        """
        coordinates = self.__get_coordinates(y_size=image.size[1])

        draw.ellipse((coordinates), fill=self.color, width=self.line_width, outline=self.outline)
