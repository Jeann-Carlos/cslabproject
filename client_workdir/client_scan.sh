#!/bin/bash
localip=
serverip=
targettimeout=
globaltimeout=
input=$(nmap -sP $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '10.8.0.*'| grep -v '127.0.0.1')/24 | grep -Eo '(addr:)?([0-9]*\.){3}[0-9]*') 
input="${input//$'\n'/ }"
if !(pgrep autorecon); 
then screen -d -m bash -c "sudo autorecon --target-timeout $targettimeout --timeout $globaltimeout -o /home/cslab/client_workdir/results/ $input>> /home/cslab/client_workdir/log && rsync /home/cslab/client_workdir/results  -r  client_rrsync@$serverip:$localip/ >>/home/cslab/client_workdir/log && touch $localip && rsync /home/cslab/client_workdir/$localip client_rrsync@$serverip:finished/ && sudo killall nmap";
fi

