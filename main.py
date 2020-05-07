from gui import *

window1 = python_GUI("test1")

spr1=shape("test",50,50,100,100,3)
window1.add_custom_sprite(spr1)



while 1:
    window1.tick()
