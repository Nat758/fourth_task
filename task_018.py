# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# import random
# n = int(input())
# k = [random.randint(0, 5) for _ in range(n+1)]
# print(k)
# res = []
# i = 0
# st = len(k) - 1
# for elem in k:
#     if elem != 0 and elem != 1:
#         res.append(str(elem) + '*x^' + str(st))
#     elif elem == 1:
#         res.append('x^' + str(st))
#     st -=1
# res[-1] = res[-1][:-4]
# if res[-2][0].isdigit():
#     res[-2] = res[-2][:-2]
# else:
#     res[-2] = res[-2][:-2]
# s = ' + '.join(res) + ' = 0'
# print(s)
# with open('data.txt', 'w', encoding = 'utf-8') as file:
#     print(s, file = file)


from random import randint

k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
   koefs.append(randint(1, 100))

   ans = list()
for i in range(len(koefs)):
   if k == 1:
    ans.append(f'{koefs[i]}*x')
   elif k == 0:
    ans.append(f'{koefs[i]}')
   else:
    ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
if flag == 1:
  ans.append('+')
elif flag == 0:
  ans.append('-')
  k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()