# Среднегодовая температура
'''
a = 'london', 'Moscow', 'Paris'

b = ['Russia', 'United Kingdom', 'France']

print(len(a))
'''

temp = []
for i in range(12):
    a = float(input('Введите значение температуры: '))
    temp.insert(i, a)

print(temp)
