from heapq import *

def Reorganise(S:str) -> str:
    hash_map = dict()
    
    for character in S:
        hash_map[character] = hash_map.get(character, 0) + 1
      
    max_heap = list()
    
    for key, value in hash_map.items():
        heappush(max_heap, (-value, key))
        
    ReorganisedString =[]
    
    while(len(max_heap) >= 2):
        value1, key1 = heappop(max_heap)
        freq1 = -value1
        value2, key2 = heappop(max_heap)
        freq2 = -value2
        
        ReorganisedString.append(key1)
        ReorganisedString.append(key2)
        
        freq1 -= 1
        freq2 -= 1
        
        if(freq1 > 0):
            heappush(max_heap,(-freq1, key1))
            
        if(freq2 > 0):
            heappush(max_heap, (-freq2, key2))
            
    if(len(max_heap)==0):
        return ''.join(ReorganisedString)
    else:
        value, key = heappop(max_heap)
        freq = -value
        if(freq == 1):
            ReorganisedString.append(key)
            return ''.join(ReorganisedString)
        else:
            return "\'\'"
        
# Inputs

S1 = "aaabcdddaa"
S2 = "asddgssedgf"
S3 = "aaaaaaabbbc"
result1 = Reorganise(S1)
print(result1)
result2 = Reorganise(S2)
print(result2)
result3 = Reorganise(S3)
print(result3)