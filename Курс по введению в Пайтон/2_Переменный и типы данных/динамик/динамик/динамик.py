#Вывод строки с помощью type
x = 'строка'
print(x)
print(type(x))

print()

#Вывод числа с помощью type
x = 139
print(x)
print(type(x)) 

print()

q=5
w=5
print(q+w)

print()

w='5'

try:            #пытаемся произвести сложение
    print(q+w)
except TypeError:   # если не получается 
    print('w не число, не можем сложисть с q')

