"""
    NonCrect.DataClass

This file contain data classes for using in GameObject class.
"""


""" imports """


from typing import ValuesView
from CodingTools2.Inheritance import DataClass
from .ComponentSkeleton import ComponentSkeleton
from .Component import (
    Transform,
    ScriptSkeleton,
    ColliderSkeleton,
    TextureSkeleton,
)
from .Definition import ComponentType


""" Component """


class Components(DataClass):
    """ Component data class """

    """ values """
    Transform: Transform
    Collider: ColliderSkeleton
    Script: ScriptSkeleton
    GameObject: ComponentSkeleton
    Texture: TextureSkeleton

    """ processes """

    # instance
    def __init__(
            self, *_component_types: type[ComponentSkeleton]
    ):
        """ Initialize and add value """
        super().__init__()
        [
            ComponentType.add_value_type(_type)
            for _type in _component_types
        ]
        return

    def append(self, value: ComponentSkeleton) -> 'Components':
        """ Append component """
        for c_type in ComponentType.value_types:
            if isinstance(value, c_type):
                setattr(self, value.type.name, value)
                break
            continue
        return self

    def values(self) -> ValuesView[ComponentSkeleton]:
        return super().values()

    ...
