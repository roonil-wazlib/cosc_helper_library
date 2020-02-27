import random
import time
import matplotlib.pyplot as plt
import numpy as np



def create_input(input_size):
    ls = []
    for i in range(input_size):
        ls.append(0)
    #random.shuffle(ls)
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


def get_time_on_value(func, num):
    start = time.clock()
    func(num)
    end = time.clock()
    return end - start


def get_avg_of_n_times_on_value(func, n, num):
    total_time = 0
    for i in range(n):
        total_time += get_time_on_value(func, num)
    total_time /= n
    return total_time    
        
        