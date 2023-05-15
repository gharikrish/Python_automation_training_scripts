from ncclient import manager

device_ip = "172.16.24.229"
username = "admin"
password = "cisco"

with manager.connect(host=device_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    running_config = m.get_config(source="running")
    print(running_config.xml)