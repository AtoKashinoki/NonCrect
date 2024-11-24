"""
    Game loop test file.

This file test processes of game.
"""


""" imports """


from CodingTools2.Type import Vector1D
from CodingTools2.Errors import Exit
import pygame as pg
from NonCrect.GameObject import GameObject
from NonCrect.Component import ScriptSkeleton
from NonCrect.Type import Force

""" tester """


class Test(ScriptSkeleton):
    def __repr__(self):
        return "Script Test"
    def __script__(self, *args, game_object, **kwargs):
        self.transform.force = Force((1, 1))
        print(game_object.components.Transform)
        return
    ...


size = Vector1D([900, 600])
test_objects = [
    GameObject(Test())
    for _ in range(10)
]


def __update__(events: list[pg.event.Event]) -> int:
    [_object.__update__() for _object in test_objects]
    return 0


def mainloop():

    pg.init()
    pg.display.set_mode(size.data)

    done = False
    while not done:

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                done = True
                ...
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DELETE:
                    done = True
                    raise Exit()
                ...
            ...

        option = __update__(events)
        if 1 == option:
            done = True
            ...
        pg.display.update()
        ...

    return


if __name__ == '__main__':
    mainloop()
    ...
