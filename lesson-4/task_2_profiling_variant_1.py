import math
import random
import cProfile
import timeit


# Profiling with cProfile
prof = cProfile.Profile()
prof.enable()
N = 10000


def sieve(max_count):

    list_len = int(max_count*math.log(max_count)*1.4)+2
    nums = [i for i in range(2, list_len+2)]

    for num in nums:
        if num != 0:
            for candidate in range(pow(num, 2), list_len, num):
                nums[candidate-2] = 0

    counter = 0
    for i in nums:
        if i != 0:
            counter += 1
            if counter == max_count:
                return i


sieve(N)
prof.disable()
print('cProfile results:')
prof.print_stats()


# Profiling with timeit
testcode = '''
import math
N = 10000

def sieve(max_count):

    list_len = int(max_count*math.log(max_count)*1.4)+2
    nums = [i for i in range(2, list_len+2)]

    for num in nums:
        if num != 0:
            for candidate in range(pow(num, 2), list_len, num):
                nums[candidate-2] = 0

    counter = 0
    for i in nums:
        if i != 0:
            counter += 1
            if counter == max_count:
                return i

sieve(N)
'''

print('timeit results:')
print(
    f'Execution time: {timeit.timeit(stmt=testcode, number=1000)} seconds')


###############################################################################
'''
Результаты:
Для N = 1000, с условием в 1000 повторов для функции timeit:
cProfile results:
         1199 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    0.003    0.003 task_2_profiling_variant_1.py:13(sieve)
        1    0.001    0.001    0.001    0.001 task_2_profiling_variant_1.py:16(<listcomp>)
     1195    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


timeit results:
Execution time: 1.7584219860000303 seconds
------------------------------------------

Для N = 10000, с условием в 1000 повторов для функции timeit:
cProfile results:
         12074 function calls in 0.032 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.024    0.024    0.032    0.032 task_2_profiling_variant_1.py:13(sieve)
        1    0.006    0.006    0.006    0.006 task_2_profiling_variant_1.py:16(<listcomp>)
    12070    0.002    0.000    0.002    0.000 {built-in method builtins.pow}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


timeit results:
Execution time: 25.220082319006906 seconds

'''
