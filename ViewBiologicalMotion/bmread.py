#view Biological Motion txt files
#bmread.py

import os
import sys
from tkinter import *
from tkinter import messagebox

import screen
from screen import window
from screen import WaitForKey
from screen import WaitForTime
        
def create_circle(canvas, x, y, r):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill="white")

def frameshow(data):
    xlist=data[3:][::2] #every other plus first
    ylist=data[3:][1::2] #every other (without first)
    window.geometry(str(int(max(ylist)-min(ylist)+1000))+'x'+str(int(max(xlist)-min(xlist)+1000)))
    canvas = Canvas(window, bg = "black", height = int(max(ylist)-min(ylist)+800), width = int(max(xlist)-min(xlist)+800))
    canvas.pack()

    print("Press any key to start animation. Resize tkinter window if needed.")
    key = WaitForKey(any)
    frameIndex = 1;
    dotCount = 0;
    dotsPerFrame = data[0]
    numberFrames = data[1]
    duration = data[2]

    for j in range(len(xlist)):
        x = xlist[j]
        y = ylist[j]
        print("frame #"+str(frameIndex)+": "+str(x)+"x"+str(y))
        if (x != 0 and y != 0):
            create_circle(canvas, x, y, 4)
        dotCount = dotCount + 1
        if dotCount > dotsPerFrame-1:
            frameIndex = frameIndex + 1
            dotCount = 0
            key = WaitForTime(round(duration/numberFrames)) #sets fps
            canvas.delete("all")

def display(txtfile):
    unfiltered = list(filter(None, open(txtfile,"r").read().split('\n')))
    data = list(map(int, unfiltered))
    frameshow(data)

display(sys.argv[1])
