from pygame.constants import *
from point import *

import pygame as pg
pg.init()


# TODO: sort points if they aren't. 
# TODO: convert to one loop.
def rasterize(screen: pg.Surface, color, p1: Point2d, p2: Point2d, p3: Point2d, step: int | float = 1) -> None:
    p1, p2, p3 = y_sort(p1, p2, p3)
    p4 = Point2d(find(p1, p3, None, p2.y), p2.y)

    # a bend exists somewhere in the triangle.
    if p4 not in (p1, p2, p3):
        t1 = Triangle(p1, p2, p4, sort = True)
        t2 = Triangle(p3, p2, p4, sort = True)

    else:
        t1 = Triangle(p1, p2, p3)
        t2 = None

        if p1.y == p2.y:
            t1, t2 = t2, t1

    if t1 is not None:
        y = t1.p1.y
        while (y < t1.p3.y):
            y += step
            pg.draw.line(screen, color, (find(t1.p1, t1.p2, None, y), y), (find(t1.p1, t1.p3, None, y), y))

    if t2 is not None:
        y = t2.p3.y
        while (y > t2.p1.y):
            y -= step
            pg.draw.line(screen, color, (find(t2.p1, t2.p3, None, y), y), (find(t2.p2, t2.p3, None, y), y))
