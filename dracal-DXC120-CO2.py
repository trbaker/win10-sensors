# assumes DracalView has been installed and usb_gps_get has been configured (with PATH updated).
# USB GPS in use: Dracal DXC120 CO2 sensor

import sys
import subprocess
import time

# Note: dracal-usb-get assumed to be in the path
# Arguments passed to -i (0,1,2) here need to be updated to fit
# your scenario. You may also specify a serial number by adding
# the -s argument.

# If dracal-usb-get exits with a non-zero values, the subprocess.CalledProcessError
# exception will be raised. Catch it.

while True:
    try:
        p = subprocess.check_output(["dracal-usb-get","-i","0"])
    except subprocess.CalledProcessError:
        print ("dracal-usb-get error")
        sys.exit(1)
    # Display values
    p = p.rstrip().lstrip() # removes tail /r/n
    p=p.decode("utf-8") # remove the b and single quotes
    print ("Carbon dioxide (ppm):", p)
    time.sleep(60) # in seconds
