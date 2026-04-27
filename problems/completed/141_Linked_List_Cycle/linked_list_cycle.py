from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        figure out if theres a 'cycle' in linked-list or not.
        '''
        i = 0
        ahead = head
        '''
        since one is lagging behind by 2, and during a loop the value of the one ahead is not moving forward the the one behind does there should be a point where they meet.
        although a linked list with a pattern similar to a loop, like: [1,2,3,4,2,3,4] when i=3 val for head and ahead will both be =4 -> giving a false 'True'.
        '''
        while ahead and ahead.next:
            head = head.next
            ahead = ahead.next.next
            if head == ahead:
                return True
        return False





    def hasCycle_visualizer(self, head: Optional[ListNode]) -> bool:
        ''' This is helping me understancd the turtle-hare-algorithm. (forgot real name) by tryuing to vizualising it with pointers;
            i: 'V' -> which increments by '1', and represents the 'head' value.
            y: '^' -> which increments by '2', and represents the 'ahead' value.
          i => V 
            [  3   2   0  -4 ]
          y => ^ 
        '''
        i = 0
        y = 0
        _ = 0 #> just iterator, has nothing to do with the code.
        _head = [3,2,0,-4] #> only for visualization purposes, has nothing to do with the code.
        ahead = head
        end = 4
        _y_changed = False #> only for visualization purposes, has nothing to do with the code.
        while _ < 10: #10 is an arbitrary limit, to make sure it stops while testing smaller testcases. 

            print(f"___[{_}]__________________________________________")
            if _y_changed:
                ''' uncomment to visualize '''
                # print(f"    _head[y]:_head[{y}]:{_head[y]}")
                # print(f"    array[y*] --actually-is--> {[h if h != _head[y] else f'[{h}]' for h in _head]}\n")
                _y_changed = False


            print("\n","    "*i,f"[i:{i}]")
            print(" ","    "*i,f"|")
            print("[  3,  2,  0, -4 ]")
            print(" ","    "*y,f"| ")
            print("","    "*y,f"[y:{y}]\n")


            if i == y and _!=0:
                print("DING DING DING")
                break

            head = head.next
            ahead = ahead.next.next
            
            i+=1
            if i == end:
                i = pos
            y+=2
            if y >= end:
                _y_changed = True
                ''' uncomment to visualize '''
                # print(f"\n    y overflow_adj / (y*):")
                # print(f"    (New) y = y*")
                # print(f"    (New) y = pos  + ( y - (end-1) )")
                # print(f"    (New) y = {pos}    + ( {y} - (  {end}-1) )")
                # print(f"    (New) y = {pos + y-(end)}")
                # print(f"    array[y*] --should-be--> {[h if h!=_head[pos + y-(end)] else f"[{_head[pos + y-(end)]}]" for h in _head ]}\n")
                y = pos + (y-end)           
            _ += 1


   
    def hasCycle_checker(self, head: Optional[ListNode]) -> bool:
        ''' Checker - This displays the timeline of the actual algorithm-values as columns. (for factchecking my visualizer)
        '''
        i = 0
        y = 0
        ahead = head
        end = 4
        while i < 9:
            print(f"i:{i} | head:{head.val} ahead:{ahead.val}")   
            head = head.next
            ahead = ahead.next.next
            i+=1
            if y>=end:
                y=pos
            else:
                y+=2
                
  
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ''' This is helping me understancd the turtle-hare-algorithm. (forgot real name) by tryuing to vizualising it with pointers;
            i: 'V' -> which increments by '1', and represents the 'head' value.
            y: '^' -> which increments by '2', and represents the 'ahead' value.
          i => V 
            [  3   2   0  -4 ]
          y => ^ 
        '''
        i = 0
        y = 0
        _ = 0 #> just iterator, has nothing to do with the code.
        _head = [3,2,0,-4] #> only for visualization purposes, has nothing to do with the code.
        ahead = head
        end = 4
        _y_changed = False #> only for visualization purposes, has nothing to do with the code.
        while _ < 10: #10 is an arbitrary limit, to make sure it stops while testing smaller testcases. 

            print(f"___[{_}]__________________________________________")
            if _y_changed:
                ''' uncomment to visualize '''
                # print(f"    _head[y]:_head[{y}]:{_head[y]}")
                # print(f"    array[y*] --actually-is--> {[h if h != _head[y] else f'[{h}]' for h in _head]}\n")
                _y_changed = False


            print("\n","    "*i,f"[i:{i}]")
            print(" ","    "*i,f"|")
            print("[  3,  2,  0, -4 ]")
            print(" ","    "*y,f"| ")
            print("","    "*y,f"[y:{y}]\n")


            if i == y and _!=0:
                print("DING DING DING")
                break

            head = head.next
            ahead = ahead.next.next
            
            i+=1
            if i == end:
                i = pos
            y+=2
            if y >= end:
                _y_changed = True
                ''' uncomment to visualize '''
                # print(f"\n    y overflow_adj / (y*):")
                # print(f"    (New) y = y*")
                # print(f"    (New) y = pos  + ( y - (end-1) )")
                # print(f"    (New) y = {pos}    + ( {y} - (  {end}-1) )")
                # print(f"    (New) y = {pos + y-(end)}")
                # print(f"    array[y*] --should-be--> {[h if h!=_head[pos + y-(end)] else f"[{_head[pos + y-(end)]}]" for h in _head ]}\n")
                y = pos + (y-end)           
            _ += 1

    def hasCycle_checker(self, head: Optional[ListNode]) -> bool:
        ''' Checker - This displays the timeline of the actual algorithm-values as columns. (for factchecking my visualizer)
        '''
        i = 0
        y = 0
        ahead = head
        end = 4
        while i < 9:
            print(f"i:{i} | head:{head.val} ahead:{ahead.val}")   
            head = head.next
            ahead = ahead.next.next
            i+=1
            if y>=end:
                y=pos
            else:
                y+=2


def build_linked_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

if __name__ == '__main__':

    cases = [
        [3,2,0,-4],
		1,
		[1,2],
		0,
		[1],
		-1
    ]

#> OPTION 0 (for Nodes)
    s = Solution()
    for i in range(0, len(cases), 2):
        vals = cases[i]
        pos = cases[i + 1]
        head = build_linked_list(vals, pos)
        print(f"___ NO.{i//2} ___________________________________")
        print(f"Input: vals={(str(vals[:10])[:-1] + f', ... {vals[-1]}]') if len(vals) > 10 else vals}, pos={pos}")
        ans = s.hasCycle(head)
        print(f"Output: {ans}\n")

    ''' uncomment to visualize 
    THESE ARE THE TESTERS TO HELP UNDERSTAND turtle-hare-algorithm. (forgot real name) by vizualising it. 
    '''
    # s = Solution()
    # for i in range(0, len(cases), 2):
    #     vals = cases[i]
    #     pos = cases[i + 1]
    #     head = build_linked_list(vals, pos)
    #     print(f"___ NO.{i//2} ___________________________________")
    #     print(f"Input: vals={(str(vals[:10])[:-1] + f', ... {vals[-1]}]') if len(vals) > 10 else vals}, pos={pos}")
    #     ans = s.hasCycle_visualizer(head)
    #     print(f"Output: {ans}\n")

    # s = Solution()
    # for i in range(0, len(cases), 2):
    #     vals = cases[i]
    #     pos = cases[i + 1]
    #     head = build_linked_list(vals, pos)
    #     print(f"___ NO.{i//2} ___________________________________")
    #     print(f"Input: vals={(str(vals[:10])[:-1] + f', ... {vals[-1]}]') if len(vals) > 10 else vals}, pos={pos}")
    #     ans = s.hasCycle_checker(head)
    #     print(f"Output: {ans}\n")



"""
(NEW) TESTCASES:
cases = [
    '[3,2,0,-4]',
    '1',
    '[1,2]',
    '0',
    '[1]',
    '-1',
    [1, 2, 3],
]

FOR LEETCODE:
'[3,2,0,-4]'
'1'
'[1,2]'
'0'
'[1]'
'-1'
[1, 2, 3]
"""


"""
__ GITHUB PUSH COMMENT _________________________
Finish 141. Linked List Cycle + move to completed
contains: description, solution.
difficulty: Easy
topics: Hash Table, Linked List, Two Pointers
"""






