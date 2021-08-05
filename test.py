from utils import  Color
import draw


posy = 3
vely = 0
g = -1

def anim_func(dt):
    global posy,vely,g
    image,pen=draw.init(640,360)
    draw.line(pen,-5,-3,5,-3,color = Color.green)
    draw.circle(pen,0,posy,radius = 0.4,color = Color.red)
    vely += g*dt
    posy += vely*dt
    if posy < -3:
        posy = -3
        vely = -vely
    return image

draw.make_animation(anim_func)



