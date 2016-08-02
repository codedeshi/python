import random
import datetime

def selectionSort(arr):
    start = 0
    while start < len(arr):
        minVal = arr[start]
        minIndex = 0
        for n,i in enumerate(arr[start:len(arr)]):
            if i < minVal:
                minVal = i
                minIndex = n
        arr[start],arr[minIndex+start] = arr[minIndex+start],arr[start]
        start+=1
    return arr
    #print arr

arr = [random.random() for i in range(100)]
iterations = 100000
start =  datetime.datetime.now()
for i in range(iterations):
    selectionSort(arr)
end = datetime.datetime.now()
print ((end.minute - start.minute) * 60 + (end.second - start.second) + float(end.microsecond - start.microsecond)/1000000)/iterations , "seconds"
