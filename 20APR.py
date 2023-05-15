# from netmiko import ConnectHandler
# deviceinfo123 = {
#     "device_type":"cisco_ios",
#     "ip":"172.16.24.229",
#     "username":"admin",
#     "password":"cisco"
# }
#
# ssh123 = ConnectHandler(**deviceinfo123)
# output123 = ssh123.send_command("show ip int br")
# print(output123)


from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip":"172.16.24.202",
    "username":"admin",
    "password":"cisco"
}

connect = ConnectHandler(**device)
output = connect.send_command("show ip int br")
print(output)