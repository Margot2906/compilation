
import os
import re
filename = os.path.join('TP1', 'dictionary.txt')
with open(filename, 'r', encoding='utf-8') as file:
    regex_ion = re.compile(r'.*ion$')
    regex_at = re.compile(r'.*at[^irt].*$|.*at$')
    list_ion = []
    list_at = []
    for line in file:
        line = line.strip()
        if regex_ion.match(line):
            list_ion.append(line)
        if regex_at.match(line):
            list_at.append(line)
    # print(list_ion)
    print(len(list_ion))
    # print(list_at)
    print(len(list_at))

# Résultat : 2096 et 7206 normalement.