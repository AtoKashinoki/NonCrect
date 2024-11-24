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
    def __setup__(self, game_objects, parent_object, **kwargs) -> OptionsDefinition | None: ...
    @abstractmethod
    def __update__(self, game_objects: tuple[GameObject], parent_object: GameObject, **kwargs) -> OptionsDefinition | None: ...
