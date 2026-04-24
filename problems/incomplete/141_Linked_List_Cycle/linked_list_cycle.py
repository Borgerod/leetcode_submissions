from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        '''
        
        '''



        return None



    

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

    s = Solution()
    for i in range(0, len(cases), 2):
        vals = cases[i]
        pos = cases[i + 1]
        head = build_linked_list(vals, pos)
        print(f"___ NO.{i//2} ___________________________________")
        print(f"Input: vals={vals}, pos={pos}")
        ans = s.hasCycle(head)
        print(f"Output: {ans}\n")

