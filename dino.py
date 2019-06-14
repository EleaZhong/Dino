import tkinter as tk
import random
import time
from PIL import Image, ImageTk
import random
import os
import math

class Dino():
    def __init__(self):
        self.img = []
        self.img.append(ImageTk.PhotoImage(Image.open( os.path.join(FILEPATH,'assets/left.gif'))))
        self.img.append(ImageTk.PhotoImage(Image.open(os.path.join(FILEPATH,'assets/right.gif'))))
        self.jump = ImageTk.PhotoImage(Image.open(os.path.join(FILEPATH,'assets/jump.gif')))
        self.dead = ImageTk.PhotoImage(Image.open(os.path.join(FILEPATH,'assets/stop.gif')))
        #Image.open(path).show()
        self.lastc = 0
        self.now = 0
        self.image = w.create_image(100,height-37,image=self.img[self.now])
        
        self.if_other_status = False
        self.h_indicator = w.create_text(100,26,text = '',font = 'Minecraftia 12',fill='#535353')
        self.dino_h = 0
        self.h_circle = w.create_oval(100-self.dino_h,18-self.dino_h,100+self.dino_h,18+self.dino_h,outline='black')
        self.lil_loop()
        #self.go_higher()
        self.height_loop()
    def lil_loop(self):
        global w
        if not self.if_other_status:
            d = {0:1,1:0}
            self.now = d[self.now]
            #print(self.now)
            w.itemconfigure(self.image,image=self.img[self.now])
        w.after(100,self.lil_loop)
    def height_loop(self):
        h = w.coords(self.image)
        
        if h:
            h = h[1]
        else:
            h = height-44
        #print(h)
        self.dino_h = -h
        if self.dino_h>=0:
            w.delete(self.h_circle)
            c = self.dino_h/120
            c = math.log2(self.dino_h)
            c = 15-c
            #if c>=20 : c=20
            self.h_circle = w.create_oval(100-c,14-c,100+c,14+c,outline='#535353')
        else:
            c = 0
            w.delete(self.h_circle)
        
        w.move(self.h_indicator,0,c-self.lastc)
        #print(c-self.lastc)
        #print(c,self.lastc)
        self.lastc = c
        if h <=0:
            
            h_txt = '+ '+str(int(height-44-h))+' m.'
            w.itemconfigure(self.h_indicator,text = h_txt)
        else:
            if self.h_indicator > 0:
                w.itemconfigure(self.h_indicator,text = '')
        
        l.after(10,self.height_loop)
    def go_higher(self):
        h = w.coords(self.image)
        if h: h = h[1]
        else: h = height-44
        if h<=200:
            w.move(self.h_circle,0,-h-self.lastc)
            self.lastc = -h

        w.after(10,self.go_higher)
    def jump_status(self):
        self.if_other_status = True
        w.itemconfigure(self.image,image=self.jump)
    def dead_status(self):
        self.if_other_status = True
        w.itemconfigure(self.image,image=self.dead)
    def kill_other_status(self):
        self.if_other_status = False
    def get_item_num(self):
        return self.image

class Clouds():
    def __init__(self):
        path = os.path.join(FILEPATH,'assets/cloud.gif')
        cloudimage = ImageTk.PhotoImage(Image.open(path))
        w.cloud = cloudimage
        self.clouds = []

        self.counter = 100
        print('')
        self.loop()
    def add(self):

        num = w.create_image(width,random.randint(20,height-230),image = w.cloud)
        w.tag_lower(num)
        self.clouds.append(num)

    def move(self):
        pops = []
        for num,c in enumerate(self.clouds):
            w.move(c,-1,0)
            pops =[]
            coords = w.coords(c)           
            if coords[0]<-50:
                pops.append((num,c))
        number = 0
        for num,c in sorted(pops): 
            
            w.delete(c)
            self.clouds.pop(num-number)
            
            number+=1



    def loop(self):
        if not if_dead:
            self.move()
            self.counter+=1
            if self.counter >= 100:
                cloud_num = len(self.clouds)
                if cloud_num in (2,3): cloud_num = 3
                rd = random.randint(0,0+cloud_num*150)<=0
                if rd and cloud_num<=6: 
                    self.add()
                    self.counter = 0
                
        else:
            self.clouds = []

        w.after(10,self.loop)
        pass





