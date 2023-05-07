from netmiko import ConnectHandler
import os

# Prompt the user for device information and troubleshooting rules
ip_address = input("Enter device IP address: ")
username = input("Enter device username: ")
password = input("Enter device password: ")
interface_down_action = input("Enter action for down interfaces (up, shut): ")
config_error_action = input("Enter action for configuration errors (fix, ignore): ")
# Connect to the device using Netmiko and perform troubleshooting
device = {
    "device_type": "cisco_ios",
    "ip": ip_address,
    "username": username,
    "password": password,
}
with ConnectHandler(**device) as net_connect:
# Check for down interfaces
    down_interfaces = net_connect.send_command("show ip interface brief | i down")
    if down_interfaces:
        if interface_down_action == "up":
            up_commands = [f"interface {interface}", "no shutdown"]
            for interface in down_interfaces.splitlines():
                net_connect.send_config_set(up_commands)
        elif interface_down_action == "shut":
            shut_commands = [f"interface {interface}", "shutdown"]
            for interface in down_interfaces.splitlines():
                net_connect.send_config_set(shut_commands)
    # Check for configuration errors
    config_errors = net_connect.send_command("show running-config | include ^!|\\s{2,}")
    if config_errors:
        if config_error_action == "fix":
            config_commands = [line.strip() for line in config_errors.splitlines() if not line.startswith("!")]
            net_connect.send_config_set(config_commands)
        elif config_error_action == "ignore":
            pass