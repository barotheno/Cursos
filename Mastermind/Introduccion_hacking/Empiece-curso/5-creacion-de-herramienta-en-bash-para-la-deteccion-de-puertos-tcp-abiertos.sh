#!/bin/bash
# seq = que valla de un numero a otro

# ./portScan.sh <ip-address>
clear
echo -e "*** Hello my friend***\n"

function red_team () {
    for i in $(seq 2 254); do
        timeout 1 bash -c "ping -c 1 10.0.2.$i > /dev/null 2>&1" && echo "Host 10.0.2.$i - ACTIVE" &
        
    done; wait
}

red_team
echo -e "\n"
if [ $1 ]; then
    ip_address=$1
    echo -e "[*] IP Address: $ip_address"
    for port in $(seq 1 65535); do
        timeout 1 bash -c "echo '' > /dev/tcp/$ip_address/$port" 2>/dev/null && echo "[*] Port $port - OPEN" & 
    done; wait
else
    echo -e "\n[!] Uso: .portScan.sh <ip-address"
    exit 1
fi



