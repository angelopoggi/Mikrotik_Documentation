###################
#MikroTik Documenter
#By: A. Poggi
#apoggi226@gmail.com
#
###################

from librouteros import connect
from librouteros.login import login_plain, login_token
# to ask for passwords from users without it echoing on terminal
# need to check if this encrypts data or secures it somehow>>>
import getpass


print("connecting to firewall now")

firewall = input("Enter Firewall name or IP:\n")
username = input("Enter Username:\n")
password = getpass.getpass("Enter Password:\n")

try:
    api = connect(username=username, password=password,
                  host=firewall, port=8728, login_plain=True)
except:
    print("Incorrect firewall, username or password")


#Variable to easily call information when needed
list_interface = api(cmd='/interface/print')
nat_rules = api(cmd='/ip/firewall/nat/print')
address_list = api(cmd='/ip/firewall/address-list/print')
firewall_rules = api(cmd='/ip/firewall/filter/print', stats=False)
hostname = api(cmd='/system/identity/print')
system_id = api(cmd='/system/license/print')
ip_addr = api(cmd='/ip/address/print')

# Print out the hostname of the Server
print('{:^20}:{:^20}'.format('System Name',hostname[0]['name']))
print('-'*80)
#print('{:^20}'.format(hostname[0]['name']))
print('{:^20}:{:^20}'.format('System ID','Sofware ID CCR'))
# Print out the system ID - associated with CHR key
system_id_results = []
for item in system_id:
    system_id_results.append({
        'system-id': item.get('system-id', 'N/A'),
        'software-id': item.get('software-id', 'N/A')
    })
for data in system_id_results:
    print('{:^20}:{:^20}'.format(data['system-id'],data['software-id']))
print('-'*80)



#Print out interface Name, mac and burned in name
print('{:^20}:{:^20}:{:^20}'.format('Interface Nick-Name','MAC Address','Interface Name'))
print('-'*80)

interface_results = []

for item in list_interface:
    interface_results.append({
        'name' : item.get('name', 'N/A'),
        'mac-address' : item.get('mac-address', 'N/A'),
        'default-name': item.get('default-name', 'N/A')
        })

for data in interface_results:
    print('{:^20}:{:^20}:{:^20}'.format(data['name'], data['mac-address'], data['default-name']))
print('-'*80)

print('{:^20}:{:^20}'.format('Interface', 'IP Address'))
print('-'*80)

for data in ip_addr:
    print('{:^20}{:^20}'.format(data['interface'],data['address']))
print('-'*80)

#print Nat rules
print('{:^20}{:^20}{:^20}{:^20}'.format('Chain','Action','Source Address','Translated Address'))
print('-'*80)

nat_results = []
for item in nat_rules:
    nat_results.append({
        'chain': item.get('chain', 'N/A'),
        'action': item.get('action', 'N/A'),
        'src-address': item.get('src-address', 'N/A'),
        'to-address': item.get('to-address', 'N/A'),
        'comment': item.get('comment', 'N/A')
        })

for data in nat_results:
    print('{:^20}{:^20}{:^20}{:^20}'.format(data['chain'],data['action'],data['src-address'],data['to-address']))


#Print Address list
print('-'*80)
print('{:^20}{:^20}'.format('Address list', 'IP Address'))
print('-'*80)
for data in address_list:
    print('{:^20}{:^20}'.format(data['list'],data['address']))
print('-'*80)

# For firewall rules, print everything, since this information is usefule and each firewall
# Will have unique information
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('Rule #','Chain','Src.','Dst.','Proto.',
                                                            'comment','Action'))
print('-'*80)



#create an array called results
#look for certain keys, if the key does not exsist, we replace it with N/A
result = []
for item in firewall_rules:
    result.append({
        '.id': item.get(".id", ""),
        'chain': item.get("chain", "N/A"),
        'protocol': item.get("protocol", "N/A"),
        'src-address': item.get("src-address", "N/A"),
        'dst-address': item.get("dst-address", "N/A"),
        'comment' : item.get("comment", "N/A"),
        'action' : item.get("action", 'N/A')
        })

#print and format result list
for data in result:
    print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format(data['.id'],data['chain'],data['src-address'],
                                                                data['dst-address'],data['protocol'],data['action'],data['comment']))
