# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]
config_file_name = argv[1]
with open(config_file_name) as configuration_file:
for config_line in configuration_file:
if not config_line.startwith("!"):
line_words = config_line.split()
forbidden_words_present = any(word in ignore for word in line_words)
if not forbidden_words_present:
print(config_line.rstrip())
