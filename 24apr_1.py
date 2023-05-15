from netmiko import ConnectHandler
import xlrd
import re

workbook123 = xlrd.open_workbook(r"C:\Users\Student04\PycharmProjects\pythonProject1\read_from_excel.xlsx")

sheet123 = workbook123.sheet_by_name("Chennai")
for singledevice in range(1,sheet123.nrows):
    hostname = sheet123.row(singledevice)[1].value
    print(hostname)
    deviceip = sheet123.row(singledevice)[2].value
    print(deviceip)
    devicetype = sheet123.row(singledevice)[3].value
    print(devicetype)
    user123 = sheet123.row(singledevice)[4].value
    print(user123)
    pass123 = sheet123.row(singledevice)[5].value
    print(pass123)
    config123 = sheet123.row(singledevice)[6].value
    listconfig123 = config123.splitlines()
    print(listconfig123)
    #
    deviceinfo123 = {
        "device_type":devicetype,
        "ip": deviceip,
        "username": user123,
        "password": pass123
    }
    ssh123 = ConnectHandler(**deviceinfo123)
    output123 = ssh123.send_command("show ip int br")
    print(output123)
    pushconfig123 = ssh123.send_config_set(listconfig123)
    print(pushconfig123)
    #capturelogmsgs
    openblanknotepad = open(r"C:\Users\Student04\PycharmProjects\pythonProject1" + deviceip + "-" + hostname + ".txt", "w")
    copycontent = openblanknotepad.write(pushconfig123)
    openblanknotepad.close()
#
print("Job completed")