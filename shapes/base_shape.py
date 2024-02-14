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
        self.transparency = kwargs.get("transparency", None)
        self._color = kwargs.get("Color", None)

    @property
    def color(self) -> str | None:
        """
        Изменяем цвет в зависимости от прозрачности фигуры
        """

        if self.transparency == "off" and self._color is None:
            self._color = "white"

        elif self.transparency == "on":
            self._color = None

        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color
