from heapq import *

def freq_sort(S:str) -> str:
    hash_map = dict()
    
    for character in S:
        hash_map[character] = hash_map.get(character, 0) + 1
        
    max_heap = list()
    
    for key, value in hash_map.items():
        heappush(max_heap, (-value, key))
        
    fq_sorted = []
    
    while(max_heap):
        value, key = heappop(max_heap)
        freq = -value
        
        for i in range(freq):
            fq_sorted.append(key)
            
    return ''.join(fq_sorted)

S = "appalpappalchhappallchaa"
result = freq_sort(S)
print(result)