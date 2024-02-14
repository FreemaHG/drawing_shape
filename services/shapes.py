from logger import logger

from shapes.circle import Circle
from shapes.rectangle import Rectangle


class ShapesCreateService:
    """
    Сервис для создания фигур по переданным параметрам
    """

    @classmethod
    def __circle(cls, circle_data: dict) -> Circle:
        """
        Метод создает и возвращает экземпляр круга
        :param circle_data: словарь с параметрами круга
        :return: объект круга
        """
        return Circle(**circle_data)

    @classmethod
    def __rectangle(cls, rectangle_data: dict) -> Rectangle:
        """
        Метод создает и возвращает экземпляр прямоугольника
        :param rectangle_data: словарь с параметрами прямоугольника
        :return: объект прямоугольника
        """
        return Rectangle(**rectangle_data)

    @classmethod
    def create_figures(cls, data: dict) -> list:
        """
        Метод парсит полученные данные и создает указанные фигуры
        :param data: словарь с данными
        :return: список с фигурами
        """

        figures_list = []

        figures = data.get("figures", None)

        if not figures:
            logger.warning("Фигур нет")

        else:
            for figure in figures:

                circle_data = figure.get("Circle", None)

                if circle_data:
                    circle = cls.__circle(circle_data=circle_data)
                    figures_list.append(circle)

                rectangle_data = figure.get("Rectangle", None)

                if rectangle_data:
                    rectangle = cls.__rectangle(rectangle_data=rectangle_data)
                    figures_list.append(rectangle)

        return figures_list
