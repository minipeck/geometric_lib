# Общее описание решения
Geometric_lib - это библиотека, созданная для работы с геометрическими фигурами: circle, square, triangle. Она написана на языке Python. С помощью нее можно считать площадб и периметр этих фигур.

Библиотека состоит из нескольких частей. Каждая часть отвечает за определенную фигуру. Функции этих частей могут быть использованы другими частями программы.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

#Описание каждой функции с примерами вызова.

## Triangle
area:
        Вычисляет полупериметр треугольника по длинам его сторон.

        Параметры:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

        Возвращает:
        float: Полупериметр треугольника.

        Пример вызова:
        >>> area(3, 4, 5)
        6.0`
        
perimeter:
        Вычисляет периметр треугольника по длинам его сторон.

        Параметры:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

        Возвращает:
        float: Периметр треугольника.

        Пример вызова:
        >>> perimeter(3, 4, 5)
        12.0


## Square
area:
        Вычисляет площадь квадрата по длине его стороны.

        Параметры:
        a (float): Длина стороны квадрата. Должна быть положительным числом.

        Возвращает:
        float: Площадь квадрата.

        Пример вызова:
        >>> area(5)
        25.0

perimeter:
        Вычисляет периметр квадрата по длине его стороны.

        Параметры:
        a (float): Длина стороны квадрата. Должна быть положительным числом.

        Возвращает:
        float: Периметр квадрата.

        Пример вызова:
        >>> perimeter(5)
        20.0

## Circle
area:
        Вычисляет площадь круга по его радиусу.

        Параметры:
        r (float): Радиус круга. Должен быть положительным числом.

        Возвращает:
        float: Площадь круга.

        Пример вызова:
        >>> area(5)
        78.53981633974483

perimeter:
        Вычисляет периметр (длину окружности) круга по его радиусу.

        Параметры:
        r (float): Радиус круга. Должен быть положительным числом.

        Возвращает:
        float: Периметр круга.

        Пример вызова:
        >>> perimeter(5)
        31.41592653589793

## Calculate
calc:
	   Вычисляет заданную функцию (периметр или площадь) для указанной фигуры
	   (круг или квадрат) и выводит результат на экран.

	   Параметры:
	   fig (str): Название фигуры. Должно быть 'circle' или 'square'.
	   func (str): Название функции для вычисления. Должно быть 'perimeter' или 'area'.
	   size (list): Список размеров фигуры, необходимые для вычисления функции.
	                Для круга необходим один параметр (радиус),
	                для квадрата - один параметр (длина стороны).

	   Исключения:
	   - Вызывает AssertionError, если fig не находится в списке доступных фигур или
	     если func не находится в списке доступных функций.

	   Пример вызова:
	   >>> calc('circle', 'area', [5])
	   area of circle is 78.53981633974483
	   >>> calc('square', 'perimeter', [4])
	   perimeter of square is 16


# История изменения проекта с хешами комитов (кроме последней записи)
## commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

## commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

## commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

## commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

    L-04: Triangle added

## commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

## commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

