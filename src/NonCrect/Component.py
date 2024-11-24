"""
    NonCrect.Component

This file contain components for using in GameObject.
"""


""" imports """


from abc import ABC, abstractmethod
from CodingTools2.Definitions import Format
from NonCrect.ComponentSkeleton import ComponentSkeleton
from NonCrect.Definition import ComponentType
from NonCrect.Type import Position, Force


""" Components """


class NoneType(ComponentSkeleton):
    """ None """
    def __init__(self):
        super(NoneType, self).__init__(
            ComponentType.NoneType
        )
        return
    def __setup__(self, game_objects, parent_object, **kwargs): ...
    def __update__(self, game_objects, parent_object, **kwargs): ...

    ...


class Transform(ComponentSkeleton):
    """ Transform component """

    """ values """
    position: Position
    rotation: float
    scale: float
    mass: float
    force:  Force

    """ properties """

    """ processes """

    # instance
    def __init__(
            self,
            position: Position = Position(),
            rotation: float = 0.0,
            scale: float = 1.0,
            mass: float = 1.0,
            force: Force = Force(),
    ) -> None:
        super(Transform, self).__init__(
            ComponentType.Transform
        )
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.mass = mass
        self.force = force
        return

    def __repr__(self):
        return Format.repr_base.format(
            self.__class__.__name__,
            (self.position, self.rotation, self.scale, self.mass, self.force)
        )

    def __setup__(self, game_objects, parent_object, **kwargs): ...

    def __update__(self, game_objects, parent_object, **kwargs):
        """ Update position and rotation """
        self.position += self.force
        return

    ...


class ColliderSkeleton(ComponentSkeleton, ABC):
    """ Collider component """

    """ values """
    __parent_object = None

    """ properties """
    @property
    def transform(self) -> Transform:
        return self.__parent_object.components.Transform
    @transform.setter
    def transform(self, transform: Transform):
        self.__parent_object.components.transform = transform
        return

    """ processes """

    # instance
    def __init__(self):
        super(ColliderSkeleton, self).__init__(
            ComponentType.Collider
        )
        self.__parent_object = None
        return

    @abstractmethod
    def __setup__(self, game_objects, parent_object, **kwargs): ...

    @abstractmethod
    def __collider__(self, game_objects, parent_objects, **kwargs): ...

    def __update__(self, game_objects, parent_objects, **kwargs):
        """ Check collision """
        self.__parent_object = parent_objects
        self.__collider__(game_objects, parent_objects, **kwargs)
        return

    ...


class TextureSkeleton(ComponentSkeleton, ABC):
    """ Texture component """

    """ values """
    __parent_objects = None

    """ properties """
    @property
    def transform(self) -> Transform:
        return self.__parent_objects.components.Transform
    @transform.setter
    def transform(self, transform: Transform):
        self.__parent_objects.components.transform = transform
        return

    """ processes """

    # instance
    def __init__(self):
        super(TextureSkeleton, self).__init__(
            ComponentType.Texture
        )
        self.__parent_objects = None
        return

    @abstractmethod
    def __setup__(self, game_objects, parent_object, **kwargs): ...

    @abstractmethod
    def __render__(self, game_objects, parent_object, **kwargs): ...

    def __update__(self, game_objects, parent_object, **kwargs):
        self.__parent_objects = parent_object
        self.__render__(game_objects, parent_object, **kwargs)
        return

    ...


class ScriptSkeleton(ComponentSkeleton, ABC):
    """ Script component """

    """ values """
    __parent_object = None

    """ properties """
    @property
    def transform(self) -> Transform:
        return self.__parent_object.components.Transform
    @transform.setter
    def transform(self, transform: Transform):
        self.__parent_object.components.transform = transform
        return
    @property
    def collider(self) -> ColliderSkeleton:
        return self.__parent_object.components.collider
    @collider.setter
    def collider(self, collider: ColliderSkeleton):
        self.__parent_object.components.collider = collider
        return
    @property
    def texture(self) -> TextureSkeleton:
        return self.__parent_object.components.texture
    @texture.setter
    def texture(self, texture: TextureSkeleton):
        self.__parent_object.components.texture = texture
        return


    """ processes """

    # instance
    def __init__(self):
        super(ScriptSkeleton, self).__init__(
            ComponentType.Script
        )
        self.__parent_object = None
        return

    @abstractmethod
    def __setup__(self, game_objects, parent_object, **kwargs): ...

    @abstractmethod
    def __script__(self, game_objects, parent_object, **kwargs): ...

    def __update__(self, game_objects, parent_object, **kwargs):
        self.__parent_object = parent_object
        self.__script__(game_objects, parent_object, **kwargs)
        return

    ...

