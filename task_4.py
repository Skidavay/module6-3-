print('Задача 4. Календари')

# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.
 
# Напишите программу, которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля) и выводит ответ на экран.

month = int(input('Введите месяц: '))
summ = 0
while month != 0:
  if (month % 2) == 0:
    summ += 1
    month = int(input('Введите месяц: '))
    #print('количество четных месяцев:', summ)
  else:
    summ += 0
    month = int(input('Введите месяц: '))
    #print('количество четных месяцев:', summ) 
print('итого:', summ, 'четных месяцев')