# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import lib

def start_task():
    print('\nЗадача 5: Расстояние между 2 точками(2D)\n' +
          'Напишите программу, которая принимает на вход'+
          ' координаты двух точек и находит расстояние'+
          ' между ними в 2D пространстве.')
    line = lib.Line()
    line.print_info()