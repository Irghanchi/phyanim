from utils import Color
import draw


posy = 3
vely = 0
g = -1
t = 0
image,pen=draw.init(640,360)
draw.line(pen,-5,-3,5,-3,color = Color.green)
draw.write(image,"../storage/shared/irfan.png")
def frame(fr):
    global posy,vely,t,image,pen
    dt = 5*(fr-t)
    t = fr
    draw.circle(pen,0,posy,radius = 0.4,color = Color.red)
    vely += g*dt
    posy += vely*dt
    print(dt)
    if posy < -3:
        posy = -3
        vely = -vely

    return draw.get_np_image(image,640,360)

draw.start_animation(frame)



