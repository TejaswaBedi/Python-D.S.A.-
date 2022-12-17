import math
def calcMaximumSum(array , windowSize):
    windowStart = 0
    windowEnd = 0
    windowSum = 0
    ansStart = 0
    ansEnd = 0
    maxsum = -math.inf
    
    for windowEnd in range(0,len(array)):
        windowSum = windowSum + array[windowEnd]
        
        if((windowEnd - windowStart + 1) >= windowSize):
            maxsum = max(maxsum,windowSum)
            ansStart = windowStart
            ansEnd = windowEnd
            
            windowSum = windowSum - array[windowStart]
            windowStart = windowStart + 1
    print("The array elements contributing to the maximum sum are :-")
    print(array[ansStart:(ansEnd+1)])
    return maxsum
print("Enter the array ")
array = list(map(int,input().split()))
windowSize = int(input("Enter the window size "))
maxSum = calcMaximumSum(array , windowSize)
print(maxSum)
