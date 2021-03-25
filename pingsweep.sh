#!/bin/bash

iprange=${1%.*}

pingsweep () {
    for i in {1..254}
    do
        ping -c 1 -W 1 $iprange.$i >> pingsweep.txt &
        BACK_PID=$!
    done
}

if [[ $1 =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/24$ ]]
then
    echo ""
    echo "######## Ping sweeping $iprange.1  - $iprange.254 ########"
    echo ""
    echo "## Results will be returned in results.txt file ##"
    echo ""
    echo "## Resulting IP addresses are those with 0% packet loss and are up for further enumeration. ##"
    pingsweep
    wait $BACK_PID
    grep -i -B 1 " 0% packet loss" pingsweep.txt >> sweepresults.txt;
    rm pingsweep.txt;
    grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' sweepresults.txt | sort -n > results.txt;
    rm sweepresults.txt
    echo ""
    echo "Done!"
else
    echo ""
    echo "#### Usage is ./pingsweep.sh <ip address>/24"
    echo ""
    echo "#### Example: ./pingsweep.sh 192.168.0.1/24"
    echo ""
    echo "#### Pingsweep will scan XXX.XXX.XXX.1 - XXX.XXX.XXX.254"
    echo "#### Active IP's that return 0% packet loss will be returned in results.txt file"
fi