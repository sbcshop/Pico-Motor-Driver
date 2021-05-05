from machine import Pin
import utime

m1 = Pin(21, Pin.OUT)
m2 = Pin(20, Pin.OUT)
m3 = Pin(19, Pin.OUT)
m4 = Pin(18, Pin.OUT)

en1 = Pin(17, Pin.OUT)
en2 = Pin(16, Pin.OUT)

def Enable_motor():
    en1(1)  # motor 1 enable, set value 0 to disable
    en2(1)  # motor 2 enable, set value 0 to disable

def Motor1_forward():
    m1(1)
    m2(0)
    
def Motor1_reverse():
    m1(0)
    m2(1)
    
def Motor2_forward():
    m3(1)
    m4(0)
    
def Motor2_reverse():
    m3(0)
    m4(1)
    
def Motor_stop():
    m1(0)
    m2(0)
    m3(0)
    m4(0)
    
while True:
    Enable_motor()
    Motor1_forward()
    Motor2_forward()
    utime.sleep(2) # Both motor in Forward direction for 2 seconds.
    Motor_stop()
    utime.sleep(2) # Both motor in Stop position.
    Motor2_reverse()
    Motor2_reverse()
    utime.sleep(2) # Both motor in Reverse direction for 2 seconds.
        
