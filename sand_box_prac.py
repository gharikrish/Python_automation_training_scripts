from netmiko import ConnectHandler
deviceinfo123 = {
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxr-1.cisco.com",
    "username":"admin",
    "password":"C1sco12345"
}

ssh123 = ConnectHandler(**deviceinfo123)
mycmd = ["show run | i hostname","show ip int br","show clock","show ver"]
for slcmd in mycmd:
    output123 = ssh123.send_command(slcmd)
    print(output123)
print("job is success")

#-------------------------------------------------------------------------------
