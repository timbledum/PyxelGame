import pyxel

from player import Player

width = 160
height = 96
assets = "assets\\resources.pyxel"
player = Player()



class Game():

    def __init__(self):
        pyxel.init(width, height, caption="Game Title", fps=30)
        pyxel.load(assets)
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_LEFT):
            player.move(-1)

        if pyxel.btnp(pyxel.KEY_RIGHT):
            player.move(1)

    def draw(self):
        pyxel.cls(1)
        self.drawFloor()
        player.drawPlayer(player.xPos)

    def drawFloor(self):

        x = 0
        for i in range(0, int(width / 4 + 1)):
            pyxel.blt(x, height - 4, 0, 16, 0, 4, 4)
            x += 4


Game()


