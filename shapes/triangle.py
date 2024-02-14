from PIL import ImageDraw, Image

from shapes.base_shape import ShapeBase


class Triangle(ShapeBase):
    """
    Класс для создания треугольника
    """

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.points = kwargs["Shape"]

    def __get_coordinates(self, y_size: int) -> list:
        """
        Метод высчитывает границы треугольника по переданным координатам и размерам листа
        :param y_size: размеры листа по оси y
        :return: список с координатами углов треугольника
        """
        points_list = []

        for point in self.points:
            point_dict = point["Point"]
            points_list.append((point_dict["X"], y_size - point_dict["Y"]))

        return points_list

    def draw(
            self,
            image: Image,
            draw: ImageDraw
    ) -> None:
        """
        Метод рисует треугольник по переданным параметрам
        :param image: объект изображения
        :param draw: объект ImageDraw для рисования
        :return: None
        """
        coordinates = self.__get_coordinates(y_size=image.size[1])

        draw.polygon((coordinates), fill=self.color, width=self.line_width, outline=self.outline)
