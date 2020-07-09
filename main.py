import graph as gr
import  time
from PID_controller import PID_controller
#PID controller test
x=0
vel=0
ar=[]
f=[]
t_graph=[]
v_graph=[]
dt=0.05
t=0
t0=time.time();
t_last=0
v_last=0
controller=PID_controller(0.5,0.1,0.1)

for i in range(0, 1000):
    if i < 20:
        ar.append(0)
    else:
        ar.append(5)


    #t = time.time()-t0
    t = t+dt
    #dt = t - t_last
    #control
    dx=ar[i]-x

    y=controller.getControl(dx)
    a=20*y
    vel = vel +a*dt
    if vel > 10:
        vel = 10
    elif vel < -10:
        vel = -1

    x = x + vel*dt + a*dt* dt/2
    f.append(x)
    t_graph.append(t)
    v_graph.append(vel)

    t_last =t
    time.sleep(0.01)
    v_last=vel
# end for
gr.printgr(t_graph,ar,f)
