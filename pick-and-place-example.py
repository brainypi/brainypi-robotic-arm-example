from uarm.wrapper import SwiftAPI

# Connect to the uArm Swift Pro robotic arm
swift = SwiftAPI()

# Reset the Arm to original position
swift.reset(speed=100000, wait=True)

# Move to the pickup co-ordinate
swift.set_position(x=250, y=210, z=25, speed=100000,wait = True)
# Wait for the command to complete.
swift.flush_cmd()
# Pickup the object by setting suction on 
swift.set_pump(True)

# Move to the co-ordinate to place the object 
swift.set_position(x=250, y=210, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=250, y=140, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=250, y=70, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=250, y=0, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=220, y=-70, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=200, y=-140, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=180, y=-210, z=170, speed=100000,wait = True)
swift.flush_cmd()
swift.set_position(x=250, y=-210, z=25, speed=100000,wait = True)
swift.flush_cmd()

# Wait 500ms, so that the object is release gently. 
time.sleep(0.5)

# Place the object down
swift.set_pump(False)
swift.flush_cmd()
swift.set_position(x=250, y=-210, z=120, speed=100000,wait = True)
swift.flush_cmd()
# Come back to rest position 
swift.reset(speed=100000, wait=True)
swift.flush_cmd()
