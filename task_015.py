# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}





from symbol import dictorsetmaker


a = int(input('сколько знаков после запятой должно быть: '))
pi = 0

for n in range(0, 100):
    result = round((1/16**n) * ((4/(8*n+1)) - (2/(8*n+4)) - (1/(8*n+5)) - (1/(8*n+6))), a)
    pi += result

print(pi)


# d=input('Задайте d: ')
# p=float(input('Задайте число для вычисления: '))
# count1=0
# count2=0
# for i in str(d):
#     if i !='.':
#         count1+=1
#     else:
#         break
# for i in str(d):
#     count2+=1
# a = count2-count1-1
# print(a)            




# import math
# d = input('Введите число d указывающее степень округления числа pi ')
# d = d[2:len(d)]
# print(round(math.pi,len(d)))

# a = int(input('введите нужную точность 1#= '))
# pi_target = 0
# for i in range(1, 1000000):
#     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
# print(str(pi_target)[:a + 2])