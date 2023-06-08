# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

A = int(input('Введите число А '))
B = int(input('Введите число B '))

def exponentiation(a : int, b : int) -> float:
    if b > 1:
        return a * exponentiation(a, b-1)
    elif b < -1:
        return exponentiation(a, b + 1)/a
    elif b == 0:
        return 1
    elif b == -1:
        return 1 / a
    else: #т.е если b равняется 1
        return a

if A == 0 and B == 0:
    print('неопределённость')
else:
    print(exponentiation(A, B))
