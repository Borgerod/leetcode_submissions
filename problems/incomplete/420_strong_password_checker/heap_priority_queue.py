# Function to return the index of the
# parent node of a given node
def parent(i):
    return (i - 1) // 2

# Function to return the index of the
# left child of the given node
def leftChild(i):
    return ((2 * i) + 1)

# Function to return the index of the
# right child of the given node
def rightChild(i):
    return ((2 * i) + 2)

'''#!DELETEME
    # just a test to understand 
    i_node = 1
    i_parent = parent(i_node)
    i_left = leftChild(i_node)
    i_right = rightChild(i_node)
    print(f"when the node is: {i_node} then the indexes for [i_parent] -> [i_left, i_parent, i_right] are: [{i_parent}] -> [{i_left},i_node,{i_right}]")
'''


# Function to shift up the node in order
# to maintain the heap property
def shiftUp(i, arr):
    while i > 0 and arr[parent(i)] < arr[i]:
        '''
        så lenge verdien på parent er større en child:
        [... parent_node, ..., child_node, ...]
        [... 9, ..., 20, ...] -> shift up child_node's index
        du er ferdig når: 
        [... child_node, ..., parent_node, ...]
        [... 20, ..., 9, ...] -> legal, finish
        '''
        # Swap parent and current node
        arr[parent(i)], arr[i] = arr[i], arr[parent(i)]

        # Update i to parent of i
        i = parent(i)
'''#! DELETEME
#test Visual TEST

arr = [20,10,2,3,6,1,7,0] # test array
# our designated node:
i = 6
node = arr[i]

# invite familly 
p_i = parent(i)
l_i = leftChild(i)
r_i = rightChild(i)
print(f"array : {arr}")
print(f"array indecies : {[i for i in range(0,len(arr))]}")
print(f"our designated node: i -> arr[i] : {i} -> {node}")
print(f"parent: {p_i}")
print(f"leftChild: {l_i}")
print(f"rightChild: {r_i}")
print()
print()
print()
print(f"Old relation ship:")
# print(f"    indecies: [.., {parent(i)}, ..] -> [.., {leftChild(i)}, ({i}), {rightChild(i)}, ..]     [.., parent(i), ..] -> [.., leftChild(i), (i), rightChild(i), ..]")
# print(f"    values: [.., {arr[parent(i)]}, ..] -> [.., {arr[leftChild(i)]}, ({arr[i]}), {arr[rightChild(i)]}, ..]")
print(f"    indecies: [.., {parent(i)}, ..] -> [.., ({i}),  ..]     [.., parent(i), ..] -> [.., (i), ..]")
print(f"    values: [.., {arr[parent(i)]}, ..] -> [..,  ({arr[i]}),  ..]")
formatted = [
    f"({x})" if idx == parent(i) or idx == i else x
    for idx, x in enumerate(arr)
]
print(f"    array: {formatted}")
print("TEST")
print(f"grandparent: {arr[parent(parent(i))]}")
print("TEST")
print()
print(f"arr[i]: {arr[i]}")
print(f"arr[parent(i)]: {arr[parent(i)]}")
print(f"then finally:")
print(f"while arr[parent(i)] < arr[i] : ({arr[parent(i)] < arr[i]})")
print(f"meaning:")
print(f"")
print(f"as long as {arr[parent(i)]} < {arr[i]}:")
print(f"    shift up the index of node {arr[i]}")
print(f"    because parent cannot be smaller then child")
print(f"    ")
print(f"    then update i to be parent's i")

print(f"    node_i = parent_i")
print(f"    {i} <= {parent(i)}")
# print(f"    New i = {parent(i)}")
i = parent(i)
print(f"    New i = {i}")
print(f"    curious: parent(i) = New parent_indedx =  {parent(i)} ??")
print(f"    array : {arr}")
print(f"    ")
# print(f"Old relation ship:")
# print(f"    {}")

print(f"New relation ship:")
# print(f"    indecies: [.., {parent(i)}, ..] -> [.., {leftChild(i)}, ({i}), {rightChild(i)}, ..]     [.., parent(i), ..] -> [.., leftChild(i), (i), rightChild(i), ..]")
# print(f"    values: [.., {arr[parent(i)]}, ..] -> [.., {arr[leftChild(i)]}, ({arr[i]}), {arr[rightChild(i)]}, ..]")
print(f"    indecies: [.., {parent(i)}, ..] -> [.., ({i}),  ..]     [.., parent(i), ..] -> [.., (i), ..]")
print(f"    values: [.., {arr[parent(i)]}, ..] -> [..,  ({arr[i]}),  ..]")
formatted = [
    f"({x})" if idx == parent(i) or idx == i else x
    for idx, x in enumerate(arr)
]
print(f"    array: {formatted}")
'''


