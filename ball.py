import math
import numpy as np

class Ball:

    def __init__(self, canv, x, y, radius, dx, dy, color):
        self.canv = canv
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.color = color
        self.object = canv.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)
        

    def move(self):
        self.canv.move(self.object, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        

    def check_glue_to_wall(self, wall):
        if wall[1] is None and abs(self.x - wall[0]) <= self.radius:
            if wall[0] < self.x and self.dx <= 0:
                self.dx = 5
            if wall[0] > self.x and self.dx >= 0:
                self.dx = -5

        if wall[0] is None and abs(self.y - wall[1]) <= self.radius:
            if wall[1] < self.y and self.dy <= 0:
                self.dy = 5
            if wall[1] > self.y and self.dy >= 0:
                self.dy = -5

        

    def collide_with_wall(self, wall):
        if wall[1] is None and abs(self.x - wall[0]) <= self.radius:
            return True

        if wall[0] is None and abs(self.y - wall[1]) <= self.radius:
            return True

        return False

    def bounce_off_wall(self, wall):
        if wall[1] is None:
            self.dx *= -1
        else:
            self.dy *= -1
        return

    def collide_with_ball(self, other_ball):
        if math.sqrt((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2) <= (self.radius + other_ball.radius):
            return True
        return False

    def bounce_off_ball(self, other_ball):
        v1 = [self.dx, self.dy]
        v2 = [other_ball.dx, other_ball.dy]

        if self.x != other_ball.x:
            fi = -math.atan((self.y - other_ball.y)/(self.x - other_ball.x))

            a_matrix = [
                [math.sin(fi), math.cos(fi)],
                [-math.cos(fi), math.sin(fi)]
            ]

            v1_star = np.matmul(a_matrix, v1)
            v2_star = np.matmul(a_matrix, v2)

            dy = v2_star[1]
            v2_star[1] = v1_star[1]
            v1_star[1] = dy

            at_matrix = np.transpose(a_matrix)

            v1 = np.matmul(at_matrix, v1_star)
            v2 = np.matmul(at_matrix, v2_star)
        else:
            dy = v2[1]
            v2[1] = v1[1]
            v1[1] = dy

        self.dx, self.dy = v1
        other_ball.dx, other_ball.dy = v2

        return
