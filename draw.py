import cairo 
from moviepy.editor import VideoClip
import math
from utils import Color
import numpy as np

def init(width,height):
    image = cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height)
    pen = cairo.Context(image)
    pen.translate(width/2,height/2)
    scalx = width/10
    scaly = -height/6
    rectangle(pen,0,0,width,height)
    pen.scale(scalx,scaly)
    return (image,pen)


def write(image,file_name):
    image.write_to_png(file_name)


def arc(pen,centx,centy,starttheta,endtheta,radius=50,color=Color.blue):
    pen.arc(centx,centy,radius,starttheta,endtheta)
    pen.set_source_rgb(*color)
    pen.fill()
    return pen

def circle(pen,centx,centy,radius=1,color=Color.blue):
    arc(pen,centx,centy,0,2*3.14,radius=radius,color=color)
    pen.fill()
    return pen



def rectangle(pen,centx,centy,width,height,color=Color.white):
    pen.rectangle(centx-width/2,centy-height/2,width,height)
    pen.set_source_rgb(*color)
    pen.fill()
    return pen

def square(pen,centx,centy,length,color = Color.blue):
    rectangle(pen,centx,centy,width,height,color = color)
    return pen

def line(pen,startx,starty,endx,endy,thickness=0.2,color=Color.yellow):
    pen.move_to(startx,starty)
    pen.set_source_rgb(*color)
    pen.set_line_width(thickness)
    pen.line_to(endx,endy)
    pen.stroke()
    return pen


def get_np_image(image,width,height):
    im= 0 + np.frombuffer(image.get_data(), np.uint8)
    im.shape = (height, width, 4)
    im = im[:, :, [2, 1, 0, 3]] 
    return im[:, :, :3] 


def start_animation(func,duration=5,path="../storage/shared/First_moviepy.mp4",fps= 30):
    clip = VideoClip(func,duration= duration)
    clip.write_videofile(path,fps)






    

