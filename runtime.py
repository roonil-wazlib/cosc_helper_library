import random
import time
import matplotlib.pyplot as plt
import numpy as np



def create_input(input_size):
    ls = list(range(input_size))
    random.shuffle(ls)
    return ls


def get_time(func, ls):
    start = time.clock()
    func(ls)
    end = time.clock()
    return end - start
    
    
def time_once(func, input_size):
    ls = create_input(input_size)
    return get_time(func, ls)


def get_avg_of_n_times(func, n, input_size):
    total_time = 0
    for i in range(n):
        ls = create_input(input_size)
        total_time += get_time(func, ls)
    total_time /= n
    return total_time
        
        