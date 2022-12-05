number = int(input('Введите число: '))
summ = 0
while number != 0:
  last_num = number % 10
  #print(last_num)
  summ += 1
  number //= 10
print('Количество цифр:', summ)