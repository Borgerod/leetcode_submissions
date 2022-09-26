import numpy as np


# TODO: Need restrictions
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = [[i, (target-i)] for index, i in enumerate(nums) if (target-i) in nums[index+1:]]
        return [index for index, i in enumerate(nums) if i in res[0]]

class Input:
    def getInput(self) -> list[int, list[int]]:
        # return 9, [2, 7, 11, 15,]
        # return 6, [3,3]
        return 6, [3,2,4] 

    def getTarget(self) -> int:
        return self.getInput()[0]

    def getNums(self) -> list[int]:
        return self.getInput()[1]

    def makeArray(self) -> np.ndarray:
        return np.array(self.getNums())

def main():
    I = Input()
    s = Solution()
    result = s.twoSum(I.makeArray(), I.getTarget())
    print(result)

if __name__ == '__main__':
    main()

'''
* NOTE TO SELF:
    * Explaining the "-> int" in a function, e.g.: "def foo(x) -> int:"
          the "-> int" is called "function annotations" and covered in PEP 3107 (https://peps.python.org/pep-3107/)
        * What is it? 
            It is essensially just documentenation, and is not nessasary (most likely)
        * What does it do? 
            it's just informing the reader, what the function is supposed to return.             
        * What does it not do?
            force the function to return certain datatype e.g.: an "int" 
        * PS: 
              Sometimes the "reader" could be other libraries/programs, 
              and therefore the function annontation could have more non-trivial / useful functions, 
              and could even be nessesary in some cases. But usually not. 

    * Relating to "function annotations":
        python also supperts "parameter annontations", e.g.:
        
            def g(x: float) -> int:
                return int(x)

        here you are informing the reader that 
        "x" is a "float", and "f(x)" returns an "int"
''' 

