from data import data 


class Solution:               
    def longestConsecutive(self, nums: list[int]) -> int:
        '''
            Longest consecutive sequence = longest uninterupted range. e.g.: 1,2,3,4,5
            return the len of that number. 
            (or the highest number - the lowest) --> 3,4,5,6,7 = 7-3 = 4 
        '''
        if len(nums)==0:
            return 0
        
        elif len(nums)==1:
            return 1

        nums = sorted(set(nums))
        len_nums = len(nums)

        current_seq = []
        max_seq = [] #temp sequence made from max(end)
        min_seq = [] #temp sequence made from min(start)
        y_counter = 0 
        i_counter = 0

        for i,y in zip(range(0,len_nums), range(1, len_nums)):
            y += y_counter
            i += i_counter

    
            if i+1 == len(nums) or y == len(nums):
                print(True)
                if i+1>=len(nums) or y+1>=len(nums):
                    print(True)
                    break
            else:
                if i+2>len(nums)or y+2>len(nums):
                    break
            # if i+1 >= len(nums) or y>=len(nums):
            #     break

        
            # print(nums, -y)
            max_ = nums[-y]
            next_max = nums[-(y+1)]

            min_ = nums[i]
            next_min = nums[i+1]
            
            # # ''' __________ CHECKING FROM MAXIMUM __________ '''
            # print(nums)

            # if next_max == max_-1:
            #     max_seq.append(max_)
            #     max_seq.append(next_max)

            #     if max_ == nums[-1]:
            #         subnums = nums[:-y]
            #     else:
            #         subnums = nums[:-y+1]
            #     for y_, _ in  enumerate(subnums):
            #         if y_+2 > len(subnums):
            #             break
            #         next_y = subnums[-(y_+2)]
            #         y_counter += 1
            #         if next_y != max_seq[-1]-1:
            #             break
            #         max_seq.append(next_y)
            # if len(max_seq) > len(current_seq):
            #     if current_seq and max_seq[0] != current_seq[-1]:
            #         current_seq.clear()
            #     current_seq+=max_seq
            # max_seq.clear()
                

            ''' __________ CHECKING FROM MINIMUM __________'''
            if next_min == min_+1:
                # print("min_ = TRUE")
                min_seq.append(min_)
                # min_seq.append(next_min)
                # print(min_seq)

                if min_ == nums[0]:
                    subnums = nums[i:]
                else:
                    subnums = nums[i-1:]

                for i_, _ in  enumerate(subnums):
                    if i_+2 == len(subnums):
                        # print("TRUE, BREAKING")
                        break
                    next_i = subnums[(i_+2)]
                    i_counter += 1
                    
                    if next_i != min_seq[-1]+1:
                        # print("TRUE, BREAKING",next_i,  min_seq[-1]+1)
                        break
                    min_seq.append(next_i)

            if len(min_seq) > len(current_seq):
                if current_seq and min_seq[-1] != current_seq[0]:
                    current_seq.clear()
                current_seq+=min_seq
            min_seq.clear()
        # print(current_seq)
        len_seq = len(set(current_seq))
        return len_seq if len_seq>0 else 1
        



if __name__ == '__main__':
    s = Solution()
    i=0
    for nums in data[:4]: #data[:3]:
        #print(f"nums sorted: \n {(nums)}")
        res = s.longestConsecutive(nums)
        print(f"i:{i}  res = {res}")
        i+=1
        # break