# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open("ospf.txt", "r") as config_file:
for config_line in config_file:
cleaned_line = config_line.replace(",", " ").replace(([", "").replace("]", "")
route_components = cleaned_line.split()
display_format = "/n{:25} {}" * 5

        print(display.format(
                "Prefix", route_components[1],
                "AD/Metric", route_components[2],
                "Next-Hop", route_components[4],
                "Last update", route_components[5],
                "Outbound Interface", route_components[6],
        ))
