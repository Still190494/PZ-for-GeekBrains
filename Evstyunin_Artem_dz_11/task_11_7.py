# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.





class MyComplex:
    def __init__(self,num_1, num_2):
        self.complex_num = complex(num_1,num_2)

    def __add__(self, other):
        return f'Сложение - {str(self.complex_num + other.complex_num)}'

    def __mul__(self, other):
        return f'Умножение - {str(self.complex_num * other.complex_num)}'


num = MyComplex(1,2)
num1 = MyComplex(3,4)
print(num + num1)
print(num * num1)



