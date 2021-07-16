import math
import random
import cProfile
import timeit


# Profiling with cProfile
prof = cProfile.Profile()
prof.enable()
N = 2000


def prime(max_count):

    list_len = int(max_count*math.log(max_count)*1.4)+2
    nums = [i for i in range(2, list_len+2)]

    for num in nums:

        i = 2
        while i <= math.sqrt(num):
            if num % i == 0:
                nums[num-2] = 0
                break

            i += 1

    counter = 0
    for i in nums:
        if i != 0:
            counter += 1
            if counter == max_count:
                return i


prime(N)
prof.disable()
print('cProfile results:')
prof.print_stats()


# Profiling with timeit
testcode = '''
import math
N = 2000


def prime(max_count):

    list_len = int(max_count*math.log(max_count)*1.4)+2
    nums = [i for i in range(2, list_len+2)]

    for num in nums:

        i = 2
        while i <= math.sqrt(num):
            if num % i == 0:
                nums[num-2] = 0
                break

            i += 1

    counter = 0
    for i in nums:
        if i != 0:
            counter += 1
            if counter == max_count:
                return i


prime(N)
'''

print('timeit results:')
print(
    f'Execution time: {timeit.timeit(stmt=testcode, number=1000)} seconds')


###############################################################################
'''
Результаты:
Для N = 1000, с условием в 1000 повторов для функции timeit:
cProfile results:
         113523 function calls in 0.028 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    0.028    0.028 task_2_profiling_variant_2.py:13(prime)
        1    0.000    0.000    0.000    0.000 task_2_profiling_variant_2.py:16(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
   113519    0.007    0.000    0.007    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


timeit results:
Execution time: 13.94967306300532 seconds
------------------------------------------

Для N = 2000, с условием в 1000 повторов для функции timeit:
cProfile results:
         330170 function calls in 0.071 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.052    0.052    0.071    0.071 task_2_profiling_variant_2.py:13(prime)
        1    0.001    0.001    0.001    0.001 task_2_profiling_variant_2.py:16(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
   330166    0.018    0.000    0.018    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


timeit results:
Execution time: 39.51571238999895 seconds

'''
