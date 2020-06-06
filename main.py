import graph as gr
x0=0;
x=0;
vel=0
ar=[]
f=[]
speed=[]
t=[]
dx=0
dSum=0
dSum_lim=20
a=2
y_max=1;
v_max=10
dt=1
for i in range (0,500):
    if i<20 :
        ar.append(0)
    else:
        ar.append(100)

    dx=ar[i]-x
    if dx >    10:
        dx = 10
    elif dx < -10:
        dx = -10

    print(dSum)
    dSum=dSum+dx

    if dSum > dSum_lim:
        dSum = dSum_lim
    elif dSum < -dSum_lim:
        dSum = -dSum_lim

    y=dx*0+dSum*0.1

    if y>y_max:
        y=y_max
    elif y<-y_max:
        y=-y_max



    vel=vel+a*dt*y
    speed.append(vel)

    if vel > v_max:
        vel = v_max
    elif vel < -v_max:
        vel = -v_max

    x=x+vel*dt

    f.append(x)
    t.append(i)
gr.printgr(t,ar,f)
gr.printgr1(speed)