# Function to shift down the node in
# order to maintain the heap property
def shiftDown(i, arr, size):
    maxIndex = i

    # Left Child
    l = leftChild(i)

    if l <= size and arr[l] > arr[maxIndex]:
        # hvis node's leftChilds_index er mindre/lik size      OG  leftChilds_verdi er større enn maxIndexens_verdi: 
            # da skal maxindex oppdateres til leftChilds_index
        maxIndex = l

    # Right Child
    r = rightChild(i)

    if r <= size and arr[r] > arr[maxIndex]:
        # hvis node's rightChild_index er mindre/lik size      OG  rightChild_verdi er større enn maxIndexens_verdi: 
            # da skal maxindex oppdateres til rightChild_index
        maxIndex = r

    # If i not same as maxIndex
    if i != maxIndex:
        # om i IKKE er maxIndex:
        #   så skal i_verdi or maxIndex_verdi bytte plass. 
        #   så skal shiftDown bli callet på nytt igjen (prøver på nytt)
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
        shiftDown(maxIndex, arr, size)

# Function to insert a new element
# in the Binary Heap
def insert(p, arr, size):
    size[0] = size[0] + 1
    arr.append(p)

    # Shift Up to maintain heap property
    shiftUp(size[0], arr)

# Function to extract the element with
# maximum priority
def extractMax(arr, size):
    result = arr[0]

    # Replace the value at the root
    # with the last leaf
    arr[0] = arr[size[0]]
    size[0] = size[0] - 1

    # Shift down the replaced element
    # to maintain the heap property
    shiftDown(0, arr, size[0])
    return result

# Function to change the priority
# of an element
def changePriority(i, p, arr, size):
    oldp = arr[i]
    arr[i] = p

    if p > oldp:
        shiftUp(i, arr)
    else:
        shiftDown(i, arr, size[0])

# Function to get value of the current
# maximum element
def getMax(arr):
    return arr[0]

# Function to remove the element
# located at given index
def remove(i, arr, size):
    arr[i] = getMax(arr) + 1

    # Shift the node to the root
    # of the heap
    shiftUp(i, arr)

    # Extract the node
    extractMax(arr, size)

if __name__ == "__main__":
    # NOTE
    # heap: means the whole array 
    # size: means the measured size of the whole array 
    # size[0] is the index of the last valid element in arr.
    # 
    # size = [-1] → heap is empty (no elements)
    # size = [0] → heap has 1 element (arr[0])
    # size = [1] → heap has 2 elements (arr[0], arr[1])
    # size = [2] → heap has 3 elements (arr[0], arr[1], arr[2])

    
    #       45
    #     /      \
    #    31      14
    #   /  \    /  \
    #  13  20  7   11
    # /  \
    #12   7
    #Create a priority queue shown in
    #example in a binary max heap form.
    #Queue will be represented in the
    #form of array as:
    #45 31 14 13 20 7 11 12 7
    # Insert the element to the
    # priority queue

    arr = []
    size = [-1]
    insert(45, arr, size)
    insert(20, arr, size)
    insert(14, arr, size)
    insert(12, arr, size)
    insert(31, arr, size)
    insert(7, arr, size)
    insert(11, arr, size)
    insert(13, arr, size)
    insert(7, arr, size)

    i = 0

    # Priority queue before extracting max
    print("Priority Queue : ", end="")
    while i <= size[0]:
        print(arr[i], end=" ")
        i += 1

    print()

    # Node with maximum priority
    print("Node with maximum priority : " + str(extractMax(arr, size)))

    # Priority queue after extracting max
    print("Priority queue after extracting maximum : ", end="")
    j = 0
    while j <= size[0]:
        print(arr[j], end=" ")
        j += 1

    print()

    # Change the priority of element
    # present at index 2 to 49
    changePriority(2, 49, arr, size)
    print("Priority queue after priority change : ", end="")
    k = 0
    while k <= size[0]:
        print(arr[k], end=" ")
        k += 1

    print()

    # Remove element at index 3
    remove(3, arr, size)
    print("Priority queue after removing the element : ", end="")
    l = 0
    while l <= size[0]:
        print(arr[l], end=" ")
        l += 1
