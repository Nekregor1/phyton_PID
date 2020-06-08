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
controller=PID_controller(0.8,0.5,0)

for i in range(0, 400):
    if i < 20:
        ar.append(0)
    else:
        ar.append(50)

    timer=timer+dt
    #control

    y=controller.getControl(x,ar[i],timer)

    vel = 10 * y
    x = x + vel * dt + a * dt * dt / 2
    f.append(x)
    t.append(timer)
# end for
gr.printgr(t,ar,f)