class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='100x20+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        self.if_full = True
        root.wm_attributes('-fullscreen','true')
        root.attributes("-topmost", True)
        master.bind('<Escape>',self.tg_g)            
    def tg_g(self,event):
        if self.if_full:
            self.master.wm_attributes('-fullscreen','false')
            self.master.attributes("-topmost", False)
            self.master.destroy()
            









move_counter = 0
def move():
    global w,text,accleration,speed,in_air,dino,time_lapse,move_counter
    x,y = w.coords(text)
    if height-44-y < speed:
        w.move(text,0,height-44-y)
        speed = 0
        accleration = 0
        in_air = False
        print(move_counter)
        move_counter = 0
        if time_lapse-time.time()>=-0.1 and (not auto):
            
            jump_timer()
    #else:
    w.move(text,0,speed)
    if accleration == 0:
        in_air = False
        dino.kill_other_status()
    #w.move(text,0,speed)
    speed+=accleration
    if accleration != 0:
        move_counter+=1
    move_obastacle()
    
    move_objects()
    
cb_count = 0

can_do = False
ct = 0

button = ''
time_lapse = 0
def jump_timer():
    global speed,accleration,in_air,dino,s_mp,time_lapse

    if if_dead:
        restart(0)
        return 0
    if not in_air:
        speed -= 13
        accleration = 0.8
        dino.jump_status()
    else:
        time_lapse = time.time()
        #print(time_lapse)
        speed -= 0

def jump_timer_down():
    global can_do,in_air,accleration,s_mp,time_lapse
    if if_dead:
        return 0
    can_do = True
    in_air = True
    accleration = 1.3#+s_mp/10
    

timer = time.time()

def speed_multiplier():
    global s_mp,score
    s_mp = (time.time() - timer)/15
    tp = s_mp**2*100
    score = int(s_mp*150+tp)
    #print(tp)
    #print(s_mp)
    l.after(50,speed_multiplier)

def fly_up(event):
    pass

     

def random_obstacle():
    global w,obstacles
    if_make = random.randint(1,5)<=3
    if if_make:
        if_make = random.randint(0,8) <= int(s_mp)
        #print(int(s_mp+1)/9,s_mp,if_make)
        if if_make :#and (not auto):
            rd = random.randint(0,4)
            o = w.create_image(width+30,height-35,image=w.exp[rd])
            
            obstacles.append(o)
            
        rd = random.randint(0,4)
        o = w.create_image(width,height-35,image=w.obs[rd])
        obstacles.append(o)


def random_birb():
    global w,obstacles
    if_make = random.randint(0,7)<=5
    if if_make:
        #rd = random.randint(0,3)
        #o = w.create_image(width,height-35,image=w.obs[rd])
        rd = random.randint(height-100,height-30)
        o = w.create_oval(width,rd,width+10,rd+10)
        obstacles.append(o)
   
       

def move_obastacle():
    global obstacles,s_mp
    pops = []
    for num,o in enumerate(obstacles):
        o_speed = -6-(s_mp)
        if o_speed <= -14: o_speed=-14
        w.move(o,o_speed,0)
        coord = []
        c =  w.coords(o)
        #print(obstacles)
        #print(s_mp)
        if c[0]<-70:
            #print(num,o,w.bbox(o))
            pops.append((num,o))
        if c[0]<=(110+60+20*(s_mp)) and c[0]>=110 and auto:
            
            jump_timer()

            jump_timer_down()
    number = 0
    for num,o in sorted(pops):
        
        w.delete(o)
        

        obstacles.pop(num-number)
        number+=1


