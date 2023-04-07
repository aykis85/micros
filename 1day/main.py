# Алексей Рюмин

## Урок №1, Задание №1
'''
Напишите программу, которая спрашивает имя пользователя и затем приветствует его.
'''
# Вариант 1
# name = input('Введите ваше имя: ')
# print('Привет, ' + name)

# Вариант 2
# print('Привет, ' + input('Введите имя: '))

## Урок №1, Задание №2
'''
Напишите программу, которая считывает три числа и выводит их сумму.
'''
# Вариант 1
# print('Сумма чисел 50, 20 и 30 равно 100')

# Вариант 2
# val1 = 50
# val2 = 20
# val3 = 30
# summ = val1 + val2 + val3
# print(f'Сумма чисел {val1}, {val2} и {val3} равно {summ}')

# Вариант 3
# num1 = input('Введите число 1: ')
# num2 = input('Введите число 2: ')
# num3 = input('Введите число 3: ')
# print(f'Сумма числе {num1}, {num2} и {num3} равно' + ' ' + str(int(num1) + int(num2) + int(num3)))

# Вариант 2
# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))
# num3 = int(input('Введите число 3: '))
# print(int(num1) + int(num2) + int(num3))
# print(f'Сумма числе {num1}, {num2} и {num3} равно' + ' ' + str(num1 + num2 + num3))

## Урок №1, Задание №3
'''
Напишите программу, для решения следующей задачи: n школьников делят k яблок поровну, неделящийся остаток остается
в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
'''
# Вариант 1
# n = input('Количество яблок: ')
# k = input('Количество школьников: ')
# print('Яблок у каждого школьника: ' + str(int(n) // int(k)))
# print('Осталось яблок в корзине: ' + str(int(n) % int(k)))

# Вариант 2
# n = int(input('Количество яблок: '))
# k = int(input('Количество школьников: '))
# print('Яблок у каждого школьника: ' + str(n // k))
# print('Осталось яблок в корзине: ' + str(n % k))

# Вариант 3
# n = int(input('Количество яблок: '))
# k = int(input('Количество школьников: '))
# children = n // k
# apple = n % k
# print(f'Яблок у каждого школьника: {children}')
# print(f'Осталось яблок в корзине: {apple}')

## Урок №1, Задание №4
'''
Напишите программу, которая спрашивает число у пользователя и выводит следующее.
'''
# num = int(input('Введите число: '))
# print(f'Следующее число для {num} --> {num + 1}')
# print(f'Предыдущее число для {num} --> {num - 1}')

## Урок №1, Задание №5
'''
Напишите программу, которая выводит текст в данном формате.
'''
'''Twinkle, twinkle, little star,
    How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
    Twinkle, twinkle, little star,
            How I wonder what you are!         
'''
# Вариант 1
# print(
# '''
# Twinkle, twinkle, little star,
#     How I wonder what you are!
#             Up above the world so high,
#             Like a diamond in the sky.
# Twinkle, twinkle, little star,
#         How I wonder what you are!
# '''
#      )

# Вариант 2
# print('Twinkle, twinkle, little star,\n    '
#       'How I wonder what you are!\n\t\t    '
#       'Up above the world so high,\n\t\t    '
#       'Like a diamond in the sky.\n'
#       'Twinkle, twinkle, little star,\n\t\t'
#       'How I wonder what you are!'
#       )

## Урок №1, Задание №6
'''
Напишите программу для использования метода форматирования следующих трех переменных в соответствии с ожидаемым 
результатом.  
'''

# Вариант 1
# print('У меня есть %s долларов, поэтому я могу купить %s футбольных мяча за %s долларов' % (1000, 3, 450))

# Вариант 2
# totalMoney = 1000
# quantity = 3
# price = 450
# print(f'У меня есть {totalMoney} долларов, поэтому я могу купить {quantity} футбольных мяча за {price} долларов')

# Вариант 3
# print('У меня есть '
#       + str(totalMoney)
#       + ' '
#       + 'долларов, поэтому я могу купить'
#       + ' '
#       + str(quantity)
#       + ' '
#       + 'футбольных мяча за'
#       + ' '
#       + str(price)
#       + ' '
#       + 'долларов'
#       )

## Урок №1, Задание №7
'''
Создайте две переменных, со значением ‘spam’ и ‘eggs’, затем распечатайте объединив две переменной в одну целую
'''
# Вариант 1
# a = 'spam'
# b = 'eggs'
# c = a + b
# print(c)
# print(a + b)
# print(f'{a}{b}')
# print('{}{}'.format(a,b))

# Вариант 2
# print('{}{}'.format('spam','eggs'))
# print(f'{"spam"}{"eggs"}')

# Вариант 3
# print('spam', end='')
# print('eggs')

# конец