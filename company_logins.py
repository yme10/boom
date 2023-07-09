import tkinter
from tkinter import *

class Page:
  def __init__(self, window, title):
    self.window = window
    self.window.title(title)
    self.window.geometry("420x560")
    self.window.config(bg="off-white", state="zoomed")


def run():
  window = TK()
  Page(window)
  window.mainloop()


if __name__ == __main__:
  run()
