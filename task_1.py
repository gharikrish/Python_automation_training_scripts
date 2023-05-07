import csv
from netmiko import ConnectHandler
# Create a list of devices to connect to
devices = [{"device_type": "cisco_ios",
            "ip": "172.16.24.54",
            "username": "admin",
            "password": "cisco",
            },
           {"device_type": "cisco_ios",
            "ip": "172.16.24.51",
            "username": "admin",
            "password": "cisco",
            },
# Add more devices as needed
]
# Open a CSV file to store the collected information
with open("network_device_inventory.csv","w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write headers to the CSV file
    csv_writer.writerow(["Hostname", "IP Address", "Interfaces", "VLANs"])
    # Connect to each device and collect information
    for device in devices:
        with ConnectHandler(**device) as net_connect:
            hostname = net_connect.send_command("show run | i hostname").split()[-1]
            ip_address = device["ip"]
            interfaces = net_connect.send_command("show ip interface brief")
            vlans = net_connect.send_command("show vlan brief")
            # Write the collected information to the CSV file
            csv_writer.writerow([hostname, ip_address, interfaces,vlans])