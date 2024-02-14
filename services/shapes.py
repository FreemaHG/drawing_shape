from logger import logger

from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle


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
    def __square(cls, square_data: dict) -> Square:
        """
        Метод создает и возвращает экземпляр прямоугольника
        :param square_data: словарь с параметрами квадрата
        :return: объект квадрата
        """
        return Square(**square_data)

    @classmethod
    def __triangle(cls, triangle_data: dict) -> Triangle:
        """
        Метод создает и возвращает экземпляр треугольника
        :param triangle_data: словарь с параметрами треугольника
        :return: объект треугольника
        """
        return Triangle(**triangle_data)

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

                square_data = figure.get("Square", None)

                if square_data:
                    square = cls.__square(square_data=square_data)
                    figures_list.append(square)

                triangle_data = figure.get("Triangle", None)

                if triangle_data:
                    triangle = cls.__triangle(triangle_data=triangle_data)
                    figures_list.append(triangle)

        return figures_list
