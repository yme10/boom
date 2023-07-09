import tkinter
from tkinter import *

class Page:
  def __init__(self, window, title):
    self.window = window
    self.window.title(title)
    self.window.geometry("420x560")
    self.window.config(bg="white")


def main():
  run()

def run():
  window = TK()
  Page(window, "Home")
  window.mainloop()


if __name__ == "__main__":
  main()
