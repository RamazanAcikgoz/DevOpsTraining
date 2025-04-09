from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        # Angela's version
        # with open("data.txt") as data:
        #   self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt", mode= "r") as highscore_file:
            new_highscore = highscore_file.read()
        self.write(f"Score: {self.score} High Score: {new_highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode= "w") as highscore_file:
                highscore_file.write(f"{self.highscore}")
            # Angela's version
            # with open("data.txt", mode= "w") as data:
            #   data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

