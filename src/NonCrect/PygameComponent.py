"""
    NonCrect.PygameComponent

This file contain components of pygame for using in NonCrect.
"""


""" imports """


import pygame
from NonCrect.Definition import ComponentType
from NonCrect.Component import (
    ColliderSkeleton, TextureSkeleton,
)


""" Components """


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

    def __render__(
            self,
            *args,
            game_object,
            **kwargs,
    ):
        master: pygame.Surface = kwargs["master"]
        master.blit(self.__surface__, self.transform.position.data)
        return
