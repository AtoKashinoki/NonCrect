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

    def __init__(self):
        """ Initialize texture component """
        super().__init__()
        return

    def __render__(self, *args, game_object, **kwargs):
        return
