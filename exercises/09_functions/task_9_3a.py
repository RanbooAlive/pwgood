# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
access_interfaces = {}
trunk_interfaces = {}
with open(config_filename) as config_file:
current_port = ""
for config_line in config_file:
config_line = config_line.rstrip()
if config_line.startswith("interface FastEthernet"):
current_port = config_line.split()[1]
access_interfaces[current_port] = 1
elif "switchport access vlan" in config_line:
vlan_id = int(config_line.split()[-1])
access_interfaces[current_port] = vlan_id
elif "switchport trunk allowed vlan" in config_line:
vlan_numbers = [int(vlan) for vlan in config_line.split()[-1].split(",")]
trunk_interfaces[current_port] = vlan_numbers
del access_interfaces[current_port]
return access_interfaces, trunk_interfaces
