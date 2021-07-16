import random
import cProfile
import timeit


# Profiling with cProfile
prof = cProfile.Profile()
prof.enable()
N = 50000
a = [random.randint(0, 100) for i in range(N)]
b = []

for i, j in enumerate(a):
    if j % 2 == 0:
        b.append(i)

prof.disable()
print('cProfile results:')
prof.print_stats()


# Profiling with timeit
testcode = '''
import random
N = 50000
a = [random.randint(0, 100) for i in range(N)]
b = []

for i, j in enumerate(a):
    if j % 2 == 0:
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
         5760 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.000    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.001    0.001 task_1_profiling_variant_1.py:10(<listcomp>)
      478    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1280    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 0.5737666389977676 seconds
------------------------------------------

Для N = 10000, с условием в 1000 повторов для функции timeit:
cProfile results:
         57663 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    0.004    0.000    0.009    0.000 random.py:200(randrange)
    10000    0.002    0.000    0.011    0.000 random.py:244(randint)
    10000    0.003    0.000    0.005    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.002    0.002    0.013    0.013 task_1_profiling_variant_1.py:10(<listcomp>)
     5044    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12617    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 5.605942752001283 seconds
------------------------------------------

Для N = 50000, с условием в 1000 повторов для функции timeit:
cProfile results:
         288928 function calls in 0.058 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    50000    0.018    0.000    0.038    0.000 random.py:200(randrange)
    50000    0.010    0.000    0.048    0.000 random.py:244(randint)
    50000    0.014    0.000    0.020    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.009    0.009    0.057    0.057 task_1_profiling_variant_1.py:10(<listcomp>)
    25464    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    50000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    63462    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 28.350708837002458 seconds
'''
