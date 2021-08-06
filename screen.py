import cairo
from shapes import Shapes, Rectangle
import numpy as np
class Screen:
    width = 640
    height = 360
    def __init__(self):
        self.width = Screen.width
        self.height = Screen.height
        self.image = cairo.ImageSurface(cairo.FORMAT_ARGB32,self.width,self.height)
        self.pen = cairo.Context(self.image)
        self.pen.translate(self.width/2,self.height/2)
        scalx = self.width/10
        scaly = -self.height/6
        screen=Rectangle(width=self.width,height=self.height)
        screen.draw(self.pen)
        self.pen.scale(scalx,scaly)
        #del Shapes.objlist[0]

    def write_to_png(self,path):
        self.image.write_to_png(path)

    def draw_shapes(self):
        for i in reversed(Shapes.objlist):
            i.draw(self.pen)
            print(i)

    def get_np_image(self,image):
        im= 0 + np.frombuffer(image.get_data(), np.uint8)
        im.shape = (self.height, self.width, 4)
        im = im[:, :, [2, 1, 0, 3]]
        return im[:, :, :3]
