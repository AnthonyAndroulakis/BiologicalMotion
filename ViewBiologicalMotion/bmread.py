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
    xlist=data[2:][::2] #every other plus first
    ylist=data[2:][1::2] #every other (without first)
    window.geometry(str(int(max(ylist)-min(ylist)+1000))+'x'+str(int(max(xlist)-min(xlist)+1000)))
    canvas = Canvas(window, bg = "black", height = int(max(ylist)-min(ylist)+800), width = int(max(xlist)-min(xlist)+800))
    canvas.pack()

    print("Press any key to start animation. Resize tkinter window if needed.")
    key = WaitForKey(any)
    frameIndex = 1;
    dotCount = 0;
    dotsPerFrame = data[0]
    numberFrames = data[1]

    xlist=data[2:][::2] #every other plus first
    ylist=data[2:][1::2] #every other (without first)

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

def display(txtfile,duration): #duration in ms
    unfiltered = list(filter(None, open(txtfile,"r").read().split('\n'))) #./BioMotion3/PointLight_Data/StreamingAssets/data_text_files/
    data = list(map(int, unfiltered))
    frameshow(data,duration) #duration is needed for fps, duration in ms

display(sys.argv[1])
