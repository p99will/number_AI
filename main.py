from gui import *
import os,sys
windowsize = (300,350)

window1 = python_GUI("test1",windowsize)

box_num=10
boxes = []
box_size = windowsize[0] / box_num

AI_TRAIN = True

ai_input=[]

def save_number(data,number):
    pass

def clicked_box(obj):
    obj.color=colors.green
    obj.thickness=0
    obj.highlighted=True

def clicked_button1(obj):
    for i in boxes:
        is_highlited=0
        if hasattr(i, 'highlighted'):
            if (i.highlighted):
                is_highlited=1
        ai_input.append(is_highlited)
    if AI_TRAIN:
        num = input("What Number is this?: ")

for y in range(box_num):
    for x in range(box_num):
        box=shape("Box"+str(x)+':'+str(y),box_size*x,box_size*y,box_size,box_size,1)
        box.onclick=clicked_box
        boxes.append(box)


button1 = shape("Button1",0,300,50,50,0,colors.blue)
button1.onclick=clicked_button1
window1.add_custom_sprite(button1)

for i in boxes:
    window1.add_custom_sprite(i)


while 1:
    window1.tick()
