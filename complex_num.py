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

    # Возведение в степень n



    # Модуль
    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2)**(0.5)

    def trigonom_forma(self):
        return '%f(cos%s+isin%s)' % (self.__abs__(), chr(981), chr(981))


a = Compl(1, 2)
b = Compl(3, 4)
print(a.trigonom_forma())