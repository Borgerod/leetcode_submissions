

class Solution:
    '''
        Given an array of intervals intervals where intervals[i] = [starti, endi], 
        return the minimum number of intervals you need to 
        remove to make the rest of the intervals non-overlapping.
        
        Note that intervals which only touch at a point are non-overlapping. 
        For example, [1, 4] and [2, 3] are non-overlapping.
    '''
    ''' 
        v 0.2.0
        - swap out greedy sort with lambda (timsort) for sorting inital dataset. 
        - simplify greedy sort to one iteration. -> keep or skip
    '''

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            
            if start<end:
                # skip, increment removal
                removed+=1
                i+=1
                
            if start>=end:
                # keep, update end
                end = intervals[i][1]
        return removed


# class Solution:
#     '''
#         Given an array of intervals intervals where intervals[i] = [starti, endi], 
#         return the minimum number of intervals you need to 
#         remove to make the rest of the intervals non-overlapping.
        
#         Note that intervals which only touch at a point are non-overlapping. 
#         For example, [1, 4] and [2, 3] are non-overlapping.
#     '''
#     ''' 
#         v 0.1.3 
#         - time limit exceeded, this is good. it is potentially solved now, all i need to do now is to optimize it. 
#         - got error in cases where big intervals where overlapping many small ones, skipping the correct answer. 
#         - refactor sorting criteria  to only care about the endbit- "intervals[j][1] < intervals[min_idx][1]" 
#         - not optimized - sortAccending and eraseOverlapIntervals should be merged into one function. 
#     '''



#     def sortAccending(self, intervals:list[int]) -> list[int]:
#         i = 0 
#         n = len(intervals)

#         while i < n:
#             min_idx = i #index for the smallest item
#             for j in range(i+1, n): #re-iterate list after current position (from current -> to n)
                
#                 if intervals[j][1] < intervals[min_idx][1]:
#                      min_idx = j #then we set j as the new smallest items

#             intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]
#             i+=1
#         return intervals




#     # def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#     #     intervals = self.sortAccending(intervals)
#     #     i = 0 
#     #     n = len(intervals)
#     #     current_stack = []
#     #     biggest_stack = [] 

#     #     while i < n: #[1, 2]
#     #         # build a stack starting with the smallest one. 
#     #         current_stack.append(intervals[i])
#     #         for j in range(i+1, n):
                
#     #             end_of_stack = current_stack[-1][1]
#     #             start_of_j = intervals[j][0]
#     #             if end_of_stack <= start_of_j:
#     #                 current_stack.append(intervals[j])
            
#     #         if len(current_stack)>len(biggest_stack):
#     #             biggest_stack = current_stack
#     #             current_stack = [] #reset current

#     #         current_stack=[]
#     #         i+=1
#     #     return n-len(biggest_stack)        
#        # def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#     #     intervals = self.sortAccending(intervals)
#     #     current_stack = []
#     #     biggest_stack = [] 

#     #     i = 0 
#     #     n = len(intervals)
#     #     while i < n:
#     #         # build a stack starting with the smallest one. 
#     #         current_stack.append(intervals[i]) #sets i as satrt of stack 
#     #         [current_stack.append(intervals[j]) for j in range(i+1, n) if current_stack[-1][1] <= intervals[j][0]]  #sub-iteration - append to current stack if next item fits behind last item in current stack. 
#     #         biggest_stack = current_stack if len(current_stack) > len(biggest_stack) else biggest_stack  #set new biggest stack if current is bigger
#     #         current_stack=[] #reset current stack
#     #         i+=1 #try from the next smallest item
#     #     return n-len(biggest_stack)

#     # def quickSort(self, intervals: list[list[int]]) -> list[list[int]]:
#     #     if len(intervals) <= 1:
#     #         return intervals
#     #     pivot = intervals[len(intervals) // 2]
#     #     left = [x for x in intervals if x[1] < pivot[1]]
#     #     middle = [x for x in intervals if x[1] == pivot[1]]
#     #     right = [x for x in intervals if x[1] > pivot[1]]
#     #     return self.quickSort(left) + middle + self.quickSort(right)
   
#     #     left = [x for x in intervals if x[1] < pivot[1]]
#     def timsort(self, intervals: list[list[int]]) -> list[list[int]]:
#         def insertion_sort(arr, left, right):
#             for i in range(left + 1, right + 1):
#                 key = arr[i]
#                 j = i - 1
#                 while j >= left and arr[j][1] > key[1]:
#                     arr[j + 1] = arr[j]
#                     j -= 1
#                 arr[j + 1] = key

