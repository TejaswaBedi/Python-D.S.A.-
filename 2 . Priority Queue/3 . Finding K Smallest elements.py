from heapq import *

def KSmallestElements(array, k):
    max_heap = []
    
    for i in range(len(array)):
        heappush(max_heap, -array[i])
        
        if(len(max_heap) == k+1):
            heappop(max_heap)
            
    KSmallest = []
        
    while(max_heap):
        KSmallest.append(-heappop(max_heap))
            
    return KSmallest

arr = [4, 8, 9, 2, 7, 6, 5]
k = 3
result = KSmallestElements(arr, k)
for small in result:
    print(small , end=" ")