def move_objects():
    global floor,s_mp
    pops = []
    for num,obj in enumerate(floor):
        o_speed = -6-(s_mp)
        if o_speed <= -14: o_speed=-14
        w.move(obj,o_speed,0)
        c =  w.coords(obj)
        if c[0]<-(6+s_mp)*10:
            pops.append([num,obj])
            w.delete(obj)
            floor.pop(num)
            '''
    for num,obj in pops:
        print('dells')
        print(num,obj)
        w.delete(obj)
        print(floor.pop(num))'''




def detect_collision():
    global text,w,obstacles,dino,if_dead
    x_d,y_d = w.coords(text)
    for obstacle in obstacles:
        try:
            x_min,y_min,x_max,y_max = w.bbox(obstacle) 
        except:
            print(obstacle)
        
        d = (
            (x_min+5>x_d+7),
            (x_max-5<x_d-7),
            (y_min+5>y_d+17),
            (y_max-5<y_d-17)
        )
        if not any(d):
            #w.itemconfig(text,text='dead')
            if_dead = True
            dino.dead_status()
            #time.sleep(0.3)

def init_floor():
    global floor,s_mp
    for t in range(int(width/60)+2):
        f = w.create_line(t*70,height-20,(t+1)*70,height-20)
        floor.append(f)
    for t in range(int(width/20)+2):
        t = t*20
        h = random.randint(0,10)
        f2 = w.create_line(t+random.randint(0,1),height-17+h,t+random.randint(1,4),height-17+h,width =1)
        floor.append(f2)




def make_floor():
    global floor,s_mp

    f = w.create_line(width,height-20,width+(6+s_mp)*10,height-20)
    
    floor.append(f)
    
            
def make_mud():
    global floor
    h = random.randint(0,10)
    f2 = w.create_line(width+random.randint(0,1),height-17+h,width+random.randint(1,4),height-17+h,width =1)
    floor.append(f2)


def restart(e):
    global stare,if_dead,dino,floor,obstacles,text,timer,score,score_text,hiscore_text,hiscore,auto_text,old_state
    if if_dead:
        w.delete('all')
        floor = []
        obstacles = []
        dino = Dino()
        text = dino.get_item_num()
        with open(d,'r') as f:
            hiscore = f.read()
        if auto:
            auto_text = w.create_text(50,20,text = 'AUTO', font = 'Minecraftia 20',fill = '#535353')
        else:
            auto_text = w.create_text(50,20,text = '', font = 'Minecraftia 20',fill = '#535353')
        old_state = auto
        hiscore_text = w.create_text(width-160,20,text = 'HI '+str(hiscore).zfill(5), font = 'Minecraftia 20',fill = '#535353')
        init_floor()
        timer = time.time()
        #dino = Dino()
        #accleration = 1
        if_dead = False
        score = 0
        score_text = w.create_text(width-50,20,text = str(score).zfill(5), font = 'Minecraftia 20',fill = '#535353')
        loop()

def stare():
    
    
    return 0

def toggle_auto(e):
    global auto
    auto = not auto

