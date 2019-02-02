import pyxel

groundHeight = 54


class Player():

    def __init__(self):
        pyxel.blt(0, 4, 0, 0, 0, 16, 16)
        self.xPos = 0
        self.yPos = groundHeight
        self.velocityDirection = 1
        self.isMoving = False
        self.isJumping = False

    def drawPlayer(self):
        if self.isJumping:
            while self.yPos >= (groundHeight - 30):
                pyxel.blt(self.xPos, self.yPos, 0, 0, 0, self.velocityDirection * -1 * 47, 34, colkey=0)
                self.yPos -= 1

            while self.yPos < groundHeight:
                pyxel.blt(self.xPos, self.yPos, 0, 0, 0, self.velocityDirection * -1 * 47, 34, colkey=0)
                self.yPos += 1

            self.isJumping = False

        else:
            pyxel.blt(self.xPos, groundHeight, 0, 0, 0, self.velocityDirection * -1 * 47, 34, colkey=0)




    def move(self, direction):

        # Move left if direction == -1 (left) and pos is not 0
        if direction == -1:
            if self.xPos != 0:
                self.xPos -= 1
                self.velocityDirection = -1

        # Move right if direction == 1 (right) and pos is not = window width
        if direction == 1:
            if self.xPos != pyxel.width-16:
                self.xPos += 1
                self.velocityDirection = 1





