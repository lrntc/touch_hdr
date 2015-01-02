import time
import subprocess
from subprocess import call

detected = False

def is_device_available():
    cmd = subprocess.call(["gphoto2", "--storage-info"])
    print(cmd)
    if cmd == 0:
        return True
    else:
        return False
    
def set_up_dslr():
    timeout = time.time() + 60
    detected = False
    while time.time() < timeout:
        if is_device_available():
            detected = True
            print("succes")

            #Set storage to Memory Card
            subprocess.call(["gphoto2", "--set-config", "/main/settings/capturetarget=1"])

            print("Changed capture target")
            
            break
        # maybe show some feedback why he has to wait
        time.sleep(1)
    if not detected:
        raise Exception('Camera device not detected')

set_up_dslr()
