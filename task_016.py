

# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


n = int(input('задай число: '))
def Factor_number(n):
    result = list()
    d = 2
    while d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result
print(Factor_number(n))

# n = int(input("Введите число N: "))
# i = 2
# list = []

# while i <= n:
#    if n % i == 0:
#     list.append(i)
#     n //= i
#     i = 2
#    else:
#     i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")

