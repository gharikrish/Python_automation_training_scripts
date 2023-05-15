from netmiko import ConnectHandler, NetmikoAuthenticationException , NetMikoAuthenticationException

file = open("device.txt","r")
ab = file.readlines()
print(ab)
file1 = open("cred.txt","r")
ab1 = file1.readlines()
print(ab1)
user = ab1[0]
pass1 = ab1[1]

for single_dev in ab:
    start = 1
    while start < 5:
        try:
            deviceinfo123 = {
                "device_type": "cisco_ios",
                "ip": single_dev,
                "username": "user",
                "password": "pass1"
            }
            ssh123 = ConnectHandler(**deviceinfo123)
            hostname123 = ssh123.find_prompt()
            print(hostname123)
            if ">" or "#" in hostname123:
                print("login to" + single_dev + "is successfully")
                print("taking connection to "+ single_dev + "#"*10)
                output123 = ssh123.send_command("show ip int br")
                print(output123)
                break
            else:
                pass
        except NetmikoAuthenticationException:
            print(single_dev, " ", "failing due to cred issuue")
            err_file = open("authentication_failed.txt", "a")
            err_file.write(single_dev + "\n")
            err_file.close()
            pass
        except NetmikoTimeoutException:
            print(single_dev, " ", "failing due to time out issue")
            err_file = open("Time_out_failed.txt", "a")
            err_file.write(single_dev + "\n")
            err_file.close()
            pass
        print(start)
        start = start + 1
print("job completed")