counter = 0
ct2 = 0
old_state = False
def loop():
    global w,text,counter,if_dead,stare,s_mp,score_text,score,ct2,hiscore_text,cacti_gen_rate,old_state
    loop_time = time.time()
    if if_dead: 
        #w.delete('all')

        #print(score)
        with open(d,'r') as f:
            t = f.read()
        if int(t) <= score:
            with open(d,'w') as f:
                print('!')
                f.write(str(score))

        stare = w.create_image(width/2,height/2,image = w.gameover)
        w.after(10,stare)
        return 0
    counter+=1
    ct2 +=1
    
    
    birb_gen_rate = 30-random.randint(-25,25)
    #if cacti_gen_rate<=10: cacti_gen_rate=10
    if counter >= cacti_gen_rate:
        #print(cacti_gen_rate)
        #print(s_mp*3)
        cacti_rd = random.randint(-15,35)
        
        cacti_gen_rate = 50-(s_mp*5)-cacti_rd
        
        random_obstacle()
        counter = 0
    if ct2 >= birb_gen_rate:
        rd = random.randint(0,5)<=3
        if rd:
            pass
            #random_birb()
        ct2 = 0
    if counter % 7 == 0:
        make_floor()
        
    if counter % 3 ==0 :#or s_mp>=10:
        make_mud()
    
    
    w.itemconfigure(score_text,text = str(score).zfill(5))
    
    if score > int(hiscore):
        
        his = 'HI '+str(score).zfill(5)
        w.itemconfigure(hiscore_text,text = his)
    if auto != old_state:
        td = {True:'AUTO',False:''}  
        w.itemconfigure(auto_text,text = td[auto])
        old_state = auto
    x,y = w.coords(text)
    
    #print(x,y)
    move()
        
    detect_collision()
    print(time.time()-loop_time)
    w.after(10,loop)
    

root = tk.Tk()


FILEPATH = os.path.dirname(__file__)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
stare = 0
obstacles = []
auto = False
s_mp = 0
cacti_gen_rate = 50-(s_mp*3)-random.randint(-15,25)

width,height = screen_width,500 # x,y
in_air = False
floor = []
l = tk.Label(root)
if_dead = False
w = tk.Canvas(root,height = screen_height,width = screen_width)
w.pack()
w.focus_set()
w.bind('<Button-1>',restart)
w.bind('<KeyPress>',lambda e:jump_timer())
w.bind('<KeyRelease>',lambda e:jump_timer_down())
w.bind('<p>',toggle_auto)
score = 0
c = Clouds()

score_text = w.create_text(width-50,20,text = str(score).zfill(5), font = 'Minecraftia 20',fill = '#535353')
d = os.path.dirname(__file__)
d = os.path.join(d,'DinoScore.txt')
if not (os.path.exists(d) and os.path.isfile(d)):
    with open(d,'w') as f:
        f.write('0')
with open(d,'r') as f:
    hiscore = f.read()

hiscore_text = w.create_text(width-160,20,text = 'HI '+str(hiscore).zfill(5), font = 'Minecraftia 20',fill = '#535353')
w.gameover = ImageTk.PhotoImage(Image.open(os.path.join(FILEPATH,'assets/gameover.gif')))

auto_text = w.create_text(50,20,text = '', font = 'Minecraftia 20',fill = '#535353')


init_floor()

obs = []
paths = (
    os.path.join(FILEPATH,'assets/ca1.gif'),
    os.path.join(FILEPATH,'assets/ca2.gif'),
    os.path.join(FILEPATH,'assets/ca3.gif'),
    os.path.join(FILEPATH,'assets/caca2.gif'),
    os.path.join(FILEPATH,'assets/cac5.gif'))

exposedpaths = (os.path.join(FILEPATH,'assets/ca1 copy.gif'),
os.path.join(FILEPATH,'assets/ca2 copy.gif'),
os.path.join(FILEPATH,'assets/ca3 copy.gif'),
os.path.join(FILEPATH,'assets/cac5 copy.gif'),
os.path.join(FILEPATH,'assets/caca2 copy.gif'))

for path in paths:
    obs.append(ImageTk.PhotoImage(Image.open(path)))
w.obs = obs
obs =[]
for path in exposedpaths:
    obs.append(ImageTk.PhotoImage(Image.open(path)))
w.exp = obs  


accleration,speed = 1,0
dino = Dino()
text = dino.get_item_num()
speed_multiplier()
#text = w.create_text(100,100,text='ass',font='Courier')


root.tk.call("::tk::unsupported::MacWindowStyle", "style", root._w, "plain", "none")
#root.wm_attributes('-fullscreen','true')
app = FullScreenApp(root)

loop()
root.mainloop()