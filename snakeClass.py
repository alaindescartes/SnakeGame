import turtle
from tkinter import TclError
from turtle import Turtle

import scoreBoard
from scoreBoard import Scoreboard
from snakeFood import Food


class Snake:
    def __init__(self, position=(0, 0), direction="UP", length=3, speed=500, color="white", is_alive=True):
        self.position = position
        self.direction = direction
        self.length = length
        self.speed = speed
        self.last_speed_increase_score = 0
        self.color = color
        self.is_alive = True
        self.segments = []
        self.screen = turtle.Screen()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.create_snake()
        if is_alive : self.move()

    def add_segment(self, position):
        """
        Creates a new segment and adds it to the snake's segments list.
        :param position : The (x, y) coordinates where the new segment should be placed.
        """
        segment = Turtle("square")
        segment.color(self.color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def create_snake(self):
        """
        Initializes the snake with the specified length by adding segments at offset positions.
        """
        x, y = self.position  # Starting position for the head
        for i in range(self.length):
            # Offset each new segment by 20 pixels to the left
            segment_position = (x - i * 20, y)
            self.add_segment(segment_position)

    def move(self):
        """
        Moves the snake in the specified direction by updating the position of each segment.

        This method updates each segment of the snake to follow the one in front of it,
        creating a smooth movement effect. The head segment moves in the specified direction
        (UP, DOWN, LEFT, RIGHT) with a set heading angle, and each subsequent segment
        moves to the previous position of the segment in front of it.

        Updates:
        - Adjusts the heading of the head segment based on the direction parameter.
        - Moves the head segment forward by a fixed distance.
        - Updates each subsequent segment to the position of the segment directly ahead,
          so the entire snake appears to follow the head in a continuous motion.
        """
        if not self.is_alive:
            return
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        head = self.segments[0]
        if self.direction == "UP":
            head.setheading(90)
        elif self.direction == "DOWN":
            head.setheading(270)
        elif self.direction == "LEFT":
            head.setheading(180)
        elif self.direction == "RIGHT":
            head.setheading(0)

        head.forward(20)
        head.getscreen().update()
        self.detect_collision()
        self.stay_in_window()

        if self.is_alive:
            try:
                head.getscreen().ontimer(self.move, self.speed)
            except TclError:
                print("Application closed successfully")


    def restrict_direction(self, new_direction):
       """
           avoids reversal of the snake direction.
           :param new_direction: the direction that the snake should change and keep.
       """
       if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
       elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
       elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
       elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def stay_in_window(self):
        """
        checks if the snake is inside the window, if not it wraps it on the opposite side.

        """
        # Get screen boundaries
        screen_width = self.screen.window_width()
        screen_height = self.screen.window_height()
        x_boundary = screen_width / 2
        y_boundary = screen_height / 2

        # Get the head segment's current position
        head = self.segments[0]
        x, y = head.xcor(), head.ycor()

        # Check if the head is out of bounds and set new position
        if x < -x_boundary:
            x = x_boundary  # Wrap to the right side
        elif x > x_boundary:
            x = -x_boundary  # Wrap to the left side

        if y < -y_boundary:
            y = y_boundary  # Wrap to the top
        elif y > y_boundary:
            y = -y_boundary  # Wrap to the bottom

        # Move the head to the wrapped position if it changed
        head.goto(x, y)
        self.position = (x, y)


    def grow(self):
        """
         Adds a new segment at the back of the snake
        """
        last_segment = self.segments[-1]
        new_position = last_segment.position()
        self.add_segment(new_position)

    def increase_speed(self):
        """
        Increases the speed of the snake by decreasing the delay,
        ensuring it doesn't go below the minimum speed threshold.
        """
        MIN_SPEED = 200  # Minimum allowed speed in milliseconds
        self.speed = max(self.speed - 30, MIN_SPEED)

    def change_speed(self):
        """
        Checks if the score is above certain thresholds and increases the speed of the snake.
        Ensures that speed increases only once per threshold.
        """
        thresholds = [5, 10, 20]  # Define the score thresholds
        for threshold in thresholds:
            if self.scoreboard.score >= threshold > self.last_speed_increase_score:
                self.increase_speed()
                self.last_speed_increase_score = threshold
        print("the speed is " + str(round(self.last_speed_increase_score, 2)))


    def detect_collision(self):
        #get the position of the head
        head = self.segments[0]
        #detect if collision had occurred with the food
        if head.distance(self.food.food) < 15 :
            self.food.delete_food()
            self.scoreboard.increase_score()
            #increase the length of the snake
            self.grow()
            self.food.create_food()

        #increase snakes speed as the score increases
        self.change_speed()

        #detect collision with tail
        tail = self.segments[-1]
        if tail.distance(head) < 15 :
            self.is_alive = False
            self.scoreboard.display_message("Game Over")
        #detect collision with the body
        for segment in self.segments[1:]:
            if segment.distance(head) < 15 :
                self.is_alive = False
                self.scoreboard.display_message("Game Over")
                break




