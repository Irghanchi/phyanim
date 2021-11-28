from shapes import Rectangle,Circle,Line
from anim import Anim
import math as m
hook = Circle(0.2)
hook.move_to([0,3])
ball = Circle(0.5)
ball.move_to([3,-1])
length = 5
g = -2
omega = 0
acc = 0
theta = m.pi/4
rod = Line(hook.pos,ball.pos,thickness = 0.05)
def main(dt):
    global acc ,omega,g,length,ball,theta
    acc = g*m.sin(theta)/length
    omega += acc*dt
    theta += omega*dt
    x = length*m.sin(theta) - hook.pos[0] 
    y = -length*m.cos(theta) + hook.pos[1]
    ball.move_to([x,y])
    rod.move_sec_end(ball.pos)



ani = Anim()
ani.make_animation(main,5,fps = 60)
