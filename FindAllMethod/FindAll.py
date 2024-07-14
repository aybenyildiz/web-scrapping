import re

total = 0
x = open('regex_sum_2049419.txt')

for line in x:
    line = line.strip()
    stuff = re.findall('[0-9]+', line)
    res = [eval(i) for i in stuff]
    total += sum(res)
print(total)