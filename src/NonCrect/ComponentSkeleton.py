"""
    NonCrect.ComponentSkeleton

This file contain component skeleton  for using in Component.
"""


""" imports """


from abc import ABC, abstractmethod
from .Definition import (
    ComponentType,
    ComponentTypeDefinition,
    OptionsDefinition,
)


""" Component skeleton """


class ComponentSkeleton(ABC):
    """ Component base """

    """ values """
    __type: ComponentTypeDefinition = \
        ComponentType.NoneType

    """ properties """
    @property
    def type(self) -> ComponentTypeDefinition: return self.__type

    """ processes """

    # instance
    def __init__(
            self,
            _type: ComponentTypeDefinition = \
                    ComponentType.NoneType
    ) -> None:
        """ Initialize component """
        self.__type = _type
        return

    @abstractmethod
    def __setup__(self, game_objects, parent_object, **kwargs) -> OptionsDefinition | None: ...
    @abstractmethod
    def __update__(self, game_objects, parent_object, **kwargs) -> OptionsDefinition | None: ...

    ...
