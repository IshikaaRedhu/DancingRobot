from controller import Robot
robot = Robot()
timestep = 64

p_l = robot.getDevice("PelvL")
p_r = robot.getDevice("PelvR")
l_ul = robot.getDevice("LegUpperL")
r_ul = robot.getDevice("LegUpperR")
a_l = robot.getDevice("AnkleL")
a_r = robot.getDevice("AnkleR")
al_l = robot.getDevice("ArmLowerL")
al_r = robot.getDevice("ArmLowerR")
au_l = robot.getDevice("ArmUpperL")
au_r = robot.getDevice("ArmUpperR")
f_l = robot.getDevice("FootL")
f_r = robot.getDevice("FootR")
head = robot.getDevice("Head")
neck = robot.getDevice("Neck")
p_yl = robot.getDevice("PelvYL")
p_yr = robot.getDevice("PelvYR")
s_l = robot.getDevice("ShoulderL")
s_r = robot.getDevice("ShoulderR")
ll_r = robot.getDevice("LegLowerR")
ll_l = robot.getDevice("LegLowerL")
head_led = robot.getDevice("HeadLed")
eyes_led = robot.getDevice("EyeLed")

eyes_led.set(880000)
head_led.set(880000)

a_l.setPosition(-0.47) #a
a_r.setPosition(0.47)  #b
al_l.setPosition(0.2) #c
al_r.setPosition(-0.2) #d
au_l.setPosition(0.3) #e 
au_r.setPosition(-0.3) #f
f_l.setPosition(0.0) #g
f_r.setPosition(0.0) #h
head.setPosition(0.21) #i 
ll_l.setPosition(-1) #j
ll_r.setPosition(1) #k
l_ul.setPosition(0.74)  #l
r_ul.setPosition(-0.74)  #m
neck.setPosition(0.0) #n  
p_l.setPosition(0.0)  #o
p_r.setPosition(0.0) #p
p_yl.setPosition(-0.1) #q
p_yr.setPosition(0.1) #r
s_l.setPosition(0.86) #s
s_r.setPosition(-0.86) #t   

def move_bot(a=-0.47,b=0.47,c=0.2,d=-0.2,
             e=0.3,f=-0.3,g=0.0,h=0.0,i=0.21,
             j=-1,k=1,l=0.74,m=-0.74,n=0.0,o=0.0,p=0.0,
             q=-0.1,r=0.1,s=0.86,t=-0.86):
    
    a_l.setPosition(a) #a
    a_r.setPosition(b)  #b
    al_l.setPosition(c) #c
    al_r.setPosition(d) #d
    au_l.setPosition(e) #e 
    au_r.setPosition(f) #f
    f_l.setPosition(g) #g
    f_r.setPosition(h) #h
    head.setPosition(i) #i 
    ll_l.setPosition(j) #j
    ll_r.setPosition(k) #k
    l_ul.setPosition(l)  #l
    r_ul.setPosition(m)  #m
    neck.setPosition(n) #n  
    p_l.setPosition(o)  #o
    p_r.setPosition(p) #p
    p_yl.setPosition(q) #q
    p_yr.setPosition(r) #r
    s_l.setPosition(s) #s
    s_r.setPosition(t) #t      

def add_delay(delay_time_steps):

    time_counter = 0
    while robot.step(timestep)  !=  -1:
        if time_counter  >=  delay_time_steps:
            break
        
        time_counter += 1
while robot.step(timestep) != -1:
    move_bot(e = 0.6, f = -0.6)
    add_delay(10)
    move_bot(i=0.5)   
    add_delay(10)
    move_bot(c=-0.5 , d = 0.5)  
    add_delay(10)
    move_bot(e = 0.77, f =-0.68)  
    add_delay(10)
    move_bot(s= -0.25, t = 0.25)  
    add_delay(10)
    move_bot(s = 1.325, t = -1.325) 
    add_delay(10)
    move_bot(c= -0.61, d =-0.61 , n = 0.2) 
    add_delay(10)
    move_bot(c = 0.7, d = 0.7 , n = -0.2) 
    add_delay(10)
    move_bot(c = -0.2, d = 0.2, e = 0.7, f = -0.7, s = -1.6, t = 1.6)
    add_delay(10)
    move_bot(o = -0.2, p = -0.2, c  = 1.63, e = 0.4 )
    add_delay(10)
    
    move_bot(o = 0.2, p =0.2, d = -1.63, f = -0.4)
    add_delay(10)
    move_bot(o = -0.2, p = -0.2, c  = 1.63, e = 0.4 )
    add_delay(10)
    
    move_bot(o = 0.2, p =0.2, d = -1.63, f = -0.4)
    add_delay(10)
    move_bot(o = 0, p = 0,s = -0.3, t = 0.3, c= -0.61, d =-0.61, e = 0.77, f = -0.68)
    add_delay(10)
    move_bot(c=-0.5 , d = 0.5,e = 0.1, f =-0.1)
    add_delay(10)
    
    