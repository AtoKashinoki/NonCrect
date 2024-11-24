"""
    Game loop test file.

This file test processes of game.
"""

""" imports """


from time import time
from CodingTools2.Type import Vector1D
from CodingTools2.Errors import Exit
import pygame
from NonCrect.GameObject import GameObject
from NonCrect.Component import ScriptSkeleton
from NonCrect.Type import Force
from NonCrect.PygameComponent import (
    Collider, Transform, Texture
)
from NonCrect.Type import Position

""" tester """


class Test(ScriptSkeleton):
    def __repr__(self):
        return "Script Test"
    def __setup__(self, game_objects, parent_object, **kwargs): ...
    def __script__(self, game_objects, parent_object, **kwargs):
        self.transform.force = Force((1, 1))
        return
    ...

class Test2(ScriptSkeleton):
    def __repr__(self):
        return "Script Test"
    def __setup__(self, game_objects, parent_object, **kwargs): ...
    def __script__(self, game_objects, parent_object, **kwargs):
        self.transform.force = Force((2, 1))
        return

    ...


size = Vector1D([900, 600])
surface = pygame.Surface((50, 50))
surface.fill((255, 255, 255))
test_objects = [
    GameObject(
        Texture(surface),
        Collider(),
        Transform(Position((200, 0))),
        Test()
    ),
    GameObject(
        Texture(surface),
        Collider(),
        Transform(Position((0, 0))),
        Test2()
    )
]


def __update__(master: pygame.Surface, events: list[pygame.event.Event]) -> int:
    [
        _object.__update__(
            test_objects,
            master=master, events=events
        )
        for _object in test_objects
    ]

    return 0

def __setup__(master: pygame.Surface, events: list[pygame.event.Event]) -> int:
    [
        _object.__setup__(
            test_objects,
            master=master, events=events
        )
        for _object in test_objects
    ]

    return 0


def mainloop():

    pygame.init()
    master = pygame.display.set_mode(size.data)
    pre_t = time()
    framerate = 30
    one_f_t = 1/framerate

    __setup__(master, [])

    done = False
    while not done:

        now_t = time()
        if now_t - pre_t < one_f_t:
            continue
        pre_t = now_t

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                done = True
                ...
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    done = True
                    raise Exit()
                ...
            ...

        master.fill("Black")
        option = __update__(master, events)
        if 1 == option:
            done = True
            ...
        pygame.display.update()
        ...

    return


if __name__ == '__main__':
    mainloop()
    ...
