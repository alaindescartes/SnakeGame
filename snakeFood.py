from turtle import Screen, Turtle, position
import random
class Food:
    def __init__(self):
        self.screen = Screen()
        self.food = Turtle()
        self.create_food()
        self.position = None

    def create_food(self):
        """
        Create a random food

        """
        # Get the screen dimensions
        screen_width = self.screen.window_width()
        screen_height = self.screen.window_height()

        # Calculate random x and y coordinates within screen boundaries
        x = random.randint(-screen_width // 2 + 20, screen_width // 2 - 20)
        y = random.randint(-screen_height // 2 + 20, screen_height // 2 - 20)

        # Move the food to the new random position
        self.food.penup()
        self.food.hideturtle()
        self.food.goto(x, y)
        self.food.dot(20, "red" )
        self.position = (x, y)

    def delete_food(self):
        """
        Delete a random food
        """
        self.food.reset()
