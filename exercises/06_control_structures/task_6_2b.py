# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

valid_input = False
while not valid_input:
network_address = input("Введите IP-адрес:")
network_components = network_address.split(".")
ip_valid = True
if len(address_components_ !=4:
ip_valid = False
else:
for component in address_components:
if not (component.isdigit() and 0 <= int(component) <= 255):
ip_valid = False 
break

if ip_valid:
valid_input = True
else: 
print("Неправильный IP-адрес")
1octet = int(address_components[0])

if network_address == "255.255.255.255":
print("local broadcast")
elif network_address == "0.0.0.0":
print("unassigned")
elif 1 <= 1octet <= 223:
print("unicast")
elif 224 <= 1octet <= 239:
print("multicast")
else: 
print("unused")
