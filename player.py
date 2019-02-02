import pyxel


class Player():

    def __init__(self):
        pyxel.blt(0, 4, 0, 0, 0, 16, 16)
        self.xPos = 0
        self.yPos = 0
        self.velocityDirection = 1


    def drawPlayer(self, xPos):
        pyxel.blt(self.xPos, pyxel.height - 20, 0, 0, 0, self.velocityDirection * 16, 16, colkey=0)

    def move(self, direction):

        # Move left if direction == -1 (left) and pos is not 0
        if direction == -1:
            if self.xPos != 0:
                self.xPos -= 1
                self.velocityDirection = -1

        # Move right if direction == 1 (right) and pos is not = window width
        if direction == 1:
            if self.xPos != pyxel.width:
                self.xPos += 1
                self.velocityDirection = 1

