from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            high_score = file.read()
        self.points = 0
        self.high_score = int(high_score)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Score: " + str(self.points) + " High Score: " +
                   str(self.high_score), move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Score: " + str(self.points) + " High Score: " +
                   str(self.high_score), move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("highscore.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.points = 0
        self.update_scoreboard()

