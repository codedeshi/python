import random
import datetime
def bubbleSort(arr):
    length = len(arr)-1
    while length > 0:
        for i in range(length):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        length-=1;
    print arr
arr = [random.random() for i in range(100)]


start =  datetime.datetime.now()
bubbleSort(arr)
end = datetime.datetime.now()
print end.microsecond - start.microsecond