#         def merge(arr, l, m, r):
#             len1, len2 = m - l + 1, r - m
#             left = arr[l:m+1]
#             right = arr[m+1:r+1]
#             i = j = 0
#             k = l
#             while i < len1 and j < len2:
#                 if left[i][1] <= right[j][1]:
#                     arr[k] = left[i]
#                     i += 1
#                 else:
#                     arr[k] = right[j]
#                     j += 1
#                 k += 1
#             while i < len1:
#                 arr[k] = left[i]
#                 i += 1
#                 k += 1
#             while j < len2:
#                 arr[k] = right[j]
#                 j += 1
#                 k += 1

#         n = len(intervals)
#         RUN = 32
#         for i in range(0, n, RUN):
#             insertion_sort(intervals, i, min((i + RUN - 1), n - 1))
#         size = RUN
#         while size < n:
#             for left in range(0, n, 2 * size):
#                 mid = min(n - 1, left + size - 1)
#                 right = min((left + 2 * size - 1), n - 1)
#                 if mid < right:
#                     merge(intervals, left, mid, right)
#             size *= 2
#         return intervals
    
#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#         intervals=[[40,70],[56,80],[63,87],[-51,39],[-74,59],[38,41],[-49,17],[6,57],[36,85],[-73,26],[-6,70],[15,70],[66,78],[37,87],[79,96],[46,97],[36,49],[-58,40],[-58,52],[26,83],[-27,43],[15,86],[11,56],[23,34],[-9,73],[-95,-75],[2,30],[-91,26],[88,89],[-83,-43]]
#         print(self.timsort(intervals))
#         intervals.sort(key=lambda x: x[1])
#         print(intervals)
#         removed = 0
#         end = intervals[0][1]
#         for i in range(1, len(intervals)):
#             start = intervals[i][0]
            
#             if start<end:
#                 # skip, increment removal
#                 removed+=1
#                 i+=1
                
                
                
#             if start>=end:
#                 # keep, update end
#                 end = intervals[i][1]
#         return removed


# class Solution:
#     def sortAccending(self, intervals:list[int]) -> list[int]:
#         len_ = len(intervals)
#         i = 0 
#         n = len(intervals)
#         while i < n:
#             # print("i: ",i)
#             a = intervals[i][0]
#             b = intervals[i][1]
#             y = 1
#             min_idx = i #index for the smallest item
#             for j in range(i+1, n): #re-iterate list after current position (from current - to n)
#                 # if intervals[j] < intervals[min_idx]: #>refactor #if the checker value (j) is smaller than current smallest value (min_idx)
#                 if intervals[j][1] < intervals[min_idx][1]: #*NEW   

#                     # print(f"    current min_idx : {min_idx}")
#                     min_idx = j #then we set j as the new smallest items
#                     # print(f"    new min found: {intervals[j]} at {j} value: {intervals[min_idx]}\n")
#                 # then swap places
#             # print(f"after sub-loop min_idx : {min_idx} value: {intervals[min_idx]}")
#             # print(f"current intervals: {intervals}\n")

#             intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]
#             i+=1
#         # print(intervals)
#         return intervals

#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
#         '''
#         Given an array of intervals intervals where intervals[i] = [starti, endi], 
#         return the minimum number of intervals you need to 
#         remove to make the rest of the intervals non-overlapping.
        
#         Note that intervals which only touch at a point are non-overlapping. 
#         For example, [1, 4] and [2, 3] are non-overlapping.
#         '''

#         print("intervals: ",intervals, len(intervals))
#         intervals = self.sortAccending(intervals)
#         print("intervals(sorted): ", intervals)

#         # [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]
     
#         print("\nSTAGE 2\n")
#         _len = len(intervals)
#         i = 0 
#         n = len(intervals)

#         # smallest_idx = 0
#         # smallest_val = []
#         current_stack = []
#         biggest_stack = [] 

#         while i < n: #[1, 2]
#             print(f"\ni: {i} | biggest stack: {biggest_stack} | current_stack: {current_stack}")
#             # build a stack starting with the smallest one. 
#             current_stack.append(intervals[i])
#             for j in range(i+1, n):
#                 end_of_stack = current_stack[-1][1]
#                 print(f"    last stack element: {current_stack[-1]} end_of_stack: {end_of_stack}")
#                 start_of_j = intervals[j][0]
#                 if end_of_stack <= start_of_j:
#                     print(f"        true: {current_stack[-1]}<={intervals[j]} --> stacking {intervals[j]}")
#                     current_stack.append(intervals[j])
            
            
#             print(f"    current_stack: {current_stack}")
#             if len(current_stack)>len(biggest_stack):
#                 print("     new biggest stack found, replacing old one: ")
#                 biggest_stack = current_stack
#                 current_stack = [] #reset current
#                 print(f"        NEW biggest stack: {biggest_stack}")
#                 print(f"        NEW current_stack: {current_stack}")
#             else:
#                 print(f"        biggest stack: {biggest_stack}")
#             current_stack=[]
#             print(f"-> biggest stack: {biggest_stack}")
#             print(f"-> current stack: {current_stack}")
#             i+=1
#         return _len-len(biggest_stack)





