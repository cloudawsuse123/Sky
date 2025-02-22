import tkinter as tk
import random

sky = tk.Tk()
sky.title("Sky Program")
# Set the window background to light blue
sky.configure(bg="black")
#set screen size 
sky.geometry("370x550")

#create a widgit and height using canvas 
canvas = tk.Canvas(sky, width=370, height=550, bg="black")
canvas.config(highlightthickness=1, highlightbackground="white")
canvas.pack()

#create function to draw a stars 
def draw_star(x, y):
  canvas.create_oval(x-2, y-2, x+2, y+2, fill="white")

#Draw 100 random stars
for _ in range(30):
    x = random.randint(0, 370)
    y = random.randint(0, 550)
    draw_star(x, y)

#Draw the moon
moon = canvas.create_oval(50, 50, 100, 100, fill="red")

#Run the main loop
sky.mainloop
