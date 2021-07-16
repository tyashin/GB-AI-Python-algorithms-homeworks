import random
import cProfile
import timeit


# Profiling with cProfile
prof = cProfile.Profile()
prof.enable()

N = 50000
b = [i for i, j in enumerate([random.randint(0, 100)
                              for i in range(N)]) if j % 2 == 0]
prof.disable()
print('cProfile results:')
prof.print_stats()


# Profiling with timeit
testcode = '''
import random
N = 50000
b = [i for i, j in enumerate([random.randint(0, 100)
                              for i in range(N)]) if j % 2 == 0]
'''

print('timeit results:')
print(
    f'Execution time: {timeit.timeit(stmt=testcode, number=1000)} seconds')


###############################################################################
'''
Результаты:
Для N = 1000, с условием в 1000 повторов для функции timeit:
cProfile results:
         5254 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
     1000    0.000    0.000    0.001    0.000 random.py:244(randint)
     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.002    0.002 task_1_profiling_variant_3.py:11(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_1_profiling_variant_3.py:12(<listcomp>)
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1251    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 0.5757770339987474 seconds

------------------------------------------

Для N = 10000, с условием в 1000 повторов для функции timeit:
cProfile results:
         52700 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    0.004    0.000    0.008    0.000 random.py:200(randrange)
    10000    0.002    0.000    0.010    0.000 random.py:244(randint)
    10000    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.002    0.002    0.012    0.012 task_1_profiling_variant_3.py:11(<listcomp>)
    10000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    12698    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 5.531334519997472 seconds
------------------------------------------

Для N = 50000, с условием в 1000 повторов для функции timeit:
cProfile results:
         263086 function calls in 0.062 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    50000    0.020    0.000    0.042    0.000 random.py:200(randrange)
    50000    0.011    0.000    0.053    0.000 random.py:244(randint)
    50000    0.016    0.000    0.022    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.009    0.009    0.062    0.062 task_1_profiling_variant_3.py:11(<listcomp>)
    50000    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    63084    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}


timeit results:
Execution time: 27.618535002999124 seconds
'''
