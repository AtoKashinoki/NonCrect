"""
    NonCrect.GameObject

This file contain GameObject classes for using in NonCrect.
"""


""" imports """


from .DataClass import Components
from .ComponentSkeleton import ComponentSkeleton
from .Component import (
    NoneType,
    ColliderSkeleton,
    TextureSkeleton,
    Transform,
)
from .Definition import OptionsDefinition, ComponentType


""" GameObject skeleton """


class GameObject(ComponentSkeleton):
    """ GameObject base """

    """ values """
    __components: Components

    """ properties """
    @property
    def components(self) -> Components:
        return self.__components

    """ processes """

    # instance
    def __init__(self, *components: ComponentSkeleton) -> None:
        """ Set GameObject properties """
        super().__init__(
            ComponentType.GameObject
        )
        self.__components = Components(
            *component_types,
            *map(type, components),
        )
        self.__components.append(Transform())
        [
            self.__components.append(component)
            for component in components
        ]
        return

    def add_component(
            self, _component: ComponentSkeleton
    ) -> None:
        """ Add a component to the game object """
        self.__components.add_value_type(type(_component))
        self.__components.append(_component)
        return

    def __setup__(self, game_objects, parent_object = None, **kwargs): ...

    def __update__(self, game_objects, parent_object = None, **kwargs) -> set[OptionsDefinition]:
        """ Update GameObject components """
        options: set[OptionsDefinition | None] = set(
            component.__update__(
                game_objects, self, **kwargs
            )
            for component in sorted(
                self.__components.values(),
                key=lambda comp: comp.type.id,
            )
        )
        return options

    ...


component_types: tuple[type[ComponentSkeleton], ...] = (
    NoneType,
    ColliderSkeleton,
    Transform,
    GameObject,
    TextureSkeleton,
)
