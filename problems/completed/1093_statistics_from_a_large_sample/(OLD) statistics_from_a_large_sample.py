''' PROBLEM:
    You are given a large sample of integers in the range [0, 255]. 
    Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

    Calculate the following statistics:
        - minimum: The minimum element in the sample.
        - maximum: The maximum element in the sample.
        - mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
        - median:
            - If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
            - If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
        - mode: The number that appears the most in the sample. It is guaranteed to be unique.
        
        Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.
'''
 
''' EXAMPLES & CONSTRAINTS
Example 1:
    Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
    Explanation: The sample represented by count is [1,2,2,2,3,3,3,3].
    The minimum and maximum are 1 and 3 respectively.
    The mean is (1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375.
    Since the size of the sample is even, the median is the average of the two middle elements 2 and 3, which is 2.5.
    The mode is 3 as it appears the most in the sample.

Example 2:
    Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
    Explanation: The sample represented by count is [1,1,1,1,2,2,2,3,3,4,4].
    The minimum and maximum are 1 and 4 respectively.
    The mean is (1+1+1+1+2+2+2+3+3+4+4) / 11 = 24 / 11 = 2.18181818... (for display purposes, the output shows the rounded number 2.18182).
    Since the size of the sample is odd, the median is the middle element 2.
    The mode is 1 as it appears the most in the sample.
 

Constraints:
    count.length == 256
    0 <= count[i] <= 109
    1 <= sum(count) <= 109
    The mode of the sample that count represents is unique.

'''

from random import sample
import numpy as np 

class Solution:
    
    def __init__(self,min_,max_) -> None:
        self.sample_range = range(min_,max_)

    def sampleStats(self, count: list[int]) -> list[float]:
        
        self.count = count 
        self.count_dict = dict.fromkeys(count, 0)
        self.optimizeData()
        self.count = list(self.count_dict.values())
        print()
        return self.getMin(), self.getMax(), self.getMean(), #self.getMedian(), self.getMode()

    def optimizeData(self):
        for i in self.sample_range:
            occurrance = self.count.count(i)
            self.count_dict[i] = occurrance
        sorted_count_dict = sorted(self.count_dict.items(), key=lambda x:x[1])
        self.count_dict = dict(sorted_count_dict)


    def dropZeros(self):
        self.zero_dropped = {k:v for k,v in self.count_dict.items() if v != 0}

    def getMin(self):
        return min(self.count)
    #     # self.dropZeros()
    #     return min(self.count)

    def getMax(self):
        return max(self.count)
        # return max(list(self.zero_dropped.keys()))

    def getMean(self):
        return sum(self.count)/len(self.count)
        self.tot_count = 0
        tot_value = 0
        for key, i in zip(self.count_dict.keys(), self.count_dict.values()):
            tot_value+=key*i
            self.tot_count+=i
        return tot_value/self.tot_count


    def getMedian(self):
        key_sorted_dict = dict(sorted(self.count_dict.items()))
        median_value = self.tot_count/2
        for i in key_sorted_dict:
            median_value -= key_sorted_dict.get(i)
            if median_value == 0 or (median_value <= 1 and median_value <= 0):
                return i 


    def getMode(self):
        return max(self.count_dict, key=self.count_dict.get)

def getSample(sample_size:int, min_:int, max_:int) -> np.array:
    # return random.sample((list(range(min_, max_))*sample_size), sample_size)
    return [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


if __name__ == '__main__':
    min_, max_ = 0, 4 
    sample = getSample(sample_size=10, min_=min_, max_=max_)
    s = Solution(min_, max_)
    result = s.sampleStats(sample)
    print(result)


# class Solution:
    
#     def __init__(self,min_,max_) -> None:
#         self.sample_range = range(min_,max_)

#     def sampleStats(self, count: list[int]) -> list[float]:
        
#         self.count = count 
#         self.count_dict = dict.fromkeys(count, 0)
#         self.optimizeData()
#         
#         return self.getMin(), self.getMax(), self.getMean(), self.getMedian(), self.getMode()

#     def optimizeData(self):
#         for i in self.sample_range:
#             occurrance = self.count.count(i)
#             self.count_dict[i] = occurrance
#         sorted_count_dict = sorted(self.count_dict.items(), key=lambda x:x[1])
#         self.count_dict = dict(sorted_count_dict)


#     def dropZeros(self):
#         self.zero_dropped = {k:v for k,v in self.count_dict.items() if v != 0}

#     def getMin(self):
#         self.dropZeros()
#         return min(list(self.zero_dropped.keys()))

#     def getMax(self):
#         return max(list(self.zero_dropped.keys()))

#     def getMean(self):
#         self.tot_count = 0
#         tot_value = 0
#         for key, i in zip(self.count_dict.keys(), self.count_dict.values()):
#             tot_value+=key*i
#             self.tot_count+=i
#         return tot_value/self.tot_count


#     def getMedian(self):
#         key_sorted_dict = dict(sorted(self.count_dict.items()))
#         median_value = self.tot_count/2
#         for i in key_sorted_dict:
#             median_value -= key_sorted_dict.get(i)
#             if median_value == 0 or (median_value <= 1 and median_value <= 0):
#                 return i 


#     def getMode(self):
#         return max(self.count_dict, key=self.count_dict.get)

# def getSample(sample_size:int, min_:int, max_:int) -> np.array:
#     # return random.sample((list(range(min_, max_))*sample_size), sample_size)
#     return [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# if __name__ == '__main__':
#     min_, max_ = 0, 4 
#     sample = getSample(sample_size=10, min_=min_, max_=max_)
#     s = Solution(min_, max_)
#     result = s.sampleStats(sample)
#     print(result)
