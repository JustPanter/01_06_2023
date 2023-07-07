# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def number_degree(num, deg):
    if deg == 1:
        return num
    return num * number_degree(num , deg - 1)

num = int(input("Введите число, которое необходимо возвести в степень: "))
deg = int(input("В какую степень возвести введеное число? "))
print(f"{num} в степени равной {deg} = {number_degree(num,deg)}")