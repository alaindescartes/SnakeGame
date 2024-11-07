from turtle import Screen

from snakeClass import Snake


class GameScreen:
    def __init__(self, size = (500,500), bg_color = "black", title_color = "white", title = "Snake Game"):
        self.screen = Screen()
        self.size = size
        self.bg_color = bg_color
        self.title_color = title_color
        self.title = title
        self.setup_screen()
        self.screen.tracer(0)
        self.snake = Snake()
        self.change_direction()


    def setup_screen(self):
        """
                initializes the game screen

                parameter:
                size: size of the game screen
            """
        self.screen.setup(*self.size)
        self.screen.bgcolor(self.bg_color)
        self.screen.title(self.title)
        self.screen.listen()


    def change_direction(self):
        """
        binds direction keys to the snake
        """
        self.screen.onkey(lambda: self.snake.restrict_direction("UP"), "w")
        self.screen.onkey(lambda: self.snake.restrict_direction("DOWN"), "s")
        self.screen.onkey(lambda: self.snake.restrict_direction("LEFT"), "a")
        self.screen.onkey(lambda: self.snake.restrict_direction("RIGHT"), "d")



