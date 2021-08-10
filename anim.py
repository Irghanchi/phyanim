from screen import Screen
import cv2
from tqdm import tqdm


class Anim:
    def make_animation(self,func,duration=10,
            fps=30,                         
            path= "/data/data/com.termux/files/home/storage/shared/my_module.mp4"):  
        out = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'mp4v'),                         
                fps,(Screen.width,Screen.height))   
        t = duration*fps    
        sc = Screen()
        dt = 0.1                            
        for i in tqdm(range(t)):     
            func(dt)                        
            sc.draw_shapes()              
            image = sc.get_np_image(sc.image)                                           
            out.write(image)
        out.release()   
