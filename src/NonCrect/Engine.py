

from time import time
import pygame as pg
from .objects import Object, Charactor, Land, KillZone, BackGround
from .Camera import Camera


lands_units = [
    (-1, 30, 1, 32),
] + [
    (0, 1, 24, 1),
    (10, 2, 5, 1),
    (11, 3, 3, 1),
    (25, 1, 5, 1)
]

spawn_point = (12, 5)

kill_units = [
    (18*i, -1, 18, 1)
    for i in range(5)
]


lands = [
    Land(rand_unit)
    for rand_unit in set(lands_units)
]

kills = [
    KillZone(kill_unit)
    for kill_unit in set(kill_units)
]

class Engine:
    fps = None
    size = None
    objects: list[Object] = None

    def __init__(self, fps = 60):
        self.fps = fps
        self.size = (900, 600)
        self.objects = [BackGround()] + lands + kills
        return

    def __start__(self, camera):
        [obj.__start__(camera) for obj in self.objects]
        return

    def __key_down__(self, key_event: pg.event.Event) -> int | None:
        return

    def __update__(self, events: list[pg.event.Event], delta_t, camera) -> int | None:
        for event in events:
            if event.type == pg.QUIT:
                return -1
            if event.type == pg.KEYDOWN:
                self.__key_down__(event.key)
                ...
            ...
        [obj.__update__(pg.key.get_pressed(), delta_t, self.objects, camera) for obj in self.objects]
        self.objects = [obj for obj in self.objects if not obj.killing]
        if not Charactor in map(type, self.objects):
            charactor = Charactor(spawn_point)
            self.objects.append(charactor)
            camera.set_target(charactor)
            ...

        return

    def __render__(self, camera):
        camera.fill("White")
        camera.__update__()
        [obj.__render__(camera) for obj in self.objects]
        pg.display.update()
        return

    def __mainloop__(self):

        one_ft = 1/self.fps
        pre_ft = time()

        camera = Camera(pg.display.set_mode(self.size))
        camera.set_target(self.objects[0])

        self.__start__(camera)

        done = False
        while not done:

            now_t = time()
            delta_t = now_t - pre_ft
            if delta_t < one_ft: continue
            pre_ft = now_t

            self.__render__(camera)
            op = self.__update__(pg.event.get(), one_ft, camera)

            if op is not None:
                match op:
                    case -1:
                        done = True
                    case -2:
                        break

            continue

        return

    def exe(self):
        pg.init()
        self.__mainloop__()
        pg.quit()
        return