import time
start_time = time.time()













class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])                
        # print("before: ", intervals)
        limit = len(intervals)
        i = 0
        while i < limit:
            
            # print(i, limit, intervals[i])
            # if not i or intervals[-1][1] < intervals[i][0]: #not overlap
            if not i: #not overlap
                # print("     i = 0")
                i+=1
            # elif intervals[-1][1] < intervals[i][0]: #not overlap
            elif intervals[i-1][1] < intervals[i][0]: #not overlap
                # print(f"     current_end < next_end, {intervals[i-1][1]} < {intervals[i][0]}")
                i+=1
            else:
                # print(f"     Is overlap: intervals[-1]: {intervals[i-1]}, next_end[i]: {intervals[i]}")
                intervals[i-1] = [intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])]#overlap
                # print("         merged into new interval: ", intervals[i-1])
                # print(f"     poppping {intervals[i]}")
                intervals.pop(i)
                i-=1
                limit-=1
            # i+=1
        # print("\nafter: ", intervals)
        return intervals
        
        
        






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# MaIN
intervals_list = [
[[10,16],[2,6],[8,10],[15,18]],
[[1,3],[2,6],[8,10],[15,18]],
[[1,7],[2,3],[5,10],[12,14]],
[[1,2],[2,3]],
[[0,2],[2,3]],
[[1,2],[0,0]],
    ]


x=0
for intervals in intervals_list:
    x+=1
    res=Solution().merge(intervals)
    print(f"NO: {x}: {res}")



#* Timer
time.sleep(.1)
diff = time.time()-start_time-.1
print(f"Elapsed time: {diff:.6f} s | {(diff)*1000:.3f} Ms")



'''
FASIT
       [[2, 6],  [8, 10], [10, 18]],      [[2, 6], [8, 10], [10, 16], [15, 18]], 
       [[1, 6],  [8, 10], [15, 18]],      [[1, 3], [2, 6], [8, 10], [15, 18]], 
       [[1, 10], [12, 14]],              [[1, 7], [2, 3], [5, 10], [12, 14]], 
       [[1, 2],  [2, 3]],                [[1, 2], [2, 3]], 

'''

'''
    1: [[2, 6], [8, 10], [10, 18]]
    2: [[1, 6], [8, 10], [15, 18]]
    3: [[1, 3], [5, 10], [12, 14]]
    4: [[1, 2], [2, 3]]
'''

''' NY FASIT                                    ORIGINAL
    1: [[2, 6], [8, 18]]                        [[2,6],[8,16], [15,18]],
    2: [[1, 6], [8, 10], [15, 18]]              [[1,3],[2,6],[8,10],[15,18]],
    3: [[1, 10], [12, 14]]                      [[1,7],[2,3],[5,10],[12,14]],
    4: [[1, 3]]                                 [[1,2],[2,3]],
    5: [[0, 3]]                                 [[0,2],[2,3]],
    6: [[0, 0], [1, 2]]                         [[1,2],[0,0]],
'''

'''
    1: [[2, 6], [8, 18]]
    2: [[1, 6], [8, 10], [15, 18]]
    3: [[1, 10], [12, 14]]
    4: [[1, 3]]
    5: [[0, 3]]
    6: [[0, 0], [1, 2]]

'''