from netmiko import ConnectHandler
import os
# Prompt the user for device information and backup file location
ip_address = input("Enter device IP address: ")
username = input("Enter device username: ")
password = input("Enter device password: ")
backup_file = input("Enter backup file location: ")
# Connect to the device using Netmiko and backup its configuration
device = {"device_type": "cisco_ios",
          "ip": ip_address,
          "username": username,
          "password": password,
}
with ConnectHandler(**device) as net_connect:
    backup_config = net_connect.send_command("show run")
    # Write the backup configuration to the specified file172
with open(backup_file+'.txt',"w") as backup_file:
    backup_file.write(backup_config)