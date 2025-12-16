# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

source_filename, target_filename = argv[1], argv[2]
with open(source_filename) as source_file, open(target_filename, 'w') as output_file:
for config_line in source_file:
if not config_line.startswith("!"):
line_words = config_line.split()
has_forbidden_words = any(word in ignore for word in line_words)
if not has_forbidden_words:
output_file.write(config_line)
