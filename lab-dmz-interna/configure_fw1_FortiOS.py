import paramiko
import time

# Datos de conexión al Fortigate
hostname = "172.100.100.14"
port = 22
username = "admin"
password = "admin"

# Comandos de configuración actualizada
commands = """
config system interface
edit "port2"
set vdom "root"
set ip 192.168.30.1 255.255.255.0
set allowaccess ping
set type physical
next
edit "port3"
set vdom "root"
set ip 192.168.40.1 255.255.255.0
set allowaccess ping
set type physical
next
edit "port4"
set vdom "root"
set ip 192.168.50.1 255.255.255.0
set allowaccess ping
set type physical
next
end

config firewall address
edit "Web-Server"
set subnet 192.168.30.10 255.255.255.255
next
edit "LDAP-Server"
set subnet 192.168.40.10 255.255.255.255
next
edit "Samba-Server"
set subnet 192.168.50.20 255.255.255.255
next
edit "Client-Office"
set subnet 192.168.50.100 255.255.255.255
next
end

config firewall policy
edit 1
set name "Internet_to_WebServer"
set srcintf "port1"
set dstintf "port2"
set srcaddr "all"
set dstaddr "Web-Server"
set action accept
set schedule "always"
set service "HTTP" "HTTPS"
set logtraffic all
set nat enable
next

edit 2
set name "Client_to_LDAP"
set srcintf "port4"
set dstintf "port3"
set srcaddr "Client-Office"
set dstaddr "LDAP-Server"
set action accept
set schedule "always"
set service "LDAP"
set logtraffic all
next

edit 3
set name "Client_to_Samba"
set srcintf "port4"
set dstintf "port4"
set srcaddr "Client-Office"
set dstaddr "Samba-Server"
set action accept
set schedule "always"
set service "SMB"
set logtraffic all
next
end
"""

def configure_firewall():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print("[+] Conectando al Fortigate...")
    client.connect(hostname, port=port, username=username, password=password)

    remote_shell = client.invoke_shell()
    time.sleep(1)

    print("[+] Enviando configuración...")
    for line in commands.strip().split('\n'):
        remote_shell.send(line + '\n')
        time.sleep(0.5)
        # Capturar y mostrar la respuesta del dispositivo
        output = remote_shell.recv(5000).decode('utf-8')
        print(output)

    print("[+] Configuración finalizada. Cerrando conexión...")
    remote_shell.close()
    client.close()

if __name__ == "__main__":
    configure_firewall()
