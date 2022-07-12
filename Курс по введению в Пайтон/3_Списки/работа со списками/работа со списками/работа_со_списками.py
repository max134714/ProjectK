list = []
#добавляем в пустой список
list.append(3) 
list.append(5)

list.append(list[0] + list[1])

print(list)

#операция удаления
list = [2, 3, 4, 5, 6]
del list[2] #второй элемент удаляем 
print(list)

list[0] = 999 #заменяем 
print(list)


# обход элементов
for x in list:
    print('{} ^ 2 = {}'.format( x, x ** 2)) #квадрат каждого числа списка
