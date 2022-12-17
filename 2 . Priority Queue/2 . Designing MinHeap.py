min_heap = []

def swap(index1, index2):
    min_heap[index1], min_heap[index2] = min_heap[index2], min_heap[index1]
    
def heapify(index):
    size = len(min_heap)
    left_child = 2*index+1
    right_child = 2*index+2
    smallestElementIndex = index
    
    if(left_child < size and min_heap[left_child] < min_heap[smallestElementIndex]):
        smallestElementIndex = left_child
        
    if(right_child < size and min_heap[right_child] < min_heap[smallestElementIndex]):
        smallestElementIndex = right_child
        
    if(smallestElementIndex != index):
        swap(index, smallestElementIndex)
        heapify(smallestElementIndex)
        
def insert(value):
    min_heap.append(value)
    size = len(min_heap)
    index = size -1
    parent = (index -1)//2
    
    while(parent >= 0 and min_heap[index] < min_heap[parent]):
        swap(index, parent)
        index = parent
        parent = (index - 1)//2
        
def delete():
    size = len(min_heap)
    if (size == 0):
        return -1
    
    key = min_heap[0]
    min_heap[0] = min_heap[size-1]
    min_heap.pop()
    
    heapify(0)
    return key

def printHeap():
    print(min_heap)
    
    
# Inputs

insert(10)
insert(4)
insert(5)
insert(6)
insert(12)
printHeap()
print(delete())
printHeap()
insert(2)
printHeap()
