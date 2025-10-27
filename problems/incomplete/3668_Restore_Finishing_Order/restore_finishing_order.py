class Solution:
    '''
    order:    ID numbers in correct order
    friends:  ID number in accending order
    '''

    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            #> contender
            1.0) Simplest and quickest way, list copy, simple search. (from order)
        '''    
        friends_sorted = []  
        for i in order:
            print(i)
            if i in friends:
                friends_sorted.append(i)

        return friends_sorted

    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            #* winner A [shared]
            1.1) Compressed
        '''    
        return [i for i in order if i in friends]

    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            #! unfinished
            2.0) from (friends) assuming friends is smaller than order it makes sense to work from them
        '''
        n = len(order)
        # n = len(friends)
        print(f"friends: {friends} ")
        print(f"order:   {order} ")
        friends_sorted = []  
        for f in friends:
            i = 0
            print(f"for f : {f}")
            while i < n:
                print(f"    f:{f} == order[{i}]:{order[i]}")
                if f == order[i]:
                    print(f"     Fround one -> {order[i]}")
                    if i > len(friends):
                        friends[-1] = order[i]
                    else:
                        friends[i] = order[i]
                    # order[i] = 
                    # friends_sorted.append(order[i])
                i+=1
        print(friends)
        return friends_sorted

    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            3.0) inplace going from order, stops when friends is depleted
        '''
        n = len(order)
        # n = len(friends)
        print(f"friends: {friends} ")
        print(f"order:   {order} ")
        friends_sorted = []
        i = 0
        # _f = len(friends)
        f = len(friends)
        # for i in order:
        while i < n:
            print(f"\n  i:{i}")
            if i>1:
                print(f"{len(friends)}//i:{i} ==> {len(friends)//(i)}")
            else:
                print(f"                i:{i} ==> {(i)}")

            # if len(friends)==n:
            # if _f == len(friends):
            if not f:
                print("found all, delete rest of order")
                if n>len(friends):
                    return order[:i]
                return order

            if not order[i] in friends:
                print(f"     order[i]: [{order[i]}] -> NOT in friends:")
                print(f"                 ->   order.pop({i})")
                order.pop(i)
                print(f"     order:   {order}")
                print(f"     friends: {friends}")

            else:
                print(f"     order[i]: [{order[i]}] -> IS in friends:")
                print(f"                 ->  keep [{order[i]}]")
                print(f"     order:   {order}")
                print(f"     friends: {friends}")
                i+=1
                f-=1

    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            3.1) Cleaned
        '''
        f = len(friends) #countdown
        n = len(order)
        i = 0
        while i < n:
            if not f:
                if n>len(friends):
                    return order[:i]
                return order

            if not order[i] in friends:
                order.pop(i)
            else:
                i+=1
                f-=1
    
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            #> contender
            3.2) Compressed - one way
        '''
        f = len(friends) #countdown
        i = 0            #countup
        while f:            
            if order[i] in friends: i+=1; f-=1
            else: order.pop(i)
        return order[:i]
    
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        '''
            #* winner B [shared]
            3.3) Compressed - other way
        '''
        i = f = 0
        while f < len(friends):
            if order[i] in friends: i += 1; f += 1
            else: order.pop(i)
        return order[:i]
    
if __name__ == '__main__':

    cases = [
        [3,1,2,5,4],
		[1,3,4],
		[1,4,5,3,2],
		[2,5],
        [47, 12, 3, 28, 8, 34, 1, 41, 13, 22, 7, 18, 24, 2, 31, 6, 10, 36, 5, 27, 4, 11, 9, 16, 14, 23, 15, 19, 21, 17, 20, 25, 26, 29, 30, 32, 33, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50],
        [3, 8, 13, 18, 24, 31, 41, 47],
        [100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88, 14, 87, 15, 86, 16, 85, 17, 84, 18, 83, 19, 82, 20, 81, 21, 80, 22, 79, 23, 78, 24, 77, 25, 76, 26, 75, 27, 74, 28, 73, 29, 72, 30, 71, 31, 70, 32, 69, 33, 68, 34, 67, 35, 66, 36, 65, 37, 64, 38, 63, 39, 62, 40, 61, 41, 60, 42, 59, 43, 58, 44, 57, 45, 56, 46, 55, 47, 54, 48, 53, 49, 52, 50, 51, 1],
        [1, 10, 20, 30, 40, 50, 60, 70],
                
    ]

    #> OPTION 2 (for multiple inputs)
    s = Solution()
    for i in range(0, len(cases), 2):

        order = cases[i+0]
        friends = cases[i+1]
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {s.recoverOrder(order, friends)}\n")


'''

LEETCODE:
    [3,1,2,5,4]
    [1,3,4]
    [1,4,5,3,2]
    [2,5]
    [47, 12, 3, 28, 8, 34, 1, 41, 13, 22, 7, 18, 24, 2, 31, 6, 10, 36, 5, 27, 4, 11, 9, 16, 14, 23, 15, 19, 21, 17, 20, 25, 26, 29, 30, 32, 33, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50]
    [3, 8, 13, 18, 24, 31, 41, 47]
    [100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91, 11, 90, 12, 89, 13, 88, 14, 87, 15, 86, 16, 85, 17, 84, 18, 83, 19, 82, 20, 81, 21, 80, 22, 79, 23, 78, 24, 77, 25, 76, 26, 75, 27, 74, 28, 73, 29, 72, 30, 71, 31, 70, 32, 69, 33, 68, 34, 67, 35, 66, 36, 65, 37, 64, 38, 63, 39, 62, 40, 61, 41, 60, 42, 59, 43, 58, 44, 57, 45, 56, 46, 55, 47, 54, 48, 53, 49, 52, 50, 51, 1]
    [1, 10, 20, 30, 40, 50, 60, 70]

EXPECTS:
    [3,1,4]
    [5,2]
    [47,3,8,41,13,18,24,31]
    [10,20,30,70,40,60,50,1]

'''