# class Solution:
#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
#         '''
#         Given an array of intervals intervals where intervals[i] = [starti, endi], 
#         return the minimum number of intervals you need to 
#         remove to make the rest of the intervals non-overlapping.
        
#         Note that intervals which only touch at a point are non-overlapping. 
#         For example, [1, 4] and [2, 3] are non-overlapping.
#         '''

#         print("intervals: ",intervals, len(intervals))
#         # # print("set(): ",set(intervals), len(set(intervals)))
#         # # print("="*20)
#         # # print(f"diff: {len(set(intervals))-len(intervals)}")

        
#         # len_ = len(intervals)
#         # i = 0 
#         # n = len(intervals)
#         # while i < n:
#         #     print("i: ",i)
#         #     a = intervals[i][0]
#         #     b = intervals[i][1]
#         #     y = 1
#         #     min_idx = i #index for the smallest item
#         #     for j in range(i+1, n): #re-iterate list after current position (from current - to n)
#         #         if intervals[j] < intervals[min_idx]: #if the checker value (j) is smaller than current smallest value (min_idx)
#         #             print(f"    current min_idx : {min_idx}")
#         #             min_idx = j #then we set j as the new smallest items
#         #             print(f"    new min found: {intervals[j]} at {j} value: {intervals[min_idx]}\n")
#         #         # then swap places
#         #     print(f"after sub-loop min_idx : {min_idx} value: {intervals[min_idx]}")
#         #     print(f"current intervals: {intervals}\n")

#         #     intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]
#         #     i+=1
#         # print(intervals)

#         # todo: merge these two loops
#         # 
#         print("\nSTAGE 2\n")
#         _len = len(intervals)
#         i = 0 
#         n = len(intervals)
#         while i < n: #[1, 2]

#             print(f"i: {i}")
#             _x = i #represents itself, which will be skipped
#             x = 0
#             a = intervals[i][0]
#             b = intervals[i][1]
            
#             while x < n: #checks next items
#                 print("intervals[x]: ", intervals[x])
#                 print("intervals[x][0]: ", intervals[x][0])
#                 if x==_x:
#                     x+=1

#                 if [_i for _i in range(intervals[i][0], intervals[i][1])] in [_x for _x in range(intervals[x][0], intervals[x][1])]:
#                     print("     !!overlap found!!!")
#                     print(f"    i_ranges {[_i for _i in range(intervals[i][0], intervals[i][1])]}")
#                     print(f"    x_ranges {[_x for _x in range(intervals[x][0], intervals[x][1])]}")

#                 elif a == intervals[x][0]:
#                     print(f"     overlap in a[0] and x[0]: {intervals[x]}:{intervals[i]} ")
#                     biggest= intervals[x] if sum(intervals[x])>sum(intervals[i]) else intervals[i]
#                     intervals.remove(biggest)
#                     n-=1
#                     print(f"     -> delete: {biggest}")

#                 elif b == intervals[x][1]:
#                     print(f"     overlap in a[1] and x[1]: {intervals[x]}:{intervals[i]} ")
#                     biggest= intervals[x] if sum(intervals[x])>sum(intervals[i]) else intervals[i]
#                     intervals.remove(biggest)
#                     n-=1
#                     print(f"     -> delete: {biggest}")

#                 # if [_i for _i in range(intervals[i][0], intervals[i][1])] in [_x for _x in range(intervals[x][0], intervals[x][1])]:
#                 #     print("     !!overlap found!!!")
#                 #     print(f"    i_ranges {[_i for _i in range(intervals[i][0], intervals[i][1])]}")
#                 #     print(f"    x_ranges {[_x for _x in range(intervals[x][0], intervals[x][1])]}")

#                 else: x+=1


#             i+=1
          


#         print("final intervals: ", intervals)
#         return _len-n

           


# class Solution:
#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
#         '''
#         Given an array of intervals intervals where intervals[i] = [starti, endi], 
#         return the minimum number of intervals you need to 
#         remove to make the rest of the intervals non-overlapping.
        
#         Note that intervals which only touch at a point are non-overlapping. 
#         For example, [1, 4] and [2, 3] are non-overlapping.
#         '''

