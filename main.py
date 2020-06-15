import graph as gr
from PID_controller import PID_controller

x=0
vel=0
ar=[]
f=[]
speed=[]
t=[]
dx_arr=[]
dSum_arr=[]


a=0

dt=0.05
timer=0.0
controller=PID_controller(0.5,0.1,0.5)

for i in range(0, 200):
    if i < 20:
        ar.append(0)
    else:
        ar.append(10)

    timer=timer+dt
    #control
    dx=ar[i]-x
    y=controller.getControl(dx,timer)
    a=20*y
    vel = vel +a*dt
    if vel > 10:
        vel = 10
    elif vel < -10:
        vel = -10

    x = x + vel * dt + a * dt * dt / 2
    f.append(x)
    t.append(timer)
# end for
gr.printgr(t,ar,f)
