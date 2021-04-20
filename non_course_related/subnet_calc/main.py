import ipaddress

ip = ipaddress.ip_interface(input('Enter IP address in IP/Mask Form ie:(10.0.0.0/255.255.0.0 or 10.0.0.0/16) : '))

print(f"Network Address : {str(ip.network).split('/')[0]}")
print(f"Broadcast Address : {ip.network.broadcast_address}")
print(f"CIDR Notation :  {ip.with_prefixlen.split('/')[1]}")
print(f"Subnet Mask : {ip.with_netmask.split('/')[1]}")
print(f"Wildcard Mask : {ip.hostmask}")
print(f"First IP :  {ip.network[1]}")
print(f"Last IP :  {ip.network[-2]}")
print(f"Number of Unique Addresses : {ip.network.num_addresses -2}")
exit(0)

# 2001:db8::0/64