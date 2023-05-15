from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
ip_lst  = ["172.16.24.29","172.16.24.205"]
for ip in ip_lst:
    deviceinfo123 = {
        "device_type": "autodetect",
        "ip": "ip",
        "username": "admin",
        "password": "cisco"
    }
    guess123 = SSHDetect(**deviceinfo123)
    device_type = guess123.autodetect()
    print(device_type)
    if device_type == "cisco_ios":
        deviceinfo123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "admin",
            "password": "cisco"
        }
        ssh123 = ConnectHandler(**deviceinfo123)
        out123 = ssh123.send_command("show ip int br")
        print(out123)
    elif device_type == "juniper":
        deviceinfo123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "admin",
            "password": "cisco"
        }
        ssh123 = ConnectHandler(**deviceinfo123)
        out123 = ssh123.send_command("set xxxxxx")
        print(out123)
    elif device_type == "cisco_asa":
        deviceinfo123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "admin",
            "password": "cisco"
        }
        ssh123 = ConnectHandler(**deviceinfo123)
        out123 = ssh123.send_command("show ip int br")
        print(out123)
    elif device_type == "panos":
        deviceinfo123 = {
            "device_type": device_type,
            "ip": ip,
            "username": "admin",
            "password": "cisco"
        }
        ssh123 = ConnectHandler(**deviceinfo123)
        out123 = ssh123.send_command("show int ip br")
        print(out123)
    else:
        print("this i non-ssh based device,excluding"+ip)
