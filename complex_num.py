'''
Сложение + __add__
Вычитание + __sub__
Умножение + __mul__
Деление + __truediv__
Сопряжение + conjugate
Возведение в степень
Извлечение корня
Алгебраическая форма
Тригонометрическая форма
Экспоненциальная форма
'''

# Функция для вычисление факториала. Для дальнейшего использования при возведении в степень
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

class Compl(object):


    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
       # return '{0.real}{0.imag}j'.format(self.real, self.imag)
        return '(%g, %gj)' % (self.real, self.imag)

    # Сложение
    def __add__(self, second):
        return Compl(self.real + second.real,
                     self.imag + second.imag)

    # Вычитание
    def __sub__(self, second):
        return Compl(self.real - second.real,
                     self.imag - second.imag)

    # Умножение
    def __mul__(self, second):
        return Compl(self.real * second.real - self.imag * second.imag,
                     self.imag * second.real + self.real * second.imag)

    # Деление. Формула - http://www.mathwarehouse.com/algebra/complex-number/divide/how-to-divide-complex-numbers.php
    def __truediv__(self, second):
        r = float(second.real ** 2 + second.imag ** 2)
        return Compl((self.real * second.real + self.imag * second.imag) / r,
                     (self.imag * second.real - self.real * second.imag) / r)

    # Сопряжение
    def conjugate(self):
        return Compl(self.real, - self.imag)

    # Возведение в степень n, извлечение корня. Реализовать бином Ньютона https://function-x.ru/complex_numbers3.html



    # Модуль
    def mod(self):
        return (self.real ** 2 + self.imag ** 2)**(0.5)

    # Тригонометрическая форма
    def trigonom_forma(self):
<<<<<<< HEAD
        return '%f(cos(f)+isin(f))' % (self.__abs__())
     #   return '%f(cos%s+isin%s)' % (self.__abs__(), chr(981), chr(981))

=======
        return '%.2f*(cos(f)+i*sin(f))' % (self.mod())
    #    return '%f(cos%s+isin%s)' % (self.__abs__(), chr(981), chr(981))
>>>>>>> 8960990568975b1e21f3dd529f8853e0809d7908

    # Показательная форма
    def exp_forma(self):
        return '%.2f*e^if' % (self.mod())
