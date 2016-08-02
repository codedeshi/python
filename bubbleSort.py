import random
import time
import timeit

def timer(func):
    def wrapper(*arg,**kwarg):
        t = 0
        for i in range(iterations):
            start =  time.time()
            func(*arg,**kwarg)
            end  = time.time()
            t+= (end-start)
        print t/iterations*1000
    return wrapper

@timer
def bubbleSort(arr):
    length = len(arr)-1
    while length > 0:
        for i in range(length):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        length-=1;
    return arr
    #print arr

arr = [random.random() for i in range(100)]
iterations = 10000

bubbleSort(arr)
