list = [1, 2, 3, 4, 5, 6]

#Вывод элементов списка по положительному индексу  
print(list[0]) #первый элемент списка
print(list[5]) #последний 
print()
index = int(input('Введите Элемент списка :'))

element = list[index]
print(element)

#Вывод элементов списка по отрицательному индексу и их сумма  
print()
pre_last = list[-2]
print(pre_last)

result = list[0] + list[-1]
print(result)


