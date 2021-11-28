from utils import Color
class Shapes:
    objlist = []
    def __init__(self,x= 0,y= 0,color = Color.red):
        self.x = x
        self.y = y
        self.color = color
        Shapes.objlist.append(self)

    def move_to(self,pos):
        self.x = pos[0]
        self.y = pos[1]

    @classmethod
    def list_shapes(cls):
        return cls.objlist
    
    @property
    def pos(self):
        return [self.x,self.y]

class Arc(Shapes):
    def __init__(self,radius = 0.1,theta_i =0,theta_f= 2*3.14,color=Color.blue):
        super().__init__(color = color)
        self.radius = radius
        self.theta_i = theta_i
        self.theta_f = theta_f  



    @property
    def get_radius(self):
        return self.radius

    def draw(self,pen):
        pen.arc(self.x,self.y,self.radius,self.theta_i,self.theta_f)
        pen.set_source_rgb(*self.color)
        pen.fill()


class Circle(Arc):
    def __init__(self,radius = 0.1,color = Color.blue):
        super().__init__(radius = radius,color= color)

    def draw(self,pen):                     
        pen.arc(self.x,self.y,self.radius,0.0,2*3.14)                 
        pen.stroke_preserve()
        pen.set_source_rgba(*self.color)
        pen.fill()

class Rectangle(Shapes):
    def __init__(self,width=1.5,height=1,color=Color.black):
        super().__init__(color = color)
        self.width = width
        self.height = height


    def draw(self,pen):
        pen.rectangle(self.x-self.width/2,self.y-self.height/2,self.width,self.height)  
        pen.set_source_rgba(*self.color)     
        pen.fill()



class Square(Rectangle):
    def __init__(self,width=1.5,color=Color.blue):
        super().__init__(color = color)

    def draw(self):
        pen.rectangle(self.x-self.width/2,self.y-self.height/2,self.width,self.width)      
        pen.set_source_rgb(*self.color)     
        pen.fill()
        
class Line(Shapes):
    def __init__(self,posi,posf,thickness = 0.2,color = Color.yellow):
        super().__init__(color=color)
        self.ix = posi[0]
        self.iy = posi[1]
        self.fx = posf[0]
        self.fy = posf[1]
        self.thickness = thickness
    def draw(self,pen):
            #startx,starty,endx,endy,thickness=0.2,color=Color.yellow):
        pen.move_to(self.ix,self.iy)          
        pen.set_source_rgb(*self.color)          
        pen.set_line_width(self.thickness)
        pen.line_to(self.fx,self.fy)
        pen.stroke()
        return pen

    def move_sec_end(self,pos):
        self.fx = pos[0]
        self.fy = pos[1]


