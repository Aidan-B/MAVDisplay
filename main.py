import tkinter as tk
import threading
import time
import altitude
from pymavlink import mavutil

def mav_thread():
    
    mav = mavutil.mavlink_connection('udpin:127.0.0.1:14550')
    mav.wait_heartbeat()

    while True:
        msg = mav.recv_match(type='AHRS2', blocking=True)

        if not msg:
            continue
        if msg.get_type() == "BAD_DATA":
            if mavutil.all_printable(msg.data):
                sys.stdout.write(msg.data)
                sys.stdout.flush()
        else:
            widget.update_attitude_widget(f"Altitude: {str(msg.altitude)}")


root = tk.Tk()
root.title("Altitude Readout")
widget = altitude.AltitudeWidget(root, "Start")

# Mavlink thread
thd = threading.Thread(target=mav_thread) 
thd.daemon = True
thd.start()  # start timer loop

# UI thread
root.mainloop()
