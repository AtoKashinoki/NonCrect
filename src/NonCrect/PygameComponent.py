"""
    NonCrect.PygameComponent

This file contain components of pygame for using in NonCrect.
"""


""" imports """


import pygame
from CodingTools2.Definitions import Index
from NonCrect.Component import (
    ColliderSkeleton,
    Transform as NCTransform,
    TextureSkeleton,
)
from NonCrect.GameObject import GameObject


""" Components """


class Collider(ColliderSkeleton):
    """ Pygame collider """

    """ values """

    """ properties """

    """ processes """
    def __setup__(self, game_objects, parent_object, **kwargs): ...

    def __collider__(self, game_objects, parent_object, **kwargs):
        return

    ...


class Transform(NCTransform):
    """ Pygame transform """

    @staticmethod
    def __check_collision(
            _targets: tuple[GameObject, ...],
            _parent_object: GameObject,
            _self_rect: pygame.Rect,
    ) -> pygame.Rect | None:
        """ Return collision """

        for _target in _targets:

            if Collider not in map(type, _target.components.values()):
                continue
            elif _target == _parent_object:
                continue
            target_transform = _target.components.Transform
            target_rect = pygame.Rect(*target_transform.position, 50, 50)
            if _self_rect.colliderect(target_rect):
                return target_rect

            continue

        return

    def __update_pos(
            self,
            i: int,
            game_objects: tuple[GameObject],
            parent_object: GameObject,
    ) -> None:
        if i == Index.X:
            self.position += (self.force.x, 0)
            ...
        else:
            self.position += (0, self.force.y)
            ...

        # noinspection PyTypeChecker
        self_rect = pygame.Rect(*self.position, 50, 50)
        collide_rect = self.__check_collision(
            game_objects, parent_object, self_rect
        )
        if collide_rect is not  None:
            if self.force[i] > 0:
                diff = collide_rect[i] - self_rect.w
                ...
            else:
                diff = collide_rect[i] + collide_rect.w
                ...
            self.position[i] = diff
            ...
        return


    def __setup__(self, game_objects, parent_object, **kwargs): ...


    def __update__(self, game_objects, parent_object, **kwargs):
        """ Update position """
        if Collider not in map(
                type, parent_object.components.values()
        ):
            super().__update__(game_objects, parent_object, **kwargs)
            return

        self.__update_pos(Index.X, game_objects, parent_object)
        self.__update_pos(Index.Y, game_objects, parent_object)

        return


class Texture(TextureSkeleton):
    """ Pygame texture """

    """ values """
    __surface__: pygame.Surface = None

    """ properties """

    """ processes """

    def __init__(self, _surface: pygame.Surface = None):
        """ Initialize texture component """
        super().__init__()

        if _surface is not None:
            self.__surface__ = _surface
            ...

        return

    def __setup__(self, game_objects, parent_object, **kwargs): ...

    def __render__(
            self,
            game_objects,
            parent_object,
            **kwargs,
    ):
        master: pygame.Surface = kwargs["master"]
        master.blit(self.__surface__, self.transform.position.data)
        return

    ...