#         print("intervals: ",intervals, len(intervals))
#         # # print("set(): ",set(intervals), len(set(intervals)))
#         # # print("="*20)
#         # # print(f"diff: {len(set(intervals))-len(intervals)}")

        
#         # len_ = len(intervals)
#         # i = 0 
#         # n = len(intervals)
#         # while i < n:
#         #     print("i: ",i)
#         #     a = intervals[i][0]
#         #     b = intervals[i][1]
#         #     y = 1
#         #     min_idx = i #index for the smallest item
#         #     for j in range(i+1, n): #re-iterate list after current position (from current - to n)
#         #         if intervals[j] < intervals[min_idx]: #if the checker value (j) is smaller than current smallest value (min_idx)
#         #             print(f"    current min_idx : {min_idx}")
#         #             min_idx = j #then we set j as the new smallest items
#         #             print(f"    new min found: {intervals[j]} at {j} value: {intervals[min_idx]}\n")
#         #         # then swap places
#         #     print(f"after sub-loop min_idx : {min_idx} value: {intervals[min_idx]}")
#         #     print(f"current intervals: {intervals}\n")

#         #     intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]
#         #     i+=1
#         # print(intervals)

#         # todo: merge these two loops
#         # 
#         print("\nSTAGE 2\n")
#         _len = len(intervals)
#         i = 0 
#         n = len(intervals)
#         while i < n: #[1, 2]

#             print(f"i: {i}")
#             _x = i #represents itself, which will be skipped
#             x = 0
#             a = intervals[i][0]
#             b = intervals[i][1]
            
#             while x < n: #checks next items
#                 # print("intervals[x]: ", intervals[x])
#                 # print("intervals[x][0]: ", intervals[x][0])
#                 if x==_x:
#                     x+=1

#                 print(" convert intervals to ranges:")
#                 # print(f"    i_ranges: {intervals[i]} -> {[_i for _i in range(intervals[i][0], intervals[i][1]+1)]}")
#                 # print(f"    x_ranges: {intervals[x]} -> {[_x for _x in range(intervals[x][0], intervals[x][1]+1)]}")
#                 # if [_i for _i in range(intervals[i][0], intervals[i][1])] in [_x for _x in range(intervals[x][0], intervals[x][1])]:
#                 #     print("     !!overlap found!!!")


#                 # i_list = [_i for _i in range(intervals[i][0]+1, intervals[i][1]+1)]
#                 # x_list = [_x for _x in range(intervals[x][0], intervals[x][1])]
#                 i_list = [_i for _i in range(intervals[i][0], intervals[i][1])]
#                 x_list = [_x for _x in range(intervals[x][0]+1, intervals[x][1]+1)]
#                 print(f"    i_ranges: {intervals[i]} -> {i_list}")
#                 print(f"    x_ranges: {intervals[x]} -> {x_list}")
#                 if not set(i_list).isdisjoint(x_list):
#                     biggest = intervals[x] if sum(intervals[x]) > sum(intervals[i]) else intervals[i]
#                     print(f"     overlap found -> removing {biggest}")
#                     intervals.remove(biggest)
#                     print(f"current intervals: {intervals}")
#                     n-=1

#                 else: x+=1

#                 #> FASIT:  [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]] 5 -> [[2, 6], [3, 7], [4, 8]] disse burde fjernes -> [[1, 5], [5, 9]] -> optimale endringer: 3 


#                 # elif a == intervals[x][0]:
#                 #     print(f"     overlap in a[0] and x[0]: {intervals[x]}:{intervals[i]} ")
#                 #     biggest= intervals[x] if sum(intervals[x])>sum(intervals[i]) else intervals[i]
#                 #     intervals.remove(biggest)
#                 #     n-=1
#                 #     print(f"     -> delete: {biggest}")

#                 # elif b == intervals[x][1]:
#                 #     print(f"     overlap in a[1] and x[1]: {intervals[x]}:{intervals[i]} ")
#                 #     biggest= intervals[x] if sum(intervals[x])>sum(intervals[i]) else intervals[i]
#                 #     intervals.remove(biggest)
#                 #     n-=1
#                 #     print(f"     -> delete: {biggest}")

          

#                 # else: x+=1


#             i+=1
          

# class Solution:
#     '''
#         Given an array of intervals intervals where intervals[i] = [starti, endi], 
#         return the minimum number of intervals you need to 
#         remove to make the rest of the intervals non-overlapping.
        
#         Note that intervals which only touch at a point are non-overlapping. 
#         For example, [1, 4] and [2, 3] are non-overlapping.
#     '''
#     ''' 
#         v 0.1.3 
#         - time limit exceeded, this is good. it is potentially solved now, all i need to do now is to optimize it. 
#         - got error in cases where big intervals where overlapping many small ones, skipping the correct answer. 
#         - refactor sorting criteria  to only care about the endbit- "intervals[j][1] < intervals[min_idx][1]" 
#         - not optimized - sortAccending and eraseOverlapIntervals should be merged into one function. 
#     '''
#     def sortAccending(self, intervals:list[int]) -> list[int]:
#         i = 0 
#         n = len(intervals)

