from ncclient import manager

device_ip = "172.16.24.20"
username = "admin"
password = "cisco"

interfaces_filter = '''
<filter>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface/>
</interfaces>
</filter>
'''

with manager.connect(host=device_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    response = m.get_config(source='running', filter=interfaces_filter)
    print(response.xml)