import cairo 
import math
from utils import Color
import numpy as np
import cv2

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


def get_np_image(image):
    im= 0 + np.frombuffer(image.get_data(), np.uint8)
    im.shape = (image.get_height(), image.get_width(), 4)
    im = im[:, :, [2, 1, 0, 3]] 
    return im[:, :, :3] 


def make_animation(func,duration=10,fps=30,path= "/data/data/com.termux/files/home/storage/shared/my_module.avi"):
    out = out = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'h264'),fps,(640,360))

    t = duration*fps
    dt = 0.1
    for i in range(t):
        image = get_np_image(func(dt))
        out.write(image)
    out.release()


class Shapes:
    objlist = []
    def __init__(self,radius= 0,width = 0,height = 0,starttheta=0,endtheta= 0,color=Color.blue):
        self.radius = radius  
        self.width = width
        self.height = height
        self.startheta = starttheta         
        self.endtheta = endtheta
        self.color  = color
        self.x = 0
        self.y = 0
        Shapes.objlist.append(self)

    def move_to(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def list_shapes(cls):
        return cls.objlist
    
    @property
    def get_pos(self):
        return (self.x,self.y) 

class Arc(Shapes):
    def __init__(self,radius = 0.1,starttheta=0,endtheta= 2*3.14,color=Color.blue):
        super().__init__(radius= radius,starttheta = starttheta,color = color)


    @property
    def get_radius(self):
        return self.radius

    def draw(self,pen):
        pen.arc(self.x,self.y,self.radius,self.starttheta,self.endtheta)
        pen.set_source_rgb(*self.color)
        pen.fill()


class Circle(Arc):
    def __init__(self,radius = 0.1,color = Color.blue):
        super().__init__(radius = radius,color= color)

    def draw(self,pen):                     
        pen.arc(self.x,self.y,self.radius,0.0,2*3.14)                
        pen.set_source_rgb(*self.color)     
        pen.fill()

class Rectangle(Shapes):
    def __init__(self,width=1.5,height=1,color=Color.white):
        super().__init__(width = width,height = height,color = color)


    def draw(self,pen):
        pen.rectangle(self.x-self.width/2,self.y-self.height/2,self.width,self.height)  
        pen.set_source_rgb(*self.color)     
        pen.fill()



class Square(Rectangle):
    def __init__(self,width=1.5,color=Color.blue):
        super().__init__(width=width,color = color)
    

class Screen:
    def __init__(self,width,height):
        self.image = cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height)                
        self.pen = cairo.Context(self.image)     
        self.pen.translate(width/2,height/2) 
        scalx = width/10                    
        scaly = -height/6                   
        screen=Rectangle(width=width,height=height)
        screen.draw(self.pen)
        self.pen.scale(scalx,scaly)

    def write_to_png(self,path):
        self.image.write_to_png(path)

    def draw_shapes(self):
        for i in Shapes.objlist:
            i.draw(self.pen)


    def get_np_image(self,image):
        im= 0 + np.frombuffer(image.get_data(), np.uint8)
        im.shape = (self.height, self.width, 4)
        im = im[:, :, [2, 1, 0, 3]]         
        return im[:, :, :3]


    def make_animation(self,func,duration=10,fps=30,path= "/data/data/com.termux/files/home/storage/shared/my_module.avi"):                  
        out = out = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'h264'),fps,(self.width,self.height)) 
        t = duration*fps
        dt = 0.1                            
        for i in range(t):                  
            image = get_np_image(func(dt))  
            out.write(image)
        out.release()
        






ctd = Screen(640,360)
gor = Circle(radius= 0.5)
rect = Rectangle(width=1,height=1,color=Color.green)
rect.move_to(-5,3)


ctd.draw_shapes()
ctd.write_to_png("../storage/shared/do1.png")






    

