'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 
Примечание: 8 разных ответов.

Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.

'''

n = {}
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            if j in n:
                n[j] += 1
            else:
                n[j] = 1

print(n)