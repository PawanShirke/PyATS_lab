from genie.testbed import load
tb = load('mock.yaml')

dev = tb.devices['nx-osv-1']
dev.connect(log_stdout=False)


#get_version = dev.parse('show version')
#version = get_version["platform"]["software"]["system_version"]
#print(get_version)


get_inventory = dev.parse('show inventory ')
inventory = get_inventory.get("name")
print(inventory)

for elements in inventory:
    sn = inventory[elements].get("serial_number", 'DOSE NOT EXIST')
    print(f'Name of the Component: {elements} ||  Serial Number of the component: {sn}')