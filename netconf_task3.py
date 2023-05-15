from ncclient import manager

device_ip = "172.16.24.20"
username = "admin"
password = "cisco"

interface_ip_config = '''
<config>
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
<interface>
<name>GigabitEthernet1</name>
<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
<address>
<ip>172.16.24.20</ip>
<netmask>255.255.255.0</netmask>
</address>
</ipv4>
</interface>
</interfaces>
</config>
'''

with manager.connect(host=device_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    m.edit_config(target='running', config=interface_ip_config)












