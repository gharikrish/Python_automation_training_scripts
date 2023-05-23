from netmiko import ConnectHandler

device = {
    "device_type":"cisco_ios",
    "ip":"172.16.24.127",
    "username":"admin",
    "password":"cisco"
}

connect = ConnectHandler(**device)


f = open('cmds1.txt','r')
c = 0
for line in f.readlines():
    v = line.split('\n')
    out = connect.send_command(v[0])
    c_v = out
    if c_v == '% Invalid input detected at \'^\' marker.':
        pass
    else:
        with open(v[0]+".txt",'a') as yo:
            yo.write(c_v)
        yo.close()
f.close()
