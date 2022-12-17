def nonRepeatition(string):
    windowStart = 0
    map = dict()
    max_length = 0
    for windowEnd in range(0,len(string)):
        currentChar = string[windowEnd]
        
        if(currentChar in map and windowStart <= windowEnd):
            windowStart = map[currentChar] + 1
        else:
            max_length = max(max_length , (windowEnd - windowStart + 1))
        map[currentChar] = windowEnd
        
    return max_length
    

string = input("Enter the String ")
maxLength = nonRepeatition(string)
print(maxLength)