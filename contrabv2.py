import os
import re
import subprocess
import sys
import time

import mariadb

try:
    conn = mariadb.connect(
        user="clientlab",
        password="cslab",
        host="127.0.0.1",
        port=3306,
        database="Invlab"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


def insertHostServiceLogs(cur_host_service_id,services):
    print (services)
    for service in services: 
        cur.execute(f"insert into log_servicios (status,nombre,SERVICIOS_ID) values ('{service[2]}','{service[3]}','{cur_host_service_id}')")
    conn.commit()
   
    
    

def removeFinishedScan(cur_host_ip):
    os.remove(f'/home/client_rrsync/results/finished/{cur_host_ip}')


def getHostServicesInfo(filecontent):
    services = []
    portstate_patt = re.compile(r"\s(\d+/\w.*)")
    if portstate_patt.search(filecontent):
        for port_info in portstate_patt.findall(filecontent):
            services.append([port_info[0:2], port_info[3:6], port_info[7:].split()[0], port_info[7:].split()[1]])
        return services


def insertHostServices(cur_host_id, services):
    for service in services:
        try:
            cur.execute(
                f"insert into servicios (port,protocol,HOST_ID) values ('{service[0]}','{service[1]}','{cur_host_id}')")
            conn.commit()
        except mariadb.IntegrityError:
            print(f'Already added {service} as a client ip skipping insertion...')
            pass
        finally:
            cur.execute(f"select SERVICIOS_ID from servicios where HOST_ID ='{cur_host_id}'")
            return cur.fetchone()[0]
        

            


def getMacAddress(filecontent):
    mac_patt = re.compile(r"MAC Address: (?:[a-fA-F0-9]{2}:)+[a-fA-F0-9]{2}")
    if mac_patt.search(filecontent):
        return mac_patt.search(filecontent)[0].split()[2]
    else:
        return None


def insertHostLogs(cur_host_id, hardware_address):
    try:
        print(f"Inserting host with Mac Address: {hardware_address}")
        cur.execute(f"insert into logs (HOST_ID,HADDRS,status) values ('{cur_host_id}','{hardware_address}','online')")
        conn.commit()
    except mariadb.IntegrityError:
        print(f"Updating log timestamp for host with Mac Address: {hardware_address}")
        cur.execute(f"select * from logs where HADDRS='{hardware_address}' and HOST_ID={cur_host_id}")
        if cur.fetchone() != None:
            cur.execute(f"update logs set timestamp=current_time() where HADDRS='{hardware_address}'")
        else:
            print("A Host has changed")
            cur.execute(f"select HADDRS from logs where HOST_ID='{cur_host_id}'")
            print(f"Old Mac Address:{cur.fetchone()[0]} New Mac Address: {hardware_address}")


def insertClientIP(client):
    try:
        cur.execute(f"insert into clientes (ip_vpn) values ('{client}')")
        conn.commit()
    except mariadb.IntegrityError:
        print(f'Already added {client} as a client ip skipping insertion...')
    finally:
        cur.execute(f"select CLIENT_ID from clientes where IP_VPN ='{client}'")
        for CLIENT_ID in cur:
            client_id = CLIENT_ID[0]
        return client_id


def insertHostIP(cur_host_ip, cur_client_id, cur_client_ip):
    try:
        cur.execute(f"insert into host (HOST_IP,CLIENT_ID) printvalues ('{cur_host_ip}','{cur_client_id}')")
        conn.commit()
    except mariadb.IntegrityError:
        print(f'This host: {cur_host_ip} already has a relation with client: {cur_client_ip}. Skipping insertion.')
    finally:
        cur.execute(f"select HOST_ID from host where HOST_IP='{cur_host_ip}' and CLIENT_ID='{cur_client_id}'")
        for HOST_ID in cur:
            host_id = HOST_ID[0]
        return host_id


def printInsertedValues(filecontent, finished_scan):
    portstate_patt = re.compile(r"\s(\d+/\w.*)")
    mac_patt = re.compile(r"MAC Address: (?:[a-fA-F0-9]{2}:)+[a-fA-F0-9]{2}")
    addr_patt = re.compile(r".*ADDRESS\n\d+\s.*")
    if mac_patt.search(filecontent):
        print(mac_patt.search(filecontent)[0].split()[2])
    else:
        print('NULL')


def main():
    hosts = os.listdir("/home/client_rrsync/results/finished/")
    print(hosts)
    for cur_host_ip in hosts:
        try:
            for cur_client_ip in os.listdir('/home/client_rrsync/results/' + cur_host_ip + '/results/'):
                try:
                    current_file = open(
                        '/home/client_rrsync/results/' + cur_host_ip + '/results/' + cur_client_ip + '/scans/_full_tcp_nmap.txt')
                    filecontent = current_file.read()
                    cur_client_id = insertClientIP(cur_client_ip)
                    cur_host_id = insertHostIP(cur_host_ip, cur_client_id, cur_client_ip)
                    services = getHostServicesInfo(filecontent)
                   # cur_host_service_id = insertHostServices(cur_host_id, services)
                  #  insertHostServiceLogs(cur_host_service_id,services)
                    hardware_address = getMacAddress(filecontent)
                    insertHostLogs(cur_host_id, hardware_address)
                    # printInsertedValues(filecontent,  cur_host_ip, cur)
                    # removeFinishedScan(cur_host_ip)
                except FileNotFoundError as err:
                    print(f"current directory: {cur_client_ip} doesn't have the scan folder...skipping.")
                    pass
        except FileNotFoundError as err:
            print(f"Current folder: {cur_host_ip} doesn't have a valid directory ignoring...")
            pass


main()


def job():
    try:
        print("Executing job...")
        hostfile_location = sys.argv[1]
        hostfile = open(hostfile_location, "r").read()
        bashcommand = "parallel-ssh -x -tt -h " + hostfile_location + " autorecon -o ~/results $(nmap -sP $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '10.8.0.*'| grep -v '127.0.0.1')/24 | grep -Eo '(addr:)?([0-9]*\.){3}[0-9]*')"
        process = subprocess.run(bashcommand.split(), capture_ifoutput=True)
        if process.returncode == 0:
            for i in hostfile.split():
                bashcommand = "rsync -ar " + i + ":~/results /home/kali/Desktop/" + i
                process = subprocess.run(bashcommand.split(), capture_output=True)
                if process.returncode == 0:
                    print('completed rsync in' + i)
                else:
                    print('error rsync in ' + i)
        else:
            print('error')
            bashcommand = "parallel-ssh -x -tt -h " + hostfile_location + " ~/backupautorecon"
            process = subprocess.run(bashcommand.split(), capture_output=True)
            time.sleep(int(sys.argv[2]))
            bashcommand = "parallel-ssh -i -x -tt -h " + hostfile_location + " cat ~/finished"
            process = subprocess.run(bashcommand.split(), capture_output=True)
            print(process.stdout)


    except FileNotFoundError as err:
        print(err)



# job()
def job():
    try:
        print("Executing job...")
        hostfile_location = sys.argv[1]
        hostfile = open(hostfile_location,"r").read()
        bashcommand = "parallel-ssh -x -tt -h "+hostfile_location+" autorecon -o ~/results $(nmap -sP $(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '10.8.0.*'| grep -v '127.0.0.1')/24 | grep -Eo '(addr:)?([0-9]*\.){3}[0-9]*')"
        process = subprocess.run(bashcommand.split(), capture_ifoutput=True)
        if process.returncode == 0:
            for i in hostfile.split():
                bashcommand = "rsync -ar "+i+":~/results /home/kali/Desktop/"+i
                process = subprocess.run(bashcommand.split(), capture_output=True)
                if process.returncode == 0:
                    print('completed rsync in'+i)
                else:
                    print('error rsync in ' + i)
        else:
            print('error')
            bashcommand = "parallel-ssh -x -tt -h "+hostfile_location+" ~/backupautorecon"
            process = subprocess.run(bashcommand.split(), capture_output=True)
            time.sleep(int(sys.argv[2]))
            bashcommand = "parallel-ssh -i -x -tt -h "+hostfile_location+" cat ~/finished"
            process = subprocess.run(bashcommand.split(), capture_output=True)
            print(process.stdout)
        
   
    except FileNotFoundError as err:
        print(err)