#         while i < n:
#             min_idx = i #index for the smallest item
#             for j in range(i+1, n): #re-iterate list after current position (from current - to n)
                
#                 if intervals[j][1] < intervals[min_idx][1]:
#                      min_idx = j #then we set j as the new smallest items
#             intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]
#             i+=1
#         return intervals

#     def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#         intervals = self.sortAccending(intervals)
#         i = 0
#         n = len(intervals)
#         current_stack = []
#         biggest_stack = [] 

#         while i < n:
#             # build a stack starting with the smallest one. 
#             current_stack.append(intervals[i])
#             for j in range(i+1, n):

#                 end_of_stack = current_stack[-1][1]
#                 start_of_j = intervals[j][0]
#                 if end_of_stack <= start_of_j:
#                     current_stack.append(intervals[j])
            
#             if len(current_stack)>len(biggest_stack):
#                 biggest_stack = current_stack
#                 current_stack = [] #reset current

#             current_stack=[]
#             i+=1
#         return n-len(biggest_stack)        
        
    

#     # def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
#     #     intervals = self.sortAccending(intervals)
#     #     current_stack = []
#     #     biggest_stack = [] 

#     #     i = 0 
#     #     n = len(intervals)
#     #     while i < n:
#     #         # build a stack starting with the smallest one. 
#     #         current_stack.append(intervals[i]) #sets i as satrt of stack 
#     #         [current_stack.append(intervals[j]) for j in range(i+1, n) if current_stack[-1][1] <= intervals[j][0]]  #sub-iteration - append to current stack if next item fits behind last item in current stack. 
#     #         biggest_stack = current_stack if len(current_stack) > len(biggest_stack) else biggest_stack  #set new biggest stack if current is bigger
#     #         current_stack=[] #reset current stack
#     #         i+=1 #try from the next smallest item
#     #     return n-len(biggest_stack)


