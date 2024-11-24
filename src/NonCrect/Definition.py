"""
    NonCrect.Definition

This file contain definitions for using in NonCrect.
"""


""" imports """


from abc import ABC, abstractmethod
from CodingTools2.Decorator import Initializer
from CodingTools2.Definitions import DefinitionsSkeleton


""" Component type """


class ComponentTypeDefinition:
    """ Component type base """

    """ values """
    __id: int
    __name: str

    """ properties """
    @property
    def id(self) -> int: return self.__id
    @property
    def name(self) -> str: return self.__name

    """ processes """

    # instance
    def __init__(self, _id: int, _name: str) -> None:
        """ Set component type values """
        self.__id = _id
        self.__name = _name
        return

    def __eq__(self, other: int) -> bool:
        return self.__id == other

    ...


@Initializer()
class ComponentType(DefinitionsSkeleton):
    """ Component type """
    NoneType = ComponentTypeDefinition(-1, "None")

    Collider = ComponentTypeDefinition(1, "Collider")
    Script = ComponentTypeDefinition(2, "Script")

    Transform = ComponentTypeDefinition(100, "Transform")
    GameObject = ComponentTypeDefinition(101, "GameObject")
    Texture = ComponentTypeDefinition(102, "Texture")
    ...


ComponentType: ComponentType
""" Component type definitions class """


""" Options """


class OptionsDefinition(ABC): ...


@Initializer()
class OptionType(DefinitionsSkeleton):
    """ Option type """
    class Exit(OptionsDefinition): ...
    ...


OptionType: OptionType
""" Option type definitions class """
