# Задача №37.Дано натуральное число N 
# и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода). 
# Input: 2 -> 3 4 Output: 4 3


# print('Задача 37')
# print('Провести инверсию натурального числа N:')
# N = str(input('  Введите натуральное число N: '))

# # Метод инверсии строки 
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
    
# print(N)
# print(reverse(N))



def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + f' {k}'


n = int(input())
print(f(n))