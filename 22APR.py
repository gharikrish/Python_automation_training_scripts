# from netmiko import ConnectHandler
# class CiscoDevice:
#     def __init__(self,device_type,ip,username,password):
#         self.device_info = {
#             "device_type":device_type,
#             "ip":ip,
#             "username":username,
#             "password":password
#         }
#         self.connection = ConnectHandler(**self.device_info)
#     def send_command(self,commands):
#         for sle_cmd in commands:
#             output = self.connection.send_command(sle_cmd)
#             print(output)
#
# device1 = CiscoDevice("cisco_ios","172.16.24.29","admin","cisco")
# commands = ["show run | i hostname","show ip int br","show ver","show clock"]
# device1.send_command(commands)
# print("job is success")

#
# # #----------------------------------------------------------------------------------------
# from netmiko import ConnectHandler
# deviceinfo123 = {
#     "device_type":"cisco_ios",
#     "ip":"172.16.24.29",
#     "username":"admin",
#     "password":"cisco"
#     }
# ssh123 = ConnectHandler(**deviceinfo123)
# my_cmd = input("pls enter the interface id")
# check_inter = ssh123.send_command("show ip int br" + my_cmd)
# if "up" and "up" in check_inter:
#     print(my_cmd + "is already up")
#     y = ssh123.send_config_set(["interface"+ my_cmd ,"shutdown","desc**reserved for CR12345*"])
#     print(y)
# else:
#     print(my_cmd + "is down")
#output123 = ssh123.send_command("show ip int br")
#print(output123)
#
# #----------------------------------------------------------------------------
from netmiko import ConnectHandler,NetmikoTimeoutException,NetmikoAuthenticationException
mul_dev = ["171.16.24.29"]
for single_dev in mul_dev:
    deviceinfo123 = {
        "device_type": "cisco_ios",
        "ip": single_dev,
        "username": "admin1",
        "password": "cisco7"
    }
    try:
        ssh123 = ConnectHandler(**deviceinfo123)
        print("taking connection to" + single_dev + "#" * 10)
        output123 = ssh123.send_command("show ip int br")
        print(output123)
    except NetmikoAuthenticationException:
        print(single_dev," ","failing due to cred issuue")
        err_file = open("authentication_failed.txt","a")
        err_file.write(single_dev + "\n")
        err_file.close()
        pass
    except NetmikoTimeoutException:
        print(single_dev, " ", "failing due to time out issue")
        err_file = open("Time_out_failed.txt", "a")
        err_file.write(single_dev + "\n")
        err_file.close()
        pass
print("job completed")
