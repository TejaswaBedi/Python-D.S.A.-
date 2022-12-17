max_heap = []

def swap(index1 , index2):
    max_heap[index1],max_heap[index2] = max_heap[index2],max_heap[index1]
    
def heapify(index):
    size = len(max_heap)
    left_child = 2*index+1
    right_child = 2*index+2
    largestElementIndex = index
    
    if(left_child < size and max_heap[left_child] > max_heap[largestElementIndex]):
        largestElementIndex = left_child
    
    if(right_child < size and max_heap[right_child] > max_heap[largestElementIndex]):
        largestElementIndex = right_child
        
    if(largestElementIndex != index):
        swap(index, largestElementIndex)
        heapify(largestElementIndex)
    
def insert(value):
    max_heap.append(value)
    size = len(max_heap)
    child = size - 1
    parent = (child-1)//2
    
    while(parent >=0 and max_heap[child] > max_heap[parent]):
        swap(child, parent)
        child = parent
        parent = (child - 1)//2
        
def delete():
    size = len(max_heap)
    if(size == 0):
        return -1
    
    key = max_heap[0]
    max_heap[0] = max_heap[size - 1]
    max_heap.pop()
    
    heapify(0)
    return key

def printHeap():
    print(max_heap)
    

# Inputs
    
insert(98)
insert(87)
insert(86)
insert(44)
insert(40)
insert(32)
insert(33)
insert(20)
insert(21)
print(delete())
printHeap()
insert(100)
printHeap()
