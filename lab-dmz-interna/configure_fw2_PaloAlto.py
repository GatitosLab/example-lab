import paramiko
import time

# Datos de conexión al Palo Alto PA-VM
hostname = "172.100.100.15"
port = 22
username = "admin"
password = "Admin@123"

# Comandos de configuración para el escenario lab-dmz-interna
commands = """
configure

set network interface ethernet ethernet1/1 layer3 ip 192.168.20.2/24
set network virtual-router default interface ethernet1/1
set zone outside network layer3 ethernet1/1

set network interface ethernet ethernet1/2 layer3 ip 192.168.30.1/24
set network virtual-router default interface ethernet1/2
set zone dmz network layer3 ethernet1/2

set network interface ethernet ethernet1/3 layer3 ip 192.168.40.1/24
set network virtual-router default interface ethernet1/3
set zone internal network layer3 ethernet1/3

set network interface ethernet ethernet1/4 layer3 ip 192.168.50.1/24
set network virtual-router default interface ethernet1/4
set zone internal network layer3 ethernet1/4

set rulebase security rules allow-fw1-to-dmz from outside to dmz source any destination any application any action allow
set rulebase security rules allow-internal-to-dmz from internal to dmz source any destination any application any action allow
set rulebase security rules allow-internal-to-internal from internal to internal source any destination any application any action allow
set rulebase security rules deny-all from any to any source any destination any application any action deny

set network profiles interface-management-profile mgmt-profile ssh yes https yes

set network interface ethernet ethernet1/1 layer3 interface-management-profile mgmt-profile
set network interface ethernet ethernet1/2 layer3 interface-management-profile mgmt-profile
set network interface ethernet ethernet1/3 layer3 interface-management-profile mgmt-profile
set network interface ethernet ethernet1/4 layer3 interface-management-profile mgmt-profile

commit
exit
"""

def configure_palo_alto():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("[+] Conectando al Palo Alto PA-VM...")
    client.connect(hostname, port=port, username=username, password=password)

    remote_shell = client.invoke_shell()
    time.sleep(1)

    print("[+] Enviando configuración...")
    for line in commands.strip().split('\n'):
        remote_shell.send(line + '\n')
        time.sleep(0.7)
        output = remote_shell.recv(5000).decode('utf-8')
        print(output)

    print("[+] Configuración finalizada. Cerrando conexión...")
    remote_shell.close()
    client.close()

if __name__ == "__main__":
    configure_palo_alto()
