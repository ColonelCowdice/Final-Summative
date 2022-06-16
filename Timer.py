import time
import tkinter
from tkinter import *
from tkinter import messagebox
import Scores
from Scores import *
import GameBot

root = Tk()
root.geometry("100x50")

w = Label(root, text=':(', font="50")
w.pack()

# countdown timer
def countdown(t):
    while t:
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line
      time.sleep(1)
      t -= 1
      while timer == 0:
        if twentyfortyeightscore < TetrisScore:
          messagebox.showerror("Oh No!", "The 2048 player lost")
          print("2048 Loss")
        elif twentyfortyeightscore > TetrisScore:
          messagebox.showerror("Oh No!", "The tetris player lost")
          print("Tetris Loss")
t = input("Enter the time in seconds: ")

countdown(int(t))
