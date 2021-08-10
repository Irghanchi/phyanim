from shapes import Circle
from anim import Anim
from utils import Color
import numpy as np

sun = Circle(radius = 0.7,color = Color.yellow)
earth = Circle(radius = 0.3,color = Color.blue)
pos = np.array([-3.0,0.0])
v = np.array([0.0,-.5])
earth.move_to(pos)
def main(dt):
    global sun,earth,pos,v  
    g = -1*pos/np.linalg.norm(pos)**2
    v += g*dt
    pos += v*dt
    earth.move_to(pos)

ani = Anim()
ani.make_animation(main,duration = 60)




