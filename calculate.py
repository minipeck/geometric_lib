import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	"""
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
	   """
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



