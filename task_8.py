print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

contribution = int(input('Введите сумму вклада: '))
percent = int(input('Введите процентную ставку: '))
total = int(input('Введите желаемую сумму: '))
year = 0
while contribution < total:
  contribution *= 1 + percent / 100
  contribution = int(contribution)
  year += 1
print('потребуется',year, 'лет')