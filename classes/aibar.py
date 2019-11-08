from classes.bar import Bar


class AIBar(Bar):
    def __init__(self, pos, ball):
        super().__init__(pos)
        self.ball = ball

    def move(self):
        if self.ball.y + self.ball.height/2 > self.y + self.height/2:
            self.down()

        elif self.ball.y + self.ball.height/2 < self.y + self.height/2:
            self.up()
