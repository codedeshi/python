import random
import datetime
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
iterations = 100000
start =  datetime.datetime.now()
for i in range(iterations):
    bubbleSort(arr)
end = datetime.datetime.now()
print ((end.minute - start.minute) * 60 + (end.second - start.second) + float(end.microsecond - start.microsecond)/1000000)/iterations , "seconds"
