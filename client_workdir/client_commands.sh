serverip= 
sudo apt install openvpn
sudo apt install python3
sudo apt install python3-pip
sudo apt install seclists
sudo apt install screen
sudo apt install nmap
sudo apt install openssh-client
sudo apt install net-tools
sudo apt install psmisc
sudo apt install rsync
python3 -m pip install git+https://github.com/Tib3rius/AutoRecon.git
sudo ssh-keygen
sudo echo 'command="/usr/bin/rrsync -wo ~/results",no-agent-forwarding,no-port-forwarding,no-pty,no-user-rc,no-X11-forwarding' $(sudo cat /root/.ssh/id_rsa.pub) | sudo ssh client_rrsync@$serverip 'cat >> ~/.ssh/authorized_keys'
