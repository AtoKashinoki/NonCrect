
from abc import ABC, abstractmethod
from copy import deepcopy
from random import randrange
from pygame import Surface, Rect
import pygame as pg


class Object(ABC):

    position = None
    size = None
    rect = None
    movement = None
    __surface__ = None
    killing = False
    depth = None

    @property
    def center(self): return [p+s//2 for p, s in zip(self.position, self.size)]
    @center.setter
    def center(self, value): self.position = [c-s//2 for c, s in zip(value, self.size)]

    def __init__(self, position, size, depth = 1.):
        self.position = list(position)
        self.size = list(size)
        self.rect = Rect(position, size)
        self.movement = [0, 0]
        self.__surface__ = Surface(size)
        self.killing = False
        self.depth = depth
        return

    @abstractmethod
    def __start__(self, camera): ...

    @abstractmethod
    def __update__(self, key_pressed, delta_t, objects, camera): ...

    def __render__(self, master):
        master.blit(self.__surface__, self.position, self.depth)
        return

    def kill(self):
        self.killing = True
        return

    ...


class NoneType(Object):
    def __start__(self, camera): ...
    def __update__(self, key_pressed, delta_t, objects, camera): ...
    ...


class Afterimage(Object):

    alpha = None

    def __init__(self, position, size, time):
        super().__init__(position, size)
        self.__surface__.fill((0, 0, 0, 192))
        self.alpha = 192
        self.rm_alpha = self.alpha/(60*time)
        return

    def __start__(self, camera): ...
    def __update__(self, key_pressed, delta_t, objects, camera):
        self.__surface__.set_alpha(self.alpha)
        self.alpha -= self.rm_alpha
        if self.alpha <= 0:
            return False
        return True



class Charactor(Object):

    is_land = None
    dash_cool = None
    afterimages = None
    afterimage_cool = None
    death = None
    spawn = None
    spawn_c = None

    def __init__(self, pos_unit):
        super().__init__(
            [pos_unit[0]*50+10, (pos_unit[1]-12)*-50+10],
            (30, 30)
        )
        self.is_land = False
        self.dash_cool = 0
        self.afterimages = []
        self.afterimage_cool = 0
        self.death = False
        self.spawn = True
        self.spawn_c = 60
        return

    def __start__(self, camera): ...

    def __update__(self, key_pressed, delta_t, objects, camera):

        self.afterimages = [
            afterimage
            for afterimage in self.afterimages
            if afterimage.__update__(key_pressed, delta_t, objects, camera)
        ]

        if self.death:
            if len(self.afterimages) == 0: self.kill()
            return

        self.afterimage_cool -= delta_t
        if randrange(4) == 0:
            self.afterimage_cool -= delta_t
            ...

        if self.afterimage_cool < 0:
            self.afterimages.append(Afterimage(
                [
                    p+randrange(s-15+1)
                    for p, s in zip(self.position, self.size)
                ],
                (15, 15),
                0.4
            ))
            self.afterimage_cool = 0.02
            ...

        if self.spawn:
            self.spawn_c -= 1
            if self.spawn_c < 0:
                self.spawn_c = 60
                self.spawn = False
                ...
            return

        self.movement[0] = 0
        if key_pressed[pg.K_LEFT]:
            self.movement[0] -= 240*delta_t
            ...
        if key_pressed[pg.K_RIGHT]:
            self.movement[0] += 240*delta_t
            ...
        self.movement[1] += 35*delta_t

        if self.is_land:
            if key_pressed[pg.K_UP]:
                self.movement[1] = -480*delta_t
                self.is_land = False
                ...
            ...

        dash = False
        self.dash_cool -= 1
        if key_pressed[pg.K_LSHIFT] and self.dash_cool < 0 and not self.movement[0] == 0:
            dash = True
            self.dash_cool = 30
            ...

        lands = [
            obj
            for obj in objects
            if isinstance(obj, Land) or isinstance(obj, KillZone)
        ]

        for i in range(2):
            pre_pos = deepcopy(self.position)
            for _ in range(20 if i == 0 and dash else 1):
                self.position[i] += self.movement[i]
                self.rect[:2] = self.position
                for land in lands:
                    if self.rect.colliderect(land.rect):
                        if isinstance(land, KillZone):
                            [
                                self.afterimages.append(Afterimage(
                                    [
                                        p + randrange(s - 5)
                                        for p, s in zip(self.position, self.size)
                                    ],
                                    (5, 5),
                                    (randrange(14)+1)/10
                                ))
                                for _ in range(60)
                            ]
                            self.death = True
                        if self.position[i] < land.position[i]:
                            self.position[i] = land.position[i] - self.size[i]
                            if i == 1: self.is_land = True
                            ...
                        else:
                            self.position[i] = land.position[i] + land.size[i]
                            ...
                        self.movement[i] = 0
                        ...
                    continue

                continue

            if i == 0 and dash:
                if pre_pos[0] < self.position[0]:
                    p1, p2 = pre_pos, self.position
                    ...
                else:
                    p1, p2 = self.position, pre_pos
                self.afterimages.append(Afterimage(
                    [
                        p
                        for p, s in zip(p1, self.size)
                    ],
                    [p2[0]-p1[0]+30, 30],
                    0.05
                ))

                ...

            continue
        self.rect[:2] = self.position
        if self.movement[1] >= 1: self.is_land = False

        return

    def __render__(self, master: Surface):
        [afterimage.__render__(master) for afterimage in self.afterimages]
        if not self.death and not self.spawn:
            super().__render__(master)
        return

    ...


class Land(Object):

    render_f = None

    def __init__(self, land_unit):
        super().__init__(
            [land_unit[0]*50, (land_unit[1]-12)*-50],
            [s*50 for s in land_unit[2:]]
        )
        self.render_f = False
        return

    def __start__(self, camera):
        self.render_f = self.rect.colliderect(camera.rect)
        return

    def __update__(self, key_pressed, delta_t, objects, camera):
        self.render_f = self.rect.colliderect(camera.rect)
        return

    def __render__(self, master: Surface):
        if self.render_f: super().__render__(master)
        return

    ...


class KillZone(Land):
    def __init__(self, land_unit):
        super().__init__(land_unit)
        self.__surface__.fill("Red")
        return

    ...


class BackGroundRect(Object):
    alpha = None
    rm_alpha = None
    angle = None

    __base_surface__ = None
    base_position = None

    def __init__(self, camera):
        pos = [
            camera.position[0]-200+randrange(camera.size[0]+200),
            600
        ]
        side = randrange(50, 200)
        size = [side for _ in range(2)]
        super().__init__(
            pos, size,
            2
        )
        self.base_position = pos
        self.alpha = randrange(120, 240)
        self.__surface__.fill((0, 0, 0, 0))
        self.__base_surface__ = pg.Surface(size)
        self.__base_surface__.fill((191, 191, 191))
        self.__surface__.set_alpha(self.alpha)
        self.rm_alpha = 1
        self.angle = randrange(0, 360)
        return

    def __start__(self, camera): ...

    def __update__(self, key_pressed, delta_t, objects, camera):
        self.angle -= 1
        self.__surface__ = pg.transform.rotozoom(
            self.__base_surface__, self.angle, 1
        )
        self.__surface__.set_colorkey("Black")
        rect = self.__surface__.get_rect()
        self.base_position[1] -= 2
        self.position = [
            bp + ss//2 - rc
            for bp, ss, rc in zip(self.base_position, self.size, rect.center)
        ]
        self.alpha -= self.rm_alpha
        if not self.alpha > 0: return False
        self.__surface__.set_alpha(self.alpha)
        return True

    ...


class BackGround(Object):

    delta_ts = None
    gen_t = 0.1
    objects = None

    def __init__(self):
        super().__init__((0, 0), (0, 0))
        self.delta_ts = 0
        self.objects = []
        return

    def __start__(self, camera): ...

    def __update__(self, key_pressed, delta_t, objects, camera):
        self.delta_ts += delta_t
        if self.delta_ts > self.gen_t:
            self.objects.append(BackGroundRect(camera))
            self.delta_ts = 0
            ...
        self.objects = [
            obj
            for obj in self.objects
            if obj.__update__(key_pressed, delta_t, objects, camera)
        ]
        return

    def __render__(self, master: Surface):
        [obj.__render__(master) for obj in self.objects]
        return

    ...
