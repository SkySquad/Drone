print "Start simulator (SITL) - SkySquad "
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Import DroneKit-Python
from dronekit import connect, VehicleMode

from dronekit import connect

vehicle = connect('127.0.0.1:14550', wait_ready = True)

vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")
