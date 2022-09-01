from machine import Pin
import time
 
M1A = 21 # GP21
M1B = 20 # GP20

M2A = 19 # GP19
M2B = 18 # GP18
 
step_count = 8
n = list(range(0, step_count)) # sequence

n[0] = [0,1,0,0]
n[1] = [0,1,0,1]
n[2] = [0,0,0,1]
n[3] = [1,0,0,1]
n[4] = [1,0,0,0]
n[5] = [1,0,1,0]
n[6] = [0,0,1,0]
n[7] = [0,1,1,0]
 
en1 = Pin(17, Pin.OUT)
en2 = Pin(16, Pin.OUT)

en1(1)  # motor 1 enable, set value 0 to disable
en2(1)  # motor 2 enable, set value 0 to disable

m1a = Pin(M1A,Pin.OUT)
m1b = Pin(M1B,Pin.OUT) 
m2a = Pin(M2A,Pin.OUT) 
m2b = Pin(M2B,Pin.OUT) 


def setStep(p1, p2, p3, p4):

    m1a(p1)
    m1b(p2)
    m2a(p3)
    m2b(p4)

 
def Forward(delay, steps):
    for i in range(steps):
        for j in range(step_count):
            setStep(n[j][0], n[j][1], n[j][2], n[j][3])
            time.sleep(delay)
 
def Backward(delay, steps):
    for i in range(steps):
        for j in reversed(range(step_count)):
            setStep(n[j][0], n[j][1], n[j][2], n[j][3])
            time.sleep(delay)
 

while 1:
    delay = int(input("Time Delay = ")) # write Time delay is in millisecond
    steps = int(input("Forward steps = ")) # Write how many Forward steps
    Forward(delay / 1000.0,steps)
    
    steps = int(input("Backward steps = ")) # Write how many backward steps
    Backward(delay/ 1000.0,steps)