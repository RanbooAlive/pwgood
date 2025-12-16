# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
requested_vlan = input("Введите номер VLAN: ")
with open("CAM_table.txt) as config_file:
for entry in config_file:
entry_components = entry.split()
if entry_components = entry.split()
if entry_components and entry_components[0].isdigit() and entry_components[0] == requested_vlan:
vlan_id, mac_address, _, port = entry_components
print)f"{vlan_id:9}{mac_address:20}{port}")
