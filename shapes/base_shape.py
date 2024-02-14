class ShapeBase:
    """
    Базовая модель для создания фигур
    """

    def __init__(
            self,
            *args,
            **kwargs
    ):
        """
        Базовые параметры для всех фигур
        :param line_width: толщина линии
        :param outline: цвет обводки
        :param transparency: прозрачность
        """
        self.line_width = kwargs.get("line_width", 1)
        self.outline = kwargs.get("outline", (0, 0, 0))
        self.color = kwargs.get("Color", None)
