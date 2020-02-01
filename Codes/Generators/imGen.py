from tkinter import *
import json
import random

master = Tk()

w = Canvas(master, width=600, height=600)
w.pack()

with open("image1.json") as f:
	x=f.read()
x=json.loads(x)

if "mountain" in x:
	if x['mountain']['position']=="left":
		left_x,left_y=0+random.randint(0,30),70+random.randint(0,150)
	else:
		print("Not implemented yet")
	
	if x['mountain']['size']=="small":
		right_x,right_y=left_x+105+random.randint(0,10),left_y
		top_x,top_y=(left_x+right_x)//2+random.randint(0,7)-random.randint(0,7),left_y-80+random.randint(0,6)
	elif x['mountain']['size']=="big":
		right_x,right_y=left_x+195+random.randint(0,15),left_y
		top_x,top_y=(left_x+right_x)//2+random.randint(0,7)-random.randint(0,7),left_y-80+random.randint(0,6)
	else:
		print("Not implemented yet")

#print(left_x,left_y,top_x,top_y,right_x,right_y)
		
'''w.create_line(left_x,left_y,top_x,top_y,fill="brown")
w.create_line(top_x,top_y,right_x,right_y,fill="brown")
w.create_line(left_x,left_y,right_x,right_y,fill="brown")'''

w.create_polygon(left_x,left_y,top_x,top_y,right_x,right_y,fill="brown")

mainloop()