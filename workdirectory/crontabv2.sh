#!/bin/bash
input=$(nmap -sP $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '10.8.0.*'| grep -v '127.0.0.1')/24 | grep -Eo '(addr:)?([0-9]*\.){3}[0-9]*') 
input="${input//$'\n'/ }"
if !(pgrep autorecon); 
then screen -d -m bash -c "sudo autorecon --target-timeout 10 -o /home/kali-server/Desktop/workdirectory/results/ $input>> /home/kali-server/Desktop/workdirectory/log && rsync /home/kali-server/Desktop/workdirectory/results  -r  client_rrsync@10.0.2.15:10.0.2.4/ && rsync /home/kali-server/Desktop/workdirectory/10.0.2.4 client_rrsync@10.0.2.15:finished/";
fi

