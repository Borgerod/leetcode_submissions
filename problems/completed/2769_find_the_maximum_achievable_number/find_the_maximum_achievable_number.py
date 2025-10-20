class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        ''' 
            x: the highest number possible to make it work.
        '''
        max = 0
        x = 0
        num_ = num
        for i in range(t):
            num_ +=1
            x -=1
        # print(f"num:{num} -> num_:{num_}")
        # print(f"x:{x} -> x+num:{abs(x)+num_}")
        max=abs(x)+num_
        
        # the other way around:
        for i in range(t):
            num_ -=1
            x +=1
        # print(f"num:{num} -> num_:{num_}")
        # print(f"x:{x} -> x+num:{abs(x)+num_}")
        return abs(x)+num_ if abs(x)+num_>max else max


    def theMaximumAchievableX(self, num: int, t: int) -> int:
        #Somehow i dont believe that its this simple
        x = 0
        for _ in range(t):
            num +=1
            x -=1
        return abs(x)+num

    def theMaximumAchievableX(self, num: int, t: int) -> int:
        #no way this will work
        ''' if x is the max number, that meens we need to achiefve the biggest 
        distance. ergo x and num must move in constant different directions 
        for t times. thus x moves t times negativly and num moves 
        t times positivly, then we add that to whatever num is.
        and we get:  
        '''
        return num+(t*2)




if __name__ == '__main__':

    cases = [
        4,
        1,
        3,
        2,
        15,
        7,
        25,
        10,
        50,
        50,
        1,
        1,
        42,
        20,
        30,
        15,
        8,
        5,
        19,
        12,
    ]
    
    s = Solution()
    for i in range(0, len(cases), 2):
        num = cases[i]
        t = cases[i + 1]
        print(f"___ NO.{i//2} ___________________________________")
        # print(f"     num:{num} \n  =>  ans:{s.theMaximumAchievableX(num)}\n")
        print(f" =>  ans:{s.theMaximumAchievableX(num, t)}\n")
        # s.theMaximumAchievableX(num, t)
