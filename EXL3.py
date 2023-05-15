from netmiko import ConnectHandler
import openpyxl as op
import csv
import re
import os
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

    x = ssh123.send_command("show version")
    y = ssh123.send_command("show run")
    z = ssh123.send_command("show processes memory sorted")
    hostname1234 = re.compile("(\S+)\s*uptime\s*is\s*")
    findhostname1234 = hostname1234.findall(x)
    print(findhostname1234[0])

    uptime123 = re.compile("uptime\s*is\s*(.+)")
    finduptime123 = uptime123.findall(x)
    print(finduptime123[0])

    version123 = re.compile("Version\s*(\S+),")
    findversion123 = version123.findall(x)
    print(findversion123[0])

    username123 = re.compile("username\s+(\S+)")
    findusername123 = username123.findall(y)
    print(findusername123[0])

    findtotalmem = re.compile("Total:\s*(\S+)")
    findtotalmem123 = findtotalmem.findall(z)
    print(findtotalmem123[0])

    findfreemem = re.compile("Free:\s*(\S+)")
    findfreemem1234 = findfreemem.findall(z)
    print(findfreemem1234[0])

    freememinpercentage = (int(findfreemem1234[0]) / int(findtotalmem123[0])) * 100
    print(freememinpercentage)

    file_exist123 = os.path.isfile(r"C:\Users\Student04\PycharmProjects\pythonProject1\fetch_regex.csv")
    if file_exist123:
        with open(r"C:\Users\Student04\PycharmProjects\pythonProject1\fetch_regex.csv", "a", newline="") as csv123:
            header123 = ["deviceip", "hostname1234", "finduptime123", "findversion123", "findusername123",
                                     "freememinpercentage"]
            csv1234 = csv.DictWriter(csv123, fieldnames=header123)
            csv1234.writeheader() # label is printed
            csv1234.writerow({"deviceip": deviceip,
            "hostname1234": findhostname1234[0],
            "finduptime123": finduptime123[0],
            "findversion123": findversion123[0],
            "findusername123": findusername123[0],
            "freememinpercentage": freememinpercentage})
    if not file_exist123:
        with open(r"C:\Users\Student04\PycharmProjects\pythonProject1\fetch_regex.csv", "a", newline="") as csv123:
            header123 = ["deviceip", "hostname1234", "finduptime123", "findversion123", "findusername123",
                                     "freememinpercentage"]
            csv1234 = csv.DictWriter(csv123, fieldnames=header123)
            csv1234.writeheader() # label is printed
            csv1234.writerow({"deviceip": deviceip,
                              "hostname1234": findhostname1234[0],
                              "finduptime123": finduptime123[0],
                              "findversion123": findversion123[0],
                              "findusername123": findusername123[0],
                              "freememinpercentage": freememinpercentage})
#
print("Job completed")