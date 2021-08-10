from utils import  Color
from anim import Anim
from shapes import Circle
import numpy as np


pos = np.array([0,3])
vel = np.array([0,0])
g = -1
gor = Circle(radius= 2,color = Color.red)

def anim_func(dt):
    global pos,vel,g,gor
    gor.move_to(0,pos)
    vel += g*dt
    pos += vel*dt
    if pos[1] < -3:
        pos[1] = -2.9
        vel[1] = -vel[1]
ani = Anim()
ani.make_animation(anim_func)



