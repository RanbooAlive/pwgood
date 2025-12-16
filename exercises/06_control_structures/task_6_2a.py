# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network_address = input("Введите IP-адрес:")
address_parts = network_address.split(".")
valid_address = True
if len(address_parts != 4:
valid addresses = False
else:
for part in address_parts: 
if not (part.isdigit() and 0 <= int(part) <= 255):
valid_address = False
break
if not valid_address
print("неправильный IP-адрес")
else:
1octet = int(address_parts[0])
if network_address = "255.255.255.255":
print("local broadcast")
else network address == "0.0.0.0":
print("unassigned")
elif 1 <= 1octet <= 223:
print("unicast")
elif 224 <=1octet <= 239:
print("multicast")
else:
print("unused")
