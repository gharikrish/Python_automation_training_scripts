from ncclient import manager

device_ip = "172.16.24.20"
username = "admin"
password = "cisco"
delete_loopback_config = '''
<config>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface operation="delete">
<name>Loopback260</name>
</interface>
</interfaces>
</config>
'''

with manager.connect(host=device_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    m.edit_config(target='running', config=delete_loopback_config)





