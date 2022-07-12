k = float(input('1 namber: '))
t = float(input('2 namber: '))
oper = input('Oper: ')

result = None

if oper == '+':
    result = k + t
elif oper =='-':
    resultn= k - t
elif oper == '*':
    resultn= k * t
elif oper == '/':
    resultn= k / t
else:
    print('errore')

if result is not None:
    print('Result:', result)

