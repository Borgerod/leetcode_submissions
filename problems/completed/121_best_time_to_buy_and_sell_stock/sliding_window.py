import sys

def maxSum(arr, n, k):

    ''' 
        gets the sum of every 'k' elements in 'arr' 
        then returns the biggest one
        *NOTE: each iteration the slider slides by 1
        *NOTE: it does NOT slide the slider by 3 (k)
        k=3 which means it sums ever 3 elements
        [5, 2, -1, 0, 3]
        [(5, 2, -1,) 0, 3] -> (5)+(2)+(-1)=6
        [5, (2, -1, 0,) 3] -> (2)+(-1)+(0)=1
        [5, 2, (-1, 0, 3)] -> (-1)+(0)+(3)=2
        returns => 6
    '''

    # Initialize result
    max_sum = -sys.maxsize

    # Consider all blocks starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        window = []
        # update results if required
        for j in range(k):
            current_sum += arr[i + j]
            window.append(arr[i + j])
        print(f"Window {i+1}: {window} -> Sum: {current_sum}")
        max_sum = max(current_sum, max_sum)
        print(f"Current max_sum: {max_sum}\n")

    print(f"Final max_sum: {max_sum}")
    return max_sum


if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3,4]
    k = 3
    n = len(arr)
    print(maxSum(arr, n, k))



class Solution:
    def visualize(self, _string, hash_set, R, L, counter, max_count):
        print(f'    string: "{_string}" | char -> "{_string[R]}"')
        print(f"    L:{L} | R:{R} ")
        print(f"    set:{hash_set}")
        print(f"    counter:{counter} | max_count:{max_count}")
        print(f"    counter>max_count:{counter>max_count}")
        if counter>max_count: 
            print(f"    ** MAX changed: max={max_count}")
        print()

    def longestSubstring(self, _string:str) -> int:
        
        '''
        
        '''
        max_count = 0 # over all max
        counter = 0 # the counter for every set, or "sub-max", will replace max when bigger
        n = len(_string)
        L=0 # window handle
        R=0 # window handle

        hash_set:list=[] #represents a set 

        # for char in _string:
        while R != n:

            
            
            self.visualize(_string, hash_set, R, L, counter, max_count)

            if _string[R] not in hash_set:
                # continue
                hash_set.append(_string[R])
                counter+=1
                R+=1
                # print(f"    counter:{counter}")
                # print(f"    counter>max_count:{counter>max_count}")
                if counter>max_count: 
                    max_count=counter
                    # print(f"    ** MAX changed: max={max_count}")
            else:
                # reset then continue 
                hash_set=[]
                counter=0
                L=R
            # print()

        return max_count

if __name__ == '__main__':

    cases = [
        "abccbad",
        # "aaabba",
    ]

#> OPTION 1 (FOR SINGLE INPUTS)
    s = Solution()
    for i, _string in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"Input: string={(str(_string[:10])[:-1] + f', ... {_string[-1]}]') if isinstance(_string, list) and len(_string) > 10 else _string}")
        ans = s.longestSubstring(_string)
        print(f"Output: {ans}\n")

