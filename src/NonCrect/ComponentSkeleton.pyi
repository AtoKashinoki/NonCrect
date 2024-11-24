"""
    NonCrect.ComponentSkeleton.pyi
"""


""" imports """


from abc import ABC, abstractmethod
from .Definition import (
    ComponentType,
    ComponentTypeDefinition,
    OptionsDefinition,
)
from .GameObject import GameObject


""" Component skeleton """


class ComponentSkeleton(ABC):
    __type: ComponentTypeDefinition = \
        ComponentType.NoneType
    @property
    def type(self) -> ComponentTypeDefinition: ...
    def __init__(self, _type: int = ComponentType.NoneType) -> None: ...
    @abstractmethod
    def __process__(self, *args, game_object: GameObject, **kwargs) -> OptionsDefinition | None: ...
