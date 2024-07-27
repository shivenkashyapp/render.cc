from rasterize import *

class Engine:
    def __init__(self, W: int = 400, H: int = 300) -> None:
        self.W = W ; self.H = H
        self.construct()


    def construct(self) -> None:
        self.screen = pg.display.set_mode((self.W, self.H), DOUBLEBUF)
        self.clock  = pg.time.Clock()

        # delta time for rotations and such.
        self.dt: float | int = 0.
        # frame cap
        self.fcap: float | int = 59.88

    def run(self) -> None:
        while (True):
            [pg.quit() for e in pg.event.get() if e.type == QUIT]; self.screen.fill(0x0)

            rasterize(self.screen, 0xff, Point2d(200, 10), Point2d(150, 200), Point2d(250, 200))

            pg.display.flip()
            self.dt = self.clock.tick(self.fcap)

if __name__ == "__main__":
    Engine().run()
