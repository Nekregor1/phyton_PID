class PID_controller:

    def __init__(self,Kp,Ki,Kd):
        self.t_last = 0.0
        self.val = 0
        self.tar = 0
        self.err = 0
        self.err_last = 0
        self.err_sum = 0
        self.err_last = 0
        self.d_err = 0
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    def getControl(self,val, tar,t):
        Kp=self.Kp
        Ki = self.Ki
        Kd = self.Kd
        t_last=self.t_last
        err_sum = self.err_sum
        err_last=self.err_last
        #

        #delta time
        dt = t-t_last
        #error
        err = tar - val

        #error sum, integral
        err_sum= err_sum + err*dt
        #cut-off value
        if Ki!=0:
            err_sum_cutoff=1/Ki*dt
        else:
            err_sum_cutoff=1

        # integral cut-off
        if err_sum > err_sum_cutoff:
            err_sum = err_sum_cutoff
        elif err_sum < -err_sum_cutoff:
            err_sum = -err_sum_cutoff

        #error derivative
        if dt==0 :
            d_err=0
        else:
            d_err = (err - err_last)/dt

        #output control
        y=Kp * err + Ki * err_sum + Kd * d_err

        #output control cut-off
        if y > 1:
            y = 1
        elif y < -1:
            y = -1

        self.err_last = err_last
        self.err_sum = err_sum
        self.t_last=t

        return y
