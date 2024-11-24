"""
    NonCrect.Type

This file contain types for using in NonCrect.
"""


""" imports """


from CodingTools2.Definitions import Index
from CodingTools2.Type import Vector1D


""" Vectors """


class Position(Vector1D):
    """ Position vector """

    """ properties """
    @property
    def x(self) -> float: return self.data[Index.X]
    @x.setter
    def x(self, value: float) -> None: self[Index.X] = value
    @property
    def y(self) -> float: return self.data[Index.Y]
    @y.setter
    def y(self, value: float) -> None: self[Index.Y] = value

    """ processes """

    # instance
    def __init__(self, _data: tuple | list = (0, 0)):
        super().__init__(_data, length=2)
        return

    ...


class Force(Position):
    """ Force vector """

    ...
