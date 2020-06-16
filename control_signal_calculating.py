import struct
import logging
import numpy as np
from time import time, strftime
import math
from PID_controller import PID_controller
class SigCalc: 
    def __init__(self):
        self.KVU0 = 1509        #Значение канала управления при состоянии покоя для канала Pitch
        self.KKU0 = 1514        #Значение канала управления при состоянии покоя для канала Roll
        self.KRU0 = 1514        #Значение канала управления при состоянии покоя для канала Yaw
        self.KHU0 = 1520        #Значение канала управления при состоянии покоя для канала Throttle
        
        self.Vmin = -410        #Максимальное смещение канала Pitch в отрицательную сторону сторону
        self.Kmin = -410        #Максимальное смещение канала Roll в отрицательную сторону сторону
        self.Rmin = -410        #Максимальное смещение канала Yaw в отрицательную сторону сторону
        self.Hmin = -403        #Максимальное смещение канала Throttle в отрицательную сторону сторону
        
        self.Vmax = 410          #Максимальное смещение канала Pitch в положительную сторону
        self.Kmax = 410          #Максимальное смещение канала Roll в положительную сторону
        self.Rmax = 410          #Максимальное смещение канала Yaw в положительную сторону
        self.Hmax = 404          #Максимальное смещение канала Throttle в положительную сторону
        
        self.Vmin_gr = 10        #Смещение хначения сигнала управления в области нулевой невязки по каналу Pitch
        self.Kmin_gr = 10        #Смещение хначения сигнала управления в области нулевой невязки по каналу Roll
        self.Rmin_gr = 10        #Смещение хначения сигнала управления в области нулевой невязки по каналу Yaw
        self.Hmin_gr = 10        #Смещение хначения сигнала управления в области нулевой невязки по каналу Throttle
        
        self.Vi_min = 50        #Нижний порог канала управления Pitch (скорости), ниже которого не может уйти в результате компенсации угла наклона камеры
        self.Vi_max = 50        #Верхнее ограничение канала Pitch (скорости) с учетом необходимости набора высоты для отработки невязки dy
        
        self.Pitch_En = False         #Флаг, разрешающий управление по Pitch
        self.Thr_En = True            #Флаг, разрешающий управление по Throttle
        self.Roll_En = True           #Флаг, разрешающий управление по Roll
        self.Yaw_En = True            #Флаг, разрешающий управление по Yaw

        thr_control = PID_controller(0.1, 0.1, 0.01)
        rol_control = PID_controller(0.1, 0.1, 0.01)
        pit_control = PID_controller(0.1, 0.1, 0.01)
        yaw_control = PID_controller(0.1, 0.1, 0.01)


    
    def Sig_Calculate(self, dx, dy,delta_time):
        #Вычисление сигнала по каналу Throttle для конмпенсации невязки по dy
        hi = self.thr_control.getControl(dy, delta_time)

        #Вычисления сигналова по каналу Pitch
        #необходимый крен для требуемой скорости, нужно добавить входной параметр-скорость сближения
        vi = 123
        #hi = self.thr_control.getControl(d_speed, delta_time)

        #Вычисление сигнала по каналу Yaw 
        ki = self.thr_control.getControl(dx, delta_time)

        # Вычисление сигнала по каналу Roll
        ri=0.4*ki#в идеале нужно сделать чтобы нос по касательной к траектории держался


        #Формирование сигналов в формате SBUS
        #Пороговая обработка(добавить пороговую обработку)
        Kv = min(abs(self.Vmin), self.Vmax)
        Kh = min(abs(self.Hmin), self.Hmax)
        Kk = min(abs(self.Kmin), self.Kmax)
        Kr = min(abs(self.Rmin), self.Rmax)

        res_vi = int(self.KVU0 + Kv*vi)
        res_hi = int(self.KHU0 + Kh*hi)
        res_ki = int(self.KKU0 + Kk*ki)
        res_ri = int(self.KRU0 + Kr*ri)
        
        return res_vi, res_hi, res_ki, res_ri
        
        
        