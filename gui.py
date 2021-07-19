import pygame as pg

STEP = 18

# images address
IMA = "./images/"


class GUI:

    def __init__(self, action, n):
        self.action = action
        self.n = n
        display_h = n*36
        display_w = n*36
        pg.init()
        self.clk = pg.time.Clock()
        self.gd = pg.display.set_mode((display_w, display_h))
        self.assets = {
            "map": pg.image.load(IMA + "MAP.png"),
            "1": pg.image.load(IMA + "1.png"),
            "0": pg.image.load(IMA + "0.png")
        }
        self.Map = self.assets["map"]
        self.one = self.assets["1"]
        self.zero = self.assets["0"]
        self.run()

    def go_next(self):
        if(self.frame < len(self.action)-1):
            self.frame += 1
        if(self.frame == len(self.action)-1):
            self.paused = True

    def go_prev(self):
        if(self.frame > -1):
            self.frame -= 1

    def run(self):

        self.paused = True
        self.running = True
        self.frame = -1

        delay = 0.0

        while(self.running):

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.go_prev()
                        self.paused = True
                        break
                    if event.key == pg.K_d:
                        self.go_next()
                        self.paused = True
                        break
                    if event.key == pg.K_SPACE:
                        self.paused = not self.paused
                        break
                    if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                        self.running = False
                        break
                if event.type == pg.QUIT:
                    self.running = False
                    break

            self.draw(self.frame)
            delay += self.clk.tick(60)

            ANIM_DELAY = 500

            if(delay >= ANIM_DELAY):
                delay -= ANIM_DELAY
                if(not self.paused):
                    self.go_next()

        pg.quit()

    def draw(self, i):
        L = 10
        F = 10
        self.gd.blit(self.Map, (0, 0))
        for k in range(self.n):
            for j in range(self.n):
                if(self.action[i][j][k] == "1"):
                    one = self.assets["1"]
                    self.gd.blit(one, (L + k * 36, F + j * 36))
                if(self.action[i][j][k] == "0"):
                    zero = self.assets["0"]
                    self.gd.blit(zero, (L + k * 36, F + j * 36))
        pg.display.update()
