class Solution:
    # SOL 1.0)
    def differenceOfSums(self, n: int, m: int) -> int:
        # print(n, m)
        num1 = 0 #sum ints in rane [1,n]: that are NOT devisible by m
        num2 = 0 #sum ints in rane [1,n]: that ARE devisible by m
        i=0
        n_range = range(1,n+1)
        print(f"n: {n} | m: {m}")
        print(f"range[1,n]: {n_range}")

        while i < len(n_range):
            x,res = divmod(n_range[i], m)

            
            print(f"n_range[i]/m: {n_range[i]}/{m} | x:{x} | res:{res}")
            if res:
                num1+=n_range[i]
            else:
                num2+=n_range[i]
            i+=1

        print(f" num1:{num1} - num2:{num2} = {num1-num2}")
        return num1 - num2
    
    # SOL 1.1) Cleaned
    def differenceOfSums(self, n: int, m: int) -> int:
        num1,num2,i = 0,0,0
        n_range = range(1,n+1)
        while i < len(n_range):
            _,res = divmod(n_range[i], m)            
            if res: num1 += n_range[i]
            else: num2 += n_range[i]
            i+=1
        return num1 - num2
 
    # SOL 2.0) For loop
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2, i = 0, 0, 0
        for i in range(1, n+1):
            _,res = divmod(i, m)
            if res: num1 += i
            else: num2 += i
        return num1 - num2
    
    # SOL 3.0) For loop is_integer
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2, i = 0, 0, 0
        for i in range(1, n+1):
            if (i/m).is_integer():
                num2 += i
            else:
                num1 += i
        return num1 - num2

    # SOL 4.0) list comprehension
    def differenceOfSums(self, n: int, m: int) -> int:
        num2 = sum([i for i in range(1, n+1) if (i/m).is_integer()])
        return (sum(range(1, n+1))-num2) -num2 #(sum(range(1, n+1))-num2) --> num1
    
    # SOL 4.1) list comprehension, no variabled, compresed
    def differenceOfSums(self, n: int, m: int) -> int:   
        return (sum(range(1, n+1))-(sum([i for i in range(1, n+1) if (i/m).is_integer()]))*2)


    # SOL 1.2) while loop; is_integer
    def differenceOfSums(self, n: int, m: int) -> int:
        num1,num2,i = 0,0,0
        n_range = range(1,n+1)
        while i < len(n_range):
            if (n_range[i]/m).is_integer(): num2 += n_range[i]
            else: num1 += n_range[i]
            i+=1
        return num1 - num2
 

if __name__ == '__main__':

    cases = [

        10,3,
        5,6,
        5,1,
        500, 7,
        250, 15,
        750, 23,
        100, 4,
        999, 13,
        300, 9,
        450, 12,
        800, 25,
        150, 6,
        600, 18
    ]

    s = Solution()
    for i in range(0, len(cases), 2):
        if i + 1 < len(cases):
            n = cases[i]
            m = cases[i + 1]
            print(f"___ NO.{i//2 + 1} ___________________________________")
            print(f"n={n}, m={m} -> {s.differenceOfSums(n, m)}\n")


'''
expected outputs: 
    1: 19
    2: 15
    3: -15
'''