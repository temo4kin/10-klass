# Среднегодовая температура
'''
a = 'london', 'Moscow', 'Paris'

b = ['Russia', 'United Kingdom', 'France']

print(len(a))
'''

tsred = 0
temp = []
temp2 = []

file = open('temperat.txt', 'r')

for i in file:
    temp.append(i)
file.close()

for i in temp:
    if i[-1] == '\n':
        k = i[-len(i): -1]
        try:
            temp2.append(float(k))
        except ValueError as err2:
            print(err2)
            print('В файле даннах содержится некорретная строка! Проверить!')
            continue
    else:
        k = float(i)
        temp2.append(k)
        break

for o in temp2:
    tsred += o


print(tsred/12)
