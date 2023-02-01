from machine import Pin, PWM
import utime

m1 = 21
m2 = 20
m3 = 19
m4 = 18

en1 = 17
en2 = 16

# Speed     - enter value between 0-100
# Direction - 1 for clockwise, 0 stop, -1 for anticlockwise
# speedGP   - for Enable Pin
# cwGP      - for clockwise Pin
# acwGP     - for anti-clockwise Pin

def motorMove(speed,direction,speedGP,cwGP,acwGP):
    print(speed,direction,speedGP,cwGP,acwGP)
    if speed > 100: speed=100
    if speed < 0: speed=0
    Speed = PWM(Pin(speedGP))
    Speed.freq(20000)
    cw = Pin(cwGP, Pin.OUT)
    acw = Pin(acwGP, Pin.OUT)
    Speed.duty_u16(int(speed/100*65536))
    print(int(speed/100*65536))
    if direction < 0:
      cw.value(0)
      acw.value(1) 
    if direction == 0:
      cw.value(0)
      acw.value(0)
    if direction > 0:
      cw.value(1)
      acw.value(0)
    
while True:
    # Both motor in Forward direction for 2 seconds.
    motorMove(100,1,en1,m1,m2)
    motorMove(100,1,en2,m3,m4)
    utime.sleep(2)
    
    # Both motor in Stop position.
    motorMove(0,0,en1,m1,m2)
    motorMove(0,0,en2,m3,m4)
    utime.sleep(2)
    
    # Both motor in Reverse direction for 2 seconds.
    motorMove(100,-1,en1,m1,m2)
    motorMove(100,-1,en2,m3,m4)
    utime.sleep(2) 
    
    # Both motor in Stop position.
    motorMove(0,0,en1,m1,m2)
    motorMove(0,0,en2,m3,m4)
    utime.sleep(2) 
    
    # Both motor in opposite directions for 2 seconds.
    motorMove(100,1,en1,m1,m2)
    motorMove(100,-1,en2,m3,m4)
    utime.sleep(2) 
    
    # Both motor in Forward half speed.
    motorMove(50,1,en1,m1,m2)
    motorMove(50,1,en2,m3,m4)
    utime.sleep(2) 
