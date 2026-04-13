class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    ''' Structure: first in -> first out 
    '''
    
    def __init__(self):
        self.front = None
        self.back = None
        self.size:int = 0

    def __len__(self):
        ''' length dunder
        0(1) - constant time -> fetches one value
        '''
        return self.size
    
    def __repr__(self):
        ''' representation dunder
        0(n) - linear time -> has to iterate whole list
        '''
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return '; '.join(items)


    def enqueue(self, value):
        ''' adds item to queue 
        0(1) - constant time -> you have to look at rear and append one element.
        if you have 5 million elements and you are enqueueing another item, all I have to to is to add it to the back and set the pointer to the next node.
        the time it takes to do this task is not effected by any size. 
        '''

        newNode = Node(value)

        if self.back is None:
            # if we dont have anything in the queue already
            # decleare the structure: front and back is the same thing, and they are = newNode
            self.front = self.back = newNode
        else:
            # if we already have something in queue.
            self.back.next = newNode # set the next item after rear/back to the new node 
            self.back = newNode # sets the back itself to the new node

        self.size += 1 # not nessasary but its practical to have a counter

        
    def dequeue(self):
        ''' removes item from queue 
        0(1) - constant time -> same as dequeue, size of the queue does not matter because it will only fetch the first one using its referense pointer, and then update the pointer for next item. 
        '''
        if self.front is None:
            raise IndexError('queue is empty')
        dequeued_value = self.front.value # extracted value -> do something with this
        self.front = self.front.next # tells that the next item in queue is not the new front/front

        if self.front is None: # if front is none as a result of that (if queue only has one item which is now removed:)
            self.back = None # then rear needs to be None

        self.size -= 1

        return dequeued_value

    def peak(self):
        if self.front is None: 
            raise IndexError('queue is empty')
        
        # print(f"    next item in queue: {self.front.value}") #> optional

        return self.front.value

    def isEmpty(self):
        ''' 0(1) - constant time -> same as __len__ it only fetches one value (size)
        '''
        return self.front is None
        # return len(self) == 0 #> alt if you want to use __len__

def main():
    ''' Example on how to use it:
    '''
    q = Queue()
    patients = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        # "Waltz, John",
        # "Heinz, Valter",
        # "Tormodson, Tormod",
        # "Oksnes, Per Mohammed",
        # "Olsen, Mehmed",
    ]
    
    for i in patients:
        q.enqueue(i) 

    print(f"patients for today: {q}")
    print("\n\nDoctors office opens: \n")
    nr = 1
    while not q.isEmpty(): # until queue is empty:
        
        print(f"    consulting patient nr.{nr}: {q.dequeue()}")
        print(f"    remaining patients in queue: {q.size}")
        print(f"    coming up: {q.peak() if not q.isEmpty() else "_empty_"}\n")
        nr += 1

if __name__ == '__main__':
    main()
