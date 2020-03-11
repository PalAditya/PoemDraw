from tkinter import *
import json
import random
import os
import webbrowser
from PIL import Image

def save_as_png(canvas, fileName):
	canvas.postscript(file = fileName + '.eps') 
	img = Image.open(fileName + '.eps') 
	img.save(fileName + '.png', 'png')

master = Tk()

w = Canvas(master, width=400, height=400)
w.pack()

x = input()
x=json.loads(x)
# print(x)
# print("I'm doing this "+json.dumps(x))
# exit()

if "mountain" in x:
	if "left" in x['mountain']['position']:
		left_x,left_y=0+random.randint(0,30),70+random.randint(0,150)
	else:
		print("Not implemented yet")
	
	if x['mountain']['size']=="small":
		right_x,right_y=left_x+125+random.randint(0,10),left_y
		top_x,top_y=(left_x+right_x)//2+random.randint(0,7)-random.randint(0,7),left_y-80+random.randint(0,6)
	elif x['mountain']['size']=="big":
		right_x,right_y=left_x+165+random.randint(0,15),left_y
		top_x,top_y=(left_x+right_x)//2+random.randint(0,7)-random.randint(0,7),left_y-80+random.randint(0,6)
	else:
		print("Not implemented yet")

if "sea" in x:
	if x['sea']['position'] == "natural":
		sea_coordinates = (0, left_y, 400, 400)
	else:
		print("Not implemented yet")

w.create_polygon(left_x,left_y,top_x,top_y,right_x,right_y,fill="brown")
#TODO: Use sea-coordinate
w.create_rectangle(0, left_y, 400, 400, fill = "blue")

#TODO: Randomize
if "right" in x['mountain']['position']:
	w.create_polygon(310,left_y,345,top_y-10,400,right_y,fill="brown")

master.update()
save_as_png(w, "k")
master.bind("<Escape>",lambda q:master.destroy())
master.mainloop()
os.remove('k.eps')
webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("k.png")

if len(x['mountain']['position']) == 1:
	print(1)
else:
	print(2)