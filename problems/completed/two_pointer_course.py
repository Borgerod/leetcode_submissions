'''
DEMO-TASK:
    Given a sorted array A (sorted in ascending order), having N integers;
        -> A = [int * N items] = [10, 20, 35, 50, 75, 80]
    find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X. 
        -> X = 70
            is there a way to add together (+) two elements from A ([10, 20, 35, 50, 75, 80]) to get X (70)?
'''
'''
The idea with pointers is to start in both ends and with trial and error you work your way into the middle. 
instead of the normal way, which would be to work from one end. 


'''
''' ILLUSTRATION

(BASE) __________________________________________________________________

      { 0   1   2   3   4   5} <- index
A[] = {10, 20, 35, 50, 75, 80} <- array

_________________________________________________________________________


(1)
      { [0]   1   2   3   4   [5]} <- index
A[] = {[10], 20, 35, 50, 75, [80]} <- array
X == 70
i = 0
j = 5
        A[i]+A[j] = 90 =/= 70 
        since the first try failed, make adjustment to either i or j, then try again. 
        since A[i]+A[j] > X --> then j-- (or i++)
        
(2) 
i = 0 -> None -> i = 0 
j = 5 -> j-=1 -> j = 4 

      { [0]   1   2   3   [4]   5} <- index
A[] = {[10], 20, 35, 50, [75], 80} <- array

A[i]+A[j] = 10+75 = 85 =/= 70 
since A[i]+A[j] > X --> then j-- (or i++)


(3)
i = 0 -> None -> i = 0 
j = 4 -> j-=1 -> j = 3 

      { [0]   1   2   [3]   4   5} <- index
A[] = {[10], 20, 35, [50], 75, 80} <- array

A[i]+A[j] = 10+75 = 85 =/= 70 
since A[i]+A[j] > X --> then j-- (or i++)


.
.
.
 
Once J == i, the formula will reset, but now i is increased by 1 (+=1) 
then the formula proceeds as normal until j=i again. 

.
.
.

The final stop occours when either; 
    1. The solution(s) has been found. 
    2. The algorythm has ran out of items to check. 

'''





'''EXAMPLE USING PYTHON'''

def isPairSum(a, n, x) -> bool:
    ''' 
        a: array
        n: len(array)
        x: val (the goal)
    '''
    ''' 
        will use l and r as pointers where: 
        "i" is now; "l" for left. 
        "j" is now; "r" is right
    '''

    
    for l in range(n):
        
        print(f"a[l]:{a[l]}")
        for r in range(1, n): 
            r = -r #change r to go ins opposite direction
            print(f"    r={r} : a[r]={a[r]}")
            if (l == r): #skips when l == r 
                print(f"        skip current r ({r})")
                continue

            # make a complete stop when a[l]+a[r] is smaller then x, 
            # since the array is accending, if alar < x:
            # you are garantueed that the iterations after this will not yield a result.  
            if (a[l] + a[r] < x): 
                # print(f"        'R' too small, skip current r ({r})")
                print(f"        'L' too small, skip current l ({a[l]})")
                break 
            
            if (a[l] + a[r] > x):
                break

            if (a[l] + a[r] == x): # break and return true when pair was found
                print(f"        True: a[l] + a[r]: {a[l]} + {a[r]} = {a[l] + a[r]}")
                return True

        print("_"*30)
    print("error, no matches were found, stopping algorythm")
    return False


#WITHOUT THR JARGON
def isPairSum(a, n, x) -> bool:
    ''' 
        a: array
        n: len(array)
        x: val (the goal)
    '''
    
    for l in range(n):
        
        for r in range(1, n): 
            r = -r #change r to go ins opposite direction
            if (l == r): #skips when l == r 
                continue

            # make a complete stop when a[l]+a[r] is smaller then x, 
            # since the array is accending, if alar < x:
            # you are garantueed that the iterations after this will not yield a result.  
            if (a[l] + a[r] < x): 
                break 
            
            if (a[l] + a[r] > x):
                break

            if (a[l] + a[r] == x): # break and return true when pair was found
                return True

    return False


'''
the input an calling the function
'''
array = [2, 3, 4, 5, 9, 10, 11]
val = 14
n = len(array)
print(
    isPairSum(array, len(array), val)
)