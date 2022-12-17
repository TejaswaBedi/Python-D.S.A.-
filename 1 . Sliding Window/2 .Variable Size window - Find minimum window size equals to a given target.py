import math
def minWindowSize(array , target):
    windowStart = 0
    windowSum = 0
    ansStart = 0
    ansEnd = 0
    winSize = math.inf
    for windowEnd in range(0,len(array)):
        windowSum = windowSum + array[windowEnd]
        
        while(windowSum >= target and windowStart <= windowEnd):
            winSize = min(winSize , (windowEnd - windowStart + 1))
            ansStart = windowStart
            ansEnd = windowEnd
            windowSum = windowSum - array[windowStart]
            windowStart = windowStart + 1
    if(winSize == math.inf):
        return 0
         
    return winSize
            

print("Enter the array ")
array = list(map(int,input().split()))
key = int(input("Enter the target value"))
minSize = minWindowSize(array , key)
print(minSize)