if __name__ == '__main__':

    # cases = [
    #     [[1,2],[2,3],[3,4],[1,3]],
	# 	[[1,2],[1,2],[1,2]],
	# 	[[1,2],[2,3]]
    # ]


    # cases = [
    # [[1,2],[2,3],[3,4],[1,3]],
    # [[1,2],[1,2],[1,2]],
    # [[-3035,30075],[1937,6906],[11834,20971],[44578,45600],[28565,37578],[19621,34415],[32985,36313],[-8144,1080],[-15279,21851],[-27140,-14703],[-12098,16264],[-36057,-16287],[47939,48626],[-15129,-5773],[10508,46685],[-35323,-26257]],
    # [[-50000,-49999],[0,1],[1,50000]],
    # [[-100,0],[0,100],[50,150],[100,200]],
    # [[1,10000],[2,3],[3,4],[4,5],[5,6]],
    # [[-5,0],[0,5],[5,10],[10,15],[15,20]],
    # [[1,5],[2,6],[3,7],[4,8],[5,9]],
    # [[1,5],[2,3],[1,10],[2,6],[3,7],[4,8],[5,9]],
    # ]

    # fasit = [
    #     1,
    #     2,
    #     9,
    #     0,
    #     1,
    #     1,
    #     0,
    #     3,
    # ]
    

    cases = [
        [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]
# [[-50000, -49999], [0, 1], [1, 49999]]
# [[-10000, 0], [0, 10000], [5000, 15000], [10000, 20000]]
# [[-50000, -40000], [-40000, -30000], [-30000, -20000], [-20000, -10000], [-10000, 0], [0, 10000], [10000, 20000], [20000, 30000], [30000, 40000], [40000, 49999]]
# [[-100, 100], [-50, 50], [0, 200], [150, 300]]
# [[1, 2], [2, 3], [3, 4], [1, 3]]
# [[1, 2], [1, 2], [1, 2]]
# [[1, 49999], [2, 3], [3, 4], [4, 5], [5, 6]]
# [[-5, 0], [0, 5], [5, 10], [10, 15], [15, 20]]

# [[1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]
# [[1, 5], [2, 3], [1, 10], [2, 6], [3, 7], [4, 8], [5, 9]]
# [[1, 2]]
# [[-50000, 50000]]
# [[-50000, 50000], [-50000, 50000]]
# [[-50000, 50000], [0, 1], [0, 1], [0, 1], [0, 1]]
# [[1, 3], [1, 3], [1, 3], [2, 4], [2, 4], [3, 5]]
# [[-50000, 0], [-50000, 0], [0, 50000], [0, 50000]]
# [[1, 5], [2, 5], [3, 5]]
# [[40,70],[56,80],[63,87],[-51,39],[-74,59],[38,41],[-49,17],[6,57],[36,85],[-73,26],[-6,70],[15,70],[66,78],[37,87],[79,96],[46,97],[36,49],[-58,40],[-58,52],[26,83],[-27,43],[15,86],[11,56],[23,34],[-9,73],[-95,-75],[2,30],[-91,26],[88,89],[-83,-43]],
# [[-15372,11264],[-43730,-33388],[-36639,1280],[840,35984],[-38240,17122],[-37497,-1380],[47229,49062],[-45771,43174],[20443,34360],[38798,39394],[-22692,16373],[-22621,-2258],[-81,38395],[15345,23474],[47816,47915],[41254,46599],[3742,19258],[-21774,21717],[-20502,33620],[-3943,45736],[-34683,27103],[-2602,47669],[-12327,-4978],[31334,34657],[23847,24423],[32985,38147],[-48465,-46143],[-587,34382],[1321,15263],[34355,40051],[15231,17384],[-19406,37949],[-41210,-10277],[49437,49809],[20294,33414],[-9945,47909],[-25978,31570],[-23459,-270],[-39323,3649],[20704,47158],[9390,22902],[-30951,41001],[-22087,45648],[33880,45867],[-33066,20339],[-21047,48689],[-21422,-2125],[41226,47928],[-28542,-13315],[737,37308],[-26427,29902],[42985,45839],[-15636,-13388],[19917,33905],[-10932,-795],[-21231,48523],[18034,49519],[42146,46603],[41878,45191],[-10742,49272],[-14630,17346],[-37973,16416],[-8933,3834],[195,23436],[-23276,30992],[-13090,23476],[-16037,37138],[-46535,23597],[-18949,21211],[34775,40394],[38012,42457],[28916,45636],[30231,41588],[-29163,29970],[7383,14037],[36231,47510],[33491,34830],[-47769,16100],[10151,44631],[44448,46454],[-20815,39312],[-11149,4784],[-31615,20562],[-7071,24280],[44438,47060],[42105,43517],[44972,47389],[-20283,12862],[-27426,-10539],[43298,46787],[-42403,-41203],[-947,24956],[-35517,41553],[-31445,38032],[-4948,13590],[48469,48744],[49052,49211],[19225,30642],[47135,47465],[536,49581],[49265,49557],[-6582,24023],[-31874,-25698],[-16722,19314],[8645,37803],[-40008,-12904],[36162,45350],[-35150,-1745],[39404,44513],[-23676,-3443],[-3094,46783],[-9240,5783],[43108,49656],[5594,13530],[5905,40820],[2123,33005],[27006,39150],[1928,40097],[-10916,15155],[32433,41651],[-29984,-23584],[-8912,11468],[18028,39535],[44028,45547],[44556,47105],[-23480,8263],[15828,33008],[19941,23799],[21392,47102],[38146,45275],[36506,49364],[7113,41790],[10695,20390],[20385,34486],[1645,30598],[27856,47537],[-3903,39263],[15403,49988],[42863,47243],[-45457,-3626],[-3506,27738],[-33222,29061],[2693,32720],[3109,48062],[22471,38381],[-36883,27670],[43035,43315],[-5922,40112],[-46602,-161],[-11295,34332],[-43648,20247],[29778,33510],[19672,22727],[-19850,33015],[-37052,6160],[28703,48683],[-38063,-13928],[-32506,8522],[-26847,8576],[-16577,18146],[18621,47977],[-43992,37303],[-38326,22600],[-7214,-2928],[-3633,4717],[-10226,45129],[42314,49998],[-36445,39472],[42587,43861],[9881,46100],[-38553,5621],[29832,31856],[8209,9871],[47513,49066],[-17908,738],[-12576,21921],[40304,45039],[39630,43144],[-30652,1425],[-18632,22113],[-3136,42234],[-9056,2501],[41712,47242],[-14910,6168],[-21145,195],[43337,47032],[2304,8441],[-33801,6787],[-8295,43218],[37925,47530],[-42735,23988],[30571,48581],[6646,36629],[20952,49802],[15209,44963],[-49743,29049],[-46975,-12871],[7537,15058],[17765,36026],[-15709,49468],[-2744,15732],[32934,33430],[17038,26071],[-30756,3873],[-13961,37806],[-27934,35351],[47001,48167],[-28929,-13806],[22330,44780],[31778,37617],[16965,32089],[-40124,-6462],[30488,32797],[17553,24928],[26781,45394],[13394,14553],[19407,37714],[38600,41958],[46801,49401],[4968,39760],[47358,49122],[-10052,47275],[32115,44275],[41227,49539],[13410,28702],[6887,44182],[-15883,-7421],[-14257,43155],[27794,43046],[-16449,33183],[-29676,12899],[-8100,46062],[15043,18283],[30390,35992],[8330,41247],[-19261,-4978],[21340,34000],[-16078,43429],[36508,36762],[-18591,18737],[-6964,42138],[-44387,-40884],[-44805,15441],[-48500,-16460],[26947,40699],[-35624,26089],[-33159,4115],[-49390,22161],[45795,49464],[1453,4902],[10154,20910],[-46178,-40424],[22181,36800],[40976,42828],[28840,40063],[-4356,11048],[-9235,-6644],[-16052,30561],[38433,41437],[-26721,-10238],[13468,44195],[49435,49779],[47037,47865],[21805,36941],[40313,49593],[-8277,10202],[33850,34622],[-26755,-21716],[29980,31215],[33748,38209],[-775,30454],[-42968,-15906],[44663,46849],[-12026,3288],[10361,30621],[37145,39297],[-33706,-24048],[21106,38935],[12621,22211],[-46145,-42868],[-42135,23450],[13971,25189],[7341,23061],[-20940,30038],[-15066,445],[32624,46741],[-35931,49158],[30767,32594],[-20014,1529],[-36941,11697],[-26134,36820],[36237,37385],[-9236,-5751],[41277,49347],[-23039,24442],[39422,43643],[13545,37777],[-6627,28463],[-20666,24278],[-38262,33758],[28211,35526],[-36127,-31763],[11302,36724],[36717,38746],[-30919,33614],[6572,39629],[-14824,-13733],[-27400,42197],[-34294,-9575],[10762,34140],[-17097,-10063],[-1042,33363],[-44219,47665],[-30141,30679],[10772,23965],[12902,42960],[-39817,11661],[30643,33645],[17058,29580],[2274,13963],[16945,40734],[-32494,22701],[21146,49391],[-33442,33949],[-6776,24101],[27160,46590],[7448,17543],[-37228,-22814],[48189,49057],[36536,38983],[8554,25590],[41234,48188],[-39914,6974],[39832,43375],[-42515,-37524],[-12643,3133],[-19611,-10026],[29177,48368],[-2591,40338],[-8183,17232],[-24894,16194],[-32046,10914],[-45685,29424],[-36081,36627],[30152,41836],[27149,27969],[-15390,23230],[12331,25454],[-40357,23506],[25137,44156],[24475,46702],[34600,43077],[-29931,33244],[24816,32631],[-43775,48765],[2730,16185],[9874,37865],[-44277,28574],[31903,44719],[-20949,1923],[85,39916],[-19464,-5884],[-46040,9362],[43693,49831],[37128,46631],[1447,40439],[4153,44725],[41483,48535],[80,38962],[-46898,11213],[-5727,8682],[-45159,-4646],[-2,21848],[6509,18910],[-3615,11448],[29419,49010],[-5183,11015],[-36675,29837],[26240,43321],[-24936,40759],[-44704,33534],[-41214,11706],[2013,42551],[661,30396],[-28445,-14826],[10419,24601],[29093,46896],[39511,44673],[-26147,-13152],[36867,38728],[-5416,8596],[-37167,-31979],[5801,36374],[34907,47961],[-48023,-18650],[-12289,-7583],[-8772,41021],[-4180,40537],[45812,48627],[2248,13168],[-4743,-4416],[20497,28509],[-10295,44183],[29155,40985],[-48210,-13182],[8171,23356],[35251,43313],[-26858,-8314],[-47595,1946],[-44793,47080],[18044,34827],[-5585,2567],[37695,45632],[-10394,11044],[-2181,37298],[-25668,771],[-45779,9781],[-23116,46028],[38065,44943],[-33393,-11700],[-33262,-1657],[29627,41042],[29401,48012],[-12981,4134],[-39368,-10863],[48146,48235],[-39729,-10458],[38176,45408],[12066,47149],[-46174,-43370],[-35773,41530],[-7562,10413],[-43307,-24495],[22723,35549],[-25531,24158],[-11714,22823],[15337,30658],[-13286,25461],[-30988,18585],[-7408,-1148],[-44171,-43750],[-18412,-9974],[27195,41882],[17525,43954],[34375,48556],[-21146,-10553],[-28931,-8863],[-6113,34225],[-15219,39476],[45911,46755],[17812,45829],[20616,38583],[-30817,17261],[10451,38704],[39407,46679],[-33844,-25940],[-15632,17886],[3492,6883],[16322,45147],[-30196,-26219],[34627,38702],[9039,49318],[-5981,40453],[37512,37738],[39457,43522],[-38309,46264],[10303,39051],[-43770,-24646],[21047,28629],[17120,29487],[-40345,48904],[19138,35022],[-3836,29544],[49639,49905],[31465,45873],[39125,42280],[-2435,3028],[-44710,-21652],[35992,40005],[-20399,10983],[-40208,37939],[-16821,2934],[-33300,-14352],[-24867,-1640],[1398,16886],[29836,43768],[-41118,24765],[36292,48569],[18088,26932],[42643,42817],[46458,49537],[-31912,-24784],[-5249,29945],[-42876,26754],[-19513,28662],[41830,42921],[-6798,26210],[-36093,-11486],[19576,45432],[30912,33111],[-42644,15869],[-4380,21062],[-12887,18779],[-57,22255],[-32719,2015],[33586,37955],[-23496,14576],[16702,40523],[-47526,-24679],[-19694,31466],[38322,39280],[-1729,25882],[17738,36866],[-14548,34020],[-22436,-7900],[4200,24068],[48969,49659],[9325,16159],[12001,17043],[1789,33621],[-886,44224],[-20317,-19713],[-4175,38943],[-40661,36751],[31208,36624],[-31226,-26512],[-28248,46470],[-24361,-15497],[-24903,-23844],[-47448,-46206],[-30818,9002],[-21301,21132],[26353,44077],[-33815,-12454],[15788,46823],[-49285,-40490],[11361,36345],[-30626,32500],[-45119,45154],[15225,25105],[-22557,-3320],[2529,19862],[-5876,45105],[-44091,4703],[8959,38737],[-38069,-32643],[-35853,11610],[38899,48897],[-4964,14047],[-10159,14611],[-38863,48705],[-39722,-10293],[-20185,39398],[45084,47581],[18291,45257],[-22944,3687],[-36542,-952],[-40973,-39117],[-33934,36668],[-29768,47656],[9758,37585],[-49173,-35562],[25684,27925],[1548,36146],[9491,15727],[-37992,-37861],[12860,36432],[40954,48741],[32795,34288],[-35373,14597],[-39949,29615],[9906,49108],[49929,49976],[39625,41215],[133,40465],[-9328,-4171],[-18433,12405],[-12747,18575],[45983,47425],[-3192,40945],[18437,21069],[-22385,-12604],[11662,16850],[7527,22944],[27511,39546],[-15563,48267],[-40555,9788],[-12633,46732],[-39170,10551],[18638,32555],[7645,10849],[-19347,11980],[22797,32599],[-27988,-27676],[-3737,46567],[-49471,-32716],[36421,48300],[14024,31476],[48886,49461],[12343,34299],[33629,43209],[-39375,-20471],[37855,49964],[29691,30977],[19147,46870],[13166,14388],[36310,46220],[28379,31258],[-44018,41236],[3244,8865],[28854,40899],[-39496,-12039],[40549,44093],[33118,34286],[38864,42560],[-45816,-15858],[14525,41472],[29170,49671],[27944,42417],[7886,14819],[-27999,34472],[7056,39498],[20974,33069],[15685,34148],[-46882,-39482],[7934,20611],[2683,19871],[-37304,40907],[-41439,-1081],[9162,47295],[42878,49929],[-8708,-2274],[11537,40875],[45100,47966],[24952,29372],[9094,26919],[6403,32185],[40223,40963],[26027,27446],[4835,20090],[-44070,-26230],[-8151,36178],[21705,23548],[44965,45365],[41735,42042],[28920,49430],[39649,45358],[-33378,20667],[41751,45544],[4059,42278],[47075,49628],[15310,22630],[38995,39707],[-17932,-6076],[43599,46103],[-49950,21935],[-41397,-19049],[147,11653],[35564,41032],[-12440,26457],[34070,40897],[27484,29024],[29804,42503],[-2515,16236],[-15025,22730],[3252,30278],[35812,37959],[45672,48526],[-24136,34747],[-25146,-19481],[-48775,19361],[-47889,-31636],[-24941,42868],[45003,49158],[-3190,8707],[-37635,-30336],[41164,42878],[-31093,4412],[7648,10949],[-7016,-3314],[15079,19808],[-46651,39448],[-33067,-3900],[-15218,25275],[27297,42095],[17681,19413],[-10760,11210],[-11352,-7661],[-8577,1357],[-23043,37256],[7678,9059],[3538,9141],[-48255,-19960]]
    ]

    fasit = [
        3,
        # 1,
        # 0,
        # 2,
        # 1,
        # 2,
        # 1,
        # 0,
        # 3,
        # 5,
        # 0,
        # 0,
        # 1,
        # 4,
        # 4,
        # 2,
        # 651,
    ]
    # # TEMP
    # cases = [
    #     [[1,10], [2,3], [3,4]]]
    
    # fasit = [0]
    #> OPTION 1 (for single inputs)
    s = Solution()
    for i, intervals in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        answer = s.eraseOverlapIntervals(intervals)
        print(f"n={i} -> {answer}\n")
        if answer==fasit[i]:
            print("  ==> CORRECT")
        else:
            print("  ==> FALSE")

