# Среднегодовая температура
'''
a = 'london', 'Moscow', 'Paris'

b = ['Russia', 'United Kingdom', 'France']

print(len(a))
'''

tsred = 0
temp = []
for i in range(12):
    a = float(input('Введите значение температуры: '))
    temp.insert(i, a)

for o in temp:
    tsred += o

print(temp)
print(tsred/12)
