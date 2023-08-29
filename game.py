import tkinter as tk
import random
import time

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.make_food()
        self.score = 0

        self.canvas.bind_all("<Key>", self.response)

        self.update()

    def make_food(self):
        # this function will create the food for the snake and using both x and y axis we will generate the food in random places and it will generate food at diffenent places every time
        x = random.randint(10, 390)
        y = random.randint(10, 390)
        return self.canvas.create_oval(x, y, x + 10, y + 10, fill="red")

    def response(self, event):
        # this function is to change the direction of the snake head and the rest of the body of the snake will follow the head direction so we have used different elif conditions to check the input that is giver by the player of the the snake game 
        new_direction = event.keysym
        if new_direction in ["Up", "Down", "Left", "Right"]:
            if (new_direction == "Up" and self.direction != "Down") or \
               (new_direction == "Down" and self.direction != "Up") or \
               (new_direction == "Left" and self.direction != "Right") or \
               (new_direction == "Right" and self.direction != "Left"):
                self.direction = new_direction

    def update(self):
        # in this function the size of the snake will increased once the food is eaten by the snake and the size will be increased at the tail part the head part will be at the same coordinate
        head_x, head_y = self.snake[0]
        new_head = None

        if self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)
        elif self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 10, head_y)

        self.snake.insert(0, new_head)

        if new_head == self.canvas.coords(self.food):
            self.score += 1
            self.canvas.delete(self.food)
            self.food = self.make_food()
        else:
            self.snake.pop()

        if (new_head[0] < 0 or new_head[0] > 390 or
            new_head[1] < 0 or new_head[1] > 390 or
            new_head in self.snake[1:]):
            self.canvas.create_text(200, 200, text="Game Over", font=("Helvetica", 20))
            return

        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tags="snake")

        self.canvas.create_text(50, 10, text=f"Score: {self.score}", anchor="nw", tags="score")

        self.root.after(100, self.update)

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
