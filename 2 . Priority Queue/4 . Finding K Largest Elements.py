from heapq import *

def LargestKElements(array, k):
    min_heap = []
    
    for i in range(len(array)):
        heappush(min_heap, array[i])
        
        if(len(min_heap) == k+1):
            heappop(min_heap)
            
    KLargest = []
    
    while(min_heap):
        KLargest.append(heappop(min_heap))
        
    return KLargest

array = [4, 7, 9, 2, 8, 6, 5]
k = 3
result = LargestKElements(array, k)
for large in result:
    print(large, end=" ")