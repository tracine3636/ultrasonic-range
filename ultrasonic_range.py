
from gpiozero import DistanceSensor
import time
import os
ultrasonic= DistanceSensor(echo=17, trigger=4, distance=0.99)

 #max_distance=2 overrides 1 ft default

from gpiozero import DistanceSensor
import time
import os
ultrasonic= DistanceSensor(echo=17, trigger=4, distance=0.99)

 #max_distance=2 overrides 1 ft default

 #0.153 meters = 6 inches
 #1 meters = 3.28 feet
 #2.13 meters = 7 feet
ultrasonic.distance
while True:
        ultrasonic.wait_for_in_range()
        print ("In range")
        ultrasonic.wait_for_out_of_range()
        print ("Out of range")
