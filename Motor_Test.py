from machine import Pin
import utime

m1 = Pin(21, Pin.OUT)
m2 = Pin(20, Pin.OUT)
m3 = Pin(19, Pin.OUT)
m4 = Pin(18, Pin.OUT)

en1 = Pin(17, Pin.OUT)
en2 = Pin(16, Pin.OUT)

en1(1)  # motor 1 enable, set value 0 to disable
en2(1)  # motor 2 enable, set value 0 to disable

while True:
    #Both Motor in forward direction
    m1(1)
    m2(0)
    m3(1)
    m4(0)
    utime.sleep(0.5)
    #Both Motor in Reverse direction
    m1(0)
    m2(1)
    m3(0)
    m4(1)
    utime.sleep(0.5)
