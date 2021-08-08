from utils import Color
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

class line:
    #def line(pen,startx,starty,endx,endy,thickness=0.2,color=Color.yellow):
   # pen.move_to(startx,starty)                                                 pen.set_source_rgb(*color)                                                 pen.set_line_width(thickness)
    #pen.line_to(endx,endy)
    #pen.stroke()
    #return pen
    pass

