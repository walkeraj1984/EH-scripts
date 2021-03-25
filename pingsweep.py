#!/usr/bin/python3

import sys
import os
import re
from datetime import datetime


# Validation check
if len(sys.argv) == 2:
    # If arguments are present, validation check that it is correctly formatted
    if re.match(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/24', sys.argv[1], re.M):
        # Reformatting the argument string for processing
        target = re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.', sys.argv[1]).group()
        commandstring = "ping -c 1 -W 1 " + target
        # Start Banner
        print("\n\r")
        print("#" * 50)
        print("\nScanning for targets in range: " + target + "1 - " + target + "254")
        print("\nTime Started: " + str(datetime.now()) + "\n")
        print("#" * 50)
        # Executing sweep 
        for i in range(1,255):
            os.system(commandstring + str(i) + " >> sweep.txt&")
            os.system("BACK_PID=$!")

        os.system("wait $BACK_PID")
        os.system("grep -i -B 1 ' 0% packet loss' sweep.txt >> sweepresults.txt;")
        os.system("rm sweep.txt;")
        os.system("grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' sweepresults.txt | sort -n >> results.txt;")
        os.system("rm sweepresults.txt;")

        # Finish Banner
        print("#" * 50)
        print("\n\rDone!\nIP addresses that returned with 0% packet loss are stored in results.txt\n")
        print("\nTime Finished: " + str(datetime.now()) + "\n\r")
        print("#" * 50)
    
    # If user submits incorrectly formatted arguments
    else:
        print("\n\r")
        print("Argument formatted improperly...\n")
        print("Usage: python3 pingsweep.py <ip range> in CIDR notation")
        print("Example: python3 pingsweep.py 192.168.0.0/24")
        print("\nThis script currently only runs in a UNIX shell")
# If user submits no arguments
else:
    print("\n\r")
    print("Usage: python3 pingsweep.py <ip range> in CIDR notation")
    print("Example: python3 pingsweep.py 192.168.0.0/24")
    print("\nThis script currently only runs in a UNIX shell")

