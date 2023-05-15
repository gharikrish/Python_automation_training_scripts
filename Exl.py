from netmiko import ConnectHandler
import openpyxl as op
wb = op.load_workbook("read_from_excel.xlsx")
sh = wb['chennai']
for singeldevice in range(2,sh.max_row + 1):
    c = str(singeldevice)
    hostname = sh['B' + c].value
    print(hostname)
    deviceip = sh['C' + c].value
    print(deviceip)
    devicetype = sh['D' + c].value
    print(devicetype)
    user123 = sh['E' + c].value
    print(user123)
    pass123 = sh['F' + c].value
    print(pass123)
    config123 = sh['G' + c].value
    listconfig123 = config123.splitlines()
    print(listconfig123)
    #
    deviceinfo123 = {
        "device_type": devicetype,
        "ip": deviceip,
        "username": user123,
        "password": pass123
    }
    ssh123 = ConnectHandler(**deviceinfo123)
    output123 = ssh123.send_command("show ip int br")
    print(output123)
    pushconfig123 = ssh123.send_config_set(listconfig123)
    print(pushconfig123)
    # capturelogmsgs
    openblanknotepad = open( deviceip + "-" + hostname + ".txt",
                            "w")
    copycontent = openblanknotepad.write(pushconfig123)
    openblanknotepad.close()
#
print("Job completed")




    # print(sh['B' + c].value)
    # print(sh['C' + c].value)
    # print(sh['D' + c].value)
    # print(sh['E' + c].value)
    # print(sh['F' + c].value)
    # print('--++--')