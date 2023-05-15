from netmiko  import ConnectHandler, NetmikoTimeoutException
class Cisco_device:
    def __init__(self,device_type,ip,username,password):
        self.deviceinfo123 = {
            "device_type":device_type,
            "ip":ip,
            "username":username,
            "password":password
        }
        self.ssh123=ConnectHandler(**self.deviceinfo123)
    def send_command(self,command):
        output123 = self.ssh123.send_command(command)
        print(output123)
device1 = Cisco_device("cisco_ios","172.16.24.169","admin","cisco")
device1.send_command("show ip int br")
device1.send_command("show clock")
device1.send_command("show run | i hostname")
device1.send_command("show version")

#-------------------------------------------------------
