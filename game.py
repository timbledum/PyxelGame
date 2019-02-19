import pyxel

from player import Player

width = 160
height = 96
assets = "assets\\resources.pyxel"



class Game():

    def __init__(self):
        pyxel.init(width, height, caption="Game Title", fps=60)
        self.player = Player()
        pyxel.load(assets)
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.player.move(-1)

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.player.move(1)

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.player.isJumping = True

    def draw(self):
        pyxel.cls(0)
        self.drawFloor()
        self.player.drawPlayer()

    def drawFloor(self):

        x = 0
        for i in range(0, int(width / 4 + 1)):
            pyxel.blt(x, height - 8, 0, 0, 40, 8, 8)
            x += 8


Game()


