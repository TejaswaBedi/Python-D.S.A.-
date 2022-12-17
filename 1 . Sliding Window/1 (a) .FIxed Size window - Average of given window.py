def calcAverage(array , windowSize):
    windowStart = 0
    windowSum = 0
    avg = []
    
    for windowEnd in range(0,len(array)):
        windowSum = windowSum + array[windowEnd]
        
        if((windowEnd - windowStart + 1) >= windowSize):
            avg.append((windowSum / windowSize))
            windowSum = windowSum - array[windowStart]
            windowStart = windowStart + 1
            
    return avg

print("Enter the array ")
array = list(map(int,input().split()))
windowSize = int(input("Enter the window size "))
average = calcAverage(array , windowSize)
print(average)