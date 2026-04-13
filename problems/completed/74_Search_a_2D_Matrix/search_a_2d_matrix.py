class Solution:
    
    def binarySearch(self, arr, target) ->bool:
                
        left = 0  #index
        right = (len(arr)) - 1 #index
        while left <= right:
            mid = (left + right) // 2 #index of center of array

            if arr[mid] == target: #target aquired
                return True
            
            if target > arr[mid]:
                # look right
                left = mid + 1

            else: #if matrix[mid] > target
                # look left
                right = mid - 1

        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        '''
        #> time complexity goal: O(log(m * n))

        return goal: find target:int in matrix then return True, else False.
        '''
        ''' How it works: 

            treats each row as a value, then just simply apply binary search for it. except were checking start and end of row, instead of middle value.
            once the corret row is found -> apply a normal binary search to that specidic row.
        '''        
            
        left = 0  #index
        right = (len(matrix)) - 1 #index

        while left <= right:
            mid = (left + right) // 2 #index of center of array
            row = matrix[mid]

            if target >= row[0] and target <=row[-1]: 
                return self.binarySearch(row, target)

            if target < row[0] :  #target is smaller than 'start of' middle row  
                right = mid - 1

            else:
                left = mid + 1
        return False

    
if __name__ == '__main__':
    cases = [
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3,
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13,
        [[-10000 + i * 100 + j for j in range(100)] for i in range(100)], -10000,
        [[-9900 + i * 100 + j for j in range(100)] for i in range(100)], 10000,
        [[-5000 + i * 100 + j for j in range(100)] for i in range(100)], 0,
        [[-1000 + i * 100 + j for j in range(100)] for i in range(100)], 9999,
        [[i for i in range(100)]], 50,
        [[i * 2 - 10000] for i in range(100)], 100
    ]

    fasit = [
        True,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
    ]

    s = Solution()
    for i in range(0, len(cases), 2):
        matrix = cases[i]
        target = cases[i+1]
        ans = s.searchMatrix(matrix, target)
        idx = i // 2
        print(f"___ NO.{idx+1} ___________________________________")
        print(f"n={i} -> {ans}  => {'CORRECT' if ans == fasit[idx] else 'WRONG'}\n")
        print(f"fasit:{fasit[idx]}")