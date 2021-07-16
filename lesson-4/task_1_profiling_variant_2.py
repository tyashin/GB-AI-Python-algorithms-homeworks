import random
import cProfile
import timeit


# Profiling with cProfile
prof = cProfile.Profile()
prof.enable()

N = 50000
a = []
b = []

for i in range(N):
    a.append(random.randint(0, 100))
    if a[i] % 2 == 0:
        b.append(i)


prof.disable()
print('cProfile results:')
prof.print_stats()


# Profiling with timeit
testcode = '''
import random
N = 50000
a = []
b = []
for i in range(N):
    a.append(random.randint(0, 100))
    if a[i] % 2 == 0:
        b.append(i)
'''

print('timeit results:')
print(
    f'Execution time: {timeit.timeit(stmt=testcode, number=1000)} seconds')


###############################################################################
'''
Результаты:
Для N = 1000, с условием в 1000 повторов для функции timeit:
cProfile results:
         6800 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
     1506    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1293    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 0.584580160000769 seconds

------------------------------------------

Для N = 10000, с условием в 1000 повторов для функции timeit:
cProfile results:
         67805 function calls in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    0.004    0.000    0.009    0.000 random.py:200(randrange)
    10000    0.002    0.000    0.011    0.000 random.py:244(randint)
    10000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
    15081    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12723    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 5.738836837997951 seconds
------------------------------------------

Для N = 50000, с условием в 1000 повторов для функции timeit:
cProfile results:
         338849 function calls in 0.057 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    50000    0.021    0.000    0.043    0.000 random.py:200(randrange)
    50000    0.009    0.000    0.053    0.000 random.py:244(randint)
    50000    0.016    0.000    0.022    0.000 random.py:250(_randbelow_with_getrandbits)
    75260    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
    50000    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    63588    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 29.472015637002187 seconds
'''
