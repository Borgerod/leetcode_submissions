import time
start_time = time.time()



class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])                
        limit = len(intervals)
        i = 0
        while i < limit:
            if not i or intervals[i-1][1] < intervals[i][0]: #not overlap
                i+=1
            else:
                intervals[i-1] = [intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])] #overlap
                intervals.pop(i)
                i-=1
                limit-=1
        return intervals




# class Solution:
            
    # def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    #     ''' note:
    #     a : start of the interval 
    #     b : end of the interval 
    #     So intervals looks like this: 
    #         intervals = [[a, b], [a, b]]
    #     '''
    #     intervals.sort(key = lambda x: x[0])    #sorts the array by the key, where the "key" = x[0] for x in intervals (aka a)
    #     a, b = map(list, zip(*intervals))       #split intervals into two arrays; a & b
    #     limit, i , next = len(a)-1, 0, 1        #defining the limit, iterator for item and next item 
    #     while i < limit:             
    #         if b[i] >= a[next]: #! MERGE
    #             if b[i] < b[next]:
    #                 b[i] = b[next]              #adjust i if next is bigger
    
    #             b.pop(next), a.pop(next)        #remove next
    #             limit -= 1                      #reduce limit since a element is removed
    #             # i, next = 0, 1                  #restarts process to check adjusted i
    #             # i, next = 0, 1                  #restarts process to check adjusted i
    #             next -= 1
    #             i-=1
    #             if i < 0:
    #                 i=0
    #         else:
    #             next += 1
    #             i+=1
    #     return list(map(list, zip(a, b)))
            
# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         ''' note:
#         a : start of the interval 
#         b : end of the interval 
#         So intervals looks like this: 
#             intervals = [[a, b], [a, b]]
#         '''
#         intervals.sort(key = lambda x: x[0])    #sorts the array by the key, where the "key" = x[0] for x in intervals (aka a)
#         a, b = map(list, zip(*intervals))       #split intervals into two arrays; a & b
#         limit, i , next = len(a)-1, 0, 1        #defining the limit, iterator for item and next item 
#         while i < limit:             
#             if b[i] >= a[next]: #! MERGE
#                 if b[i] < b[next]:
#                     b[i] = b[next]              #adjust i if next is bigger
    
#                 b.pop(next), a.pop(next)        #remove next
#                 limit -= 1                      #reduce limit since a element is removed
#                 i, next = 0, 1                  #restarts process to check adjusted i
#             else:
#                 next += 1
#                 i+=1
#         return list(map(list, zip(a, b)))















class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])      
              
        a, b = map(list, zip(*intervals))               
        limit, i = len(a)-1, 0                          
        
        while i < limit: 
            next = i+1
            if b[i] >= a[next]:                         
                if b[i]<b[next]:                        
                    b[i] = b[next]                      
    
                b.pop(next), a.pop(next)                
                limit-=1                                
                i=0                                     
            else:                                       
                i+=1
                
        return list(map(list, zip(a, b)))               
            
          





















class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])    #sorts the array by the key, where the "key" = x[0] for x in intervals (aka a)
        a, b = map(list, zip(*intervals))       #split intervals into two arrays; a & b
        limit, i , next = len(a)-1, 0, 1        #defining the limit, iterator for item and next item 
        while i < limit:             
            if b[i] >= a[next]: #! MERGE
                if b[i] < b[next]:
                    b[i] = b[next]              #adjust i if next is bigger
    
                b.pop(next), a.pop(next)        #remove next
                limit -= 1                      #reduce limit since a element is removed
                i, next = 0, 1                  #restarts process to check adjusted i
            else:
                next += 1
                i+=1
        return list(map(list, zip(a, b)))
            
            




            
            
            
 




class Solution:
            
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ''' note:
        a : start of the interval 
        b : end of the interval 
        So intervals looks like this: 
            intervals = [[a, b], [a, b]]
        '''
        intervals.sort(key = lambda x: x[0])            #sorts the array by the key, where the "key" = x[0] for x in intervals (aka a)
        a, b = map(list, zip(*intervals))               #split intervals into two arrays; a & b
        limit, i = len(a)-1, 0                          #defining the limit, iterator for item and next item
        while i < limit: 
            next = i+1
            if b[i] >= a[next]:                         #MERGE if current b is not smaller than next a 
                if b[i]<b[next]:                        
                    b[i] = b[next]                      #adjust i
    
                b.pop(next), a.pop(next)                #remove next
                limit-=1                                #reduce limit since a element is removed
                i=0                                     #restarts process to check adjusted i
            else:                                       #else iterate. (need this since it could mess with i when soft resetting (when i=0))
                i+=1
        return list(map(list, zip(a, b)))               #return the merged array





















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

