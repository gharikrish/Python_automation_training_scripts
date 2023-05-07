# import csv
# from netmiko import ConnectHandler
# # Create a list of devices to connect to
# devices = [{"device_type": "cisco_ios",
#             "ip": "172.16.24.54",
#             "username": "admin",
#             "password": "cisco",
#             },
#            {"device_type": "cisco_ios",
#             "ip": "192.168.1.2",
#             "username": "admin",
#             "password": "password",
#             },
# # Add more devices as needed
# ]
# # Open a CSV file to store the collected information
# with open("network_health_check.csv", "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     # Write headers to the CSV file
#     csv_writer.writerow(["Device", "Connectivity", "Interface Status", "Network Performance", "Issues"])
#     # Connect to each device and perform health check
#     for device in devices:
#         with ConnectHandler(**device) as net_connect:
#         # Check device connectivity
#             try:
#                 ping_output = net_connect.send_command("ping 8.8.8.8")
#                 connectivity = "Success" if "!" in ping_output else "Failed"
#             except:
#                 connectivity = "Failed"
#                 # Check interface status
#                 interface_status = net_connect.send_command("show ip interface brief")
#                 # Test network performance
#                 network_performance = net_connect.send_command("ping 192.168.1.1 repeat 100")
#                 # Identify potential issues
#                 issues = ""
#                 if "down" in interface_status:
#                     issues += "Interface Down; "
#                 if "Success rate is 0 percent" in network_performance:
#                     issues += "Network Performance Issues; "
#                 # Write the collected information to the CSV file
#                 csv_writer.writerow([device["ip"], connectivity, interface_status, network_performance, issues])



# from netmiko import ConnectHandler
#
# device = {
#     "device_type" : "cisco_ios",
#     "ip" : "172.16.24.40",
#     "username" : "admin",
#     "password" : "cisco"
# }
#
# connect = ConnectHandler(**device)
# output = connect.send_command("show ip int br")
# print(output)
# print(connect.send_command("show version"))
# print(connect.send_command("show ip int brief"))

from netmiko import ConnectHandler

class device:
    def __init__(self,device_type,ip,username,password):
        self.device_info = {
            "device_type":device_type,
            "ip":ip,
            "username":username,
            "password":password
        }
        self.connect = ConnectHandler(**self.device_info)

    def op(self):
        print(self.connect.send_command("show command"))

obj = device('cisco_ios','172.16.24.40','admin','cisco')
obj.op()