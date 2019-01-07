import time
import os

RED_BCM_PORT = 22
GREEN_BCM_PORT = 17
BLUE_BCM_PORT = 27


def hsv_to_rgb(h,s,v):
    C = v*s
    X = C * (1 - abs(((h/60.0)%2)-1))
    m = v-C
    
    R = 0
    G = 0
    B = 0

    if(0 <= h < 60):
        R = C
        G = X
    elif(60 <= h < 120):
        R = X
        G = C
    elif(120 <= h < 180):
        G = C
        B = X
    elif(180 <= h < 240):
        G = X
        B = C
    elif(240 <= h < 300):
        R = X
        B = C
    else:
        R = C
        B = X

    return R+m, G+m, B+m

for v in xrange(0,10):
    print "Value: " + str(v/10.0)
    for s in xrange(0, 10):
        print "Saturation: " + str(s/10.0)
        for h in xrange(0, 360):
            r,g,b = hsv_to_rgb(h, s/10.0, v/10.0)
        
            os.system('echo "' + str(RED_BCM_PORT) + "=" + str(r) + '" > /dev/pi-blaster')
            os.system('echo "' + str(GREEN_BCM_PORT) + "=" + str(g) + '" > /dev/pi-blaster')
            os.system('echo "' + str(BLUE_BCM_PORT) + "=" + str(b) + '" > /dev/pi-blaster')
            time.sleep(0.0001)

