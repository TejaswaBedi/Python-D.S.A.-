from heapq import *

def ClosestKPoints(points, k):
    max_heap = []
    
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]
        distance = x*x + y*y
        
        heappush(max_heap, (-distance,x,y))
        
        if(len(max_heap) == k+1):
            heappop(max_heap)
            
    KClosest = []
    
    while(max_heap):
        dist, x, y = heappop(max_heap)
        KClosest.append([x,y])
        
    return KClosest

points_arrray = [[-4, 3], [-1, 1], [5, 5], [3, 1], [-4, -3], [2, -2]]
k = 3
result = ClosestKPoints(points_arrray, k)
for KClosePoints in result:
    print(KClosePoints[0], end=" ")
    print(KClosePoints[1])