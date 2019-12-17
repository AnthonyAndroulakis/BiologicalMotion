#!/usr/bin/python

import tkinter
import time
import os

# Globals
window_width = 600
window_height = 400

# Private
last_key_released = ""

def TimerFired():
  global waitForTime
  waitForTime.set(waitForTime.get() + 1)
  pass


def WaitForTime(milliseconds):
  global waitForTime
  global window
  window.after(milliseconds, TimerFired)
  window.wait_variable(waitForTime)
  pass


def WaitForKey(key):
  global waitForVar
  global last_key_released

  last_key_released = None

  while True:
    window.wait_variable(waitForVar)
    window.update_idletasks()
    if isinstance(key, list):
      if last_key_released in key:
        return last_key_released
    elif key == any:
      return last_key_released
    else:
      if last_key_released == key:
        return last_key_released

  pass


def MainWindowEventHandler(event):
  global label
  global window
  global waitForVar
  global last_key_released

  waitForVar.set(waitForVar.get() + 1)
  last_key_released = event.keysym
  print("KeyRelease: "+last_key_released)


window = tkinter.Tk()
# tkinter
# window.attributes("-fullscreen", True)
# window.geometry("{}x{}".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.geometry(str(window_width) + 'x' + str(window_height))
window.configure(background='black')
window.bind_all('<KeyRelease>', MainWindowEventHandler)

waitForTime = tkinter.IntVar()
waitForVar = tkinter.IntVar()
