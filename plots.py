from . import runtime
import matplotlib.pyplot as plt


def plot_comparison(func1, func2, x_limit, repetitions=1):
    first_times = []
    second_times = []
    sizes = []
    for i in range(1, x_limit):
        ls = runtime.create_input(i)
        ftime = 0
        stime = 0
        for j in range(repetitions):
            ftime += runtime.get_time(func1, ls)
            stime += runtime.get_time(func2, ls)
        first_times.append(ftime/repetitions)
        second_times.append(stime/repetitions)
        sizes.append(i)
    plt.plot(sizes, first_times, "g*", second_times, "bo")
    plt.show()    


def plot(func, x_limit, repetitions=1):
    times = []
    sizes = []
    for i in range(1, x_limit):
        ls = runtime.create_input(i)
        total_time = 0
        for _ in range(repetitions):
            total_time += runtime.get_time(func, ls)
        times.append(total_time/repetitions)
        sizes.append(i)
    plt.plot(sizes, times)
    plt.show()
    
    
def plot_func_single_value_input(func, x_limit, repetitions=1):
    times = []
    sizes = []
    for i in range(1, int(x_limit/4)):
        total_time = 0
        for _ in range(repetitions):
            total_time += runtime.get_time_on_value(func, i*4)
        times.append(total_time/repetitions)
        sizes.append(i)
    plt.plot(sizes, times)
    plt.show()