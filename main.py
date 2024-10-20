spisokNumb = [2, 4, 8, 44, 13, 9, 66]# Список чисел
max_num = spisokNumb[0] # Предположим, что первый элемент максимальный
i = 1 # Присвоение значения

while i < len(spisokNumb): # Цикл while
    if spisokNumb[i] > max_num: # Сравнение
        max_num = spisokNumb[i] # Присваивание ,если максимальное значение меньше 
    i += 1 # Увеличение i
print(f"Максимальное число  : {max_num}") # Вывод числа

