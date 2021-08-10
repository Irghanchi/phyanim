from utils import  Color
from anim import Anim
from shapes import Circle


posy = 3
vely = 0
g = -1
gor = Circle(radius= 2,color = Color.red)

def anim_func(dt):
    global posy,vely,g,gor
    gor.move_to(0,posy)
    vely += g*dt
    posy += vely*dt
    if posy < -3:
        posy = -3
        vely = -vely
ani = Anim()
ani.make_animation(anim_func)



