import os
from screen import Screen
from tqdm import tqdm



class Anim:
    def make_animation(self,func,duration=10,
            fps=30,
            videopath = "/data/data/com.termux/files/home/storage/shared/phyanivideos/",
            filename="none.mp4"):
        path= "/data/data/com.termux/files/home/tmp/"
        t = duration*fps    
        sc = Screen()
        dt = 0.1  
        filenum = 0
        dispsize = "1920x1080"
        os.chdir(path)
        for i in tqdm(range(t)):     
            func(dt)                        
            sc.draw_shapes() 
            sc.image.write_to_png(str(filenum).zfill(3)+".png")
            filenum += 1


        #os.chdir("/data/data/com.termux/files/home/storage/shared/phyanivideos/")


        os.system(f"ffmpeg -r {fps} -f image2 -s {dispsize} -i %03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p {videopath+filename} -loglevel quiet -y")

        os.system("rm *.png")


    ##def make_video():




