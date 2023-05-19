# from pyats.topology import loader
# from genie.libs.ops.ospf.ios.ospf import Ospf
# from genie.libs.parser.utils import get_parser
#
# # Load testbed file
# testbed = loader.load('/home/student04/yaml/my_testbed1.yaml')
# mydevices = ["rout_1", "rout_2"]
# for x in mydevices:
#     device = testbed.devices[x]
#     # Connect to the device
#     device.connect()
#
#     # Create an OSPF object and learn OSPF state
#     ospf = Ospf(device)
#     ospf.learn()
#
#     # Access the default VRF OSPF areas \\debug
#     ospf_vrf = ospf.info['vrf']['default']
#     print(ospf_vrf)
#     ospf_instances = ospf_vrf.get('address_family', {}).get('ipv4', {}).get('instance', {})
#     print(ospf_instances)
#
#     # Perform validation tests
#     for instance_id, instance_data in ospf_instances.items():
#         ospf_areas = instance_data.get('areas', {})
#         for area, area_data in ospf_areas.items():
#             for intf, data in area_data['interfaces'].items():
#                 print(f"Interface: {intf}, Data: {data}")
#                 # Check if the interface is a sham-link
#                 if intf.startswith('SL'):
#                     continue # Skip validation tests for sham-link interfaces
#                 if not data.get('enable'):
#                     print(f"OSPF not enabled on {intf}")
#                 else:
#                     #assert area == '0.0.0.0', f"Interface {intf} not in Area 0"
#                     assert data['state'] == 'point-to-point', f"Interface {intf} not in point-to-point state"


from genie.testbed import load

# Load the testbed file
testbed = load('/home/student04/yaml/my_testbed.yaml')

# Connect to the device
device = testbed.devices['CSR_1']
device.connect()

# Execute the show command to retrieve the static route information
output = device.execute('show ip route static')

# Parse the output using the Genie parse method
parsed_output = device.parse('show ip route static')
print(parsed_output)
# Access the static_routes dictionary from parsed_output
static_routes = parsed_output['vrf']['default']['address_family']['ipv4']['routes']

for route, route_info in static_routes.items():
    if route_info['source_protocol'] == 'static':
        if 'next_hop_list' in route_info['next_hop']:
            for index, next_hop_info in route_info['next_hop']['next_hop_list'].items():
                #Test: Ensure the administrative distance is correct
                assert route_info['route_preference'] == 1, f"Incorrect administrative distance for route {route}"

                #Test: Ensure the next-hop IP address is valid
                assert '0.0.0.0' not in next_hop_info['next_hop'], f"Invalid next-hop IP address for route {route}"

    # Test: Ensure the outgoing interface is valid, if present
    if 'outgoing_interface' in route_info['next_hop']:
        for interface_name, interface_info in route_info['next_hop']['outgoing_interface'].items():
            assert interface_info['outgoing_interface'] != '', f"Invalid outgoing interface for route {route}"

            print(f"All tests passed for route {route}")

# Disconnect from the device
device.disconnect()