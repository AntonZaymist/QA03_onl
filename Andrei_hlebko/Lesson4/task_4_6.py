#1 Создать список из элементов list_a = [1,2,3,4,4,5,2,1,8]
#2 Вывести только уникальные значения и сохранить их в отдельную переменную
#3 Добавить в полученный объект значение 22
#4 Сделать list_a неизменяемым
#5 Измерить его длинну

list_a = [1,2,3,4,4,5,2,1,8]#1

list_uniq = {*list_a}#2
print(list_uniq)#2

list_uniq.add(22)#3

list_uniq = tuple(list_uniq)#4

print(len(list_uniq))#5
