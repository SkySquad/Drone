from dronekit import connect, VehicleMode, LocationGlobalRelative
import dronekit as vehicle
import time
import argparse
import cv2
import numpy as np
import pymavlink

def connectMyCopter():
    parser = argparse.ArgumentParser(description="commands")
    parser.add_argument('--connect')
    args = parser.parse_args()
    connection_string = args.connect
    baud_rate = 57600
    vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)
    return vehicle


def arm_and_takeoff(aTargetAltitude):
    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    time.sleep(5)

    print("TAKING OFF!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude
    while True:                              # Check that vehicle has reached takeoff altitude
        print
        " Altitude: ", vehicle.location.global_relative_frame.alt
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


vehicle = connectMyCopter()
arm_and_takeoff(4)

#################
##################

cap = cv2.VideoCapture(0)
time.sleep(2.2)
w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0

def condition_yaw(heading, relative=False):
    if relative:
        is_relative=1 #yaw relative to direction of travel
    else:
        is_relative=0 #yaw is an absolute angle
    # create the CONDITION_YAW command using command_long_encode()
    msg = vehicle.message_factory.command_long_encode(
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, #command
        0, #confirmation
        heading,    # param 1, yaw in degrees
        0,          # param 2, yaw speed deg/s
        1,          # param 3, direction -1 ccw, 1 cw
        is_relative, # param 4, relative offset 1, absolute angle 0
        0, 0, 0)    # param 5 ~ 7 not used
    # send command to vehicle
    vehicle.send_mavlink(msg)
def track_color( info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))
    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20
    if x == 0:
        speed = 0
        error = 0
    return error
def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def update_color(self, val):
        """
        Adjusts the currently tracked color to input.
        """
        if (cv2.mean(val) != 0):
            for i in range(0,2):
                self.current_color[i] = clamp(val[i],
                                       self.color_lower[self.color_keys[self.controll_params['Color']]][i],
                                       self.color_upper[self.color_keys[self.controll_params['Color']]][i])

def track(frame):
    """
    HSV color space tracking.
    """
    target_radius = 120
    crange = (10, 50, 50)
    color_lower = {
        'blue': (100, 200, 50),
        'red': (0, 200, 100),
        'yellow': (20, 200, 130),
    }
    color_upper = {
        'blue': (140, 255, 255),
        'red': (20, 255, 255),
        'yellow': (40, 255, 255),
    }
    controll_params = {
        'Speed': 100,
        'Color': 0,
    }
    current_color=np.array(color_lower['blue']) + np.array(color_upper['blue'])
    hud_size = (800, 600)
    midx=int(hud_size[0] / 2)
    midy=int(hud_size[1] / 2)
    # resize the frame, blur it, and convert it to the HSV
    # color space
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_RGB2HSV)
    central_color = hsv[midy,midx, :]

    # construct a mask for the color then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv,current_color -crange,current_color+crange)
    mask = cv2.erode(mask, None, iterations=3)
    mask = cv2.dilate(mask, None, iterations=3)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    image, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                              cv2.CHAIN_APPROX_SIMPLE)

    center = None

    radius = 0
    velocity = 0
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # update color from mean color
        mask_upstate = cv2.bitwise_and(hsv, hsv, mask=mask)
        mean = cv2.mean(mask_upstate)
        multiplier = float(mask.size) / (cv2.countNonZero(mask) + 0.001)
        mean = np.array([multiplier * x for x in mean])

        update_color(mean)
        print( current_color)

        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)

        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 40:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 0), 2)

            xoffset = int(center[0] -  midx)
            yoffset = int( midy - center[1])
            velocity = clamp(target_radius - radius, -40, 60) / 100 *  controll_params['Speed']
        else:
            xoffset = 0
            yoffset = 0
            velocity = 0
    else:
        xoffset = 0
        yoffset = 0
        velocity = 0

    xfact =  xoffset /  hud_size[0] *  controll_params['Speed'] * 2
    yfact =  yoffset /  hud_size[0] *  controll_params['Speed'] * 2
    return xfact

while True:

    _, img = cap.read()
    img = cv2.resize(img, (w, h))
    pError = track(img)
    condition_yaw(pError,1)
    cv2.imshow()
    #print("Center", info[0], "Area", info[1])

    if cv2.waitkey(1) & 0xFF == ord('q'):

        vehicle.mode = VehicleMode("LAND")

        break
#################
#################

cap.release()
cv2.destroyAllWindows()

vehicle.mode = VehicleMode("RTL")
time.sleep(20)
vehicle.close()