#!/usr/bin/python

import Tkinter
import time
import os
from PIL import ImageTk, Image

class ImagePanel:
  
  currentImage = 0
  panel = 0

  def Show(self, path):
    img = Image.open(path)
    # img = img.resize((200, 200), Image.ANTIALIAS)
    self.currentImage = ImageTk.PhotoImage(img)
    self.panel.config(image = self.currentImage)
    self.panel.pack(side="bottom", fill="both", expand="yes")
    self.panel.update()

  def __init__(self, parent):
    self.currentImage = None
    self.panel = Tkinter.Label(parent)


def ReadFileAsLines(path):
  with open(path) as f:
    lines = f.read().splitlines()
  return lines
