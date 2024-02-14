from PIL import ImageDraw, Image


class DrawShapesService:
    """
    Сервис для рисования фигур
    """

    @classmethod
    def draw(cls, figures: list, image: Image, draw: ImageDraw) -> None:
        """
        Метод рисует все переданные фигуры
        :param figures: список с фигурами
        :param image: объект изображения
        :param draw: объект для рисования
        :return: None
        """
        for figure in figures:
            figure.draw(image=image, draw=draw)
