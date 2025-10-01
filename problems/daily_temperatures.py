class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        '''
            answer[i] = days  | context: answer[i] = waiting(days) after [i] 
            i: day; point of measure
            answer = [days]
            answer[i] = len_days after i before warmer temperature

             
            temperatures = [     cold,     cold,     cold,     cold,     cold,     warm,     warm ]
                                            |                                        |
                                            i                                       i_hot
                              _ _ _ _ _ _ _ |________________________________________|_ _ _ _ _ _     
                                       '          '        '          '         |         '
                                                                                V
                    days_after_i = [ -1_days,   1_days,   2_days,   3_days,  (4_days),  5_days]  <- Days after i 
                                                                                |
                          answer = [  ---, ---, ---, ---, 4_days] <----- answer[i]
        '''
        answer = []                                                 
        i = 0                                                       
        
        print(f"INPUT: {temperatures[::-1]} \n")
        temperatures_inverted = temperatures[:0:-1]
        temp_check = temperatures_inverted.pop()
        day_counter = 1 

        while i < len(temperatures):
        # while temperatures_inverted:
            print(f"                    {temperatures_inverted} [{temp_check}] [{temperatures[i]}] [temperatures_inverted] [check] [i_temp]")
            i_temp = temperatures[i]


            # if len(temperatures[i:])<1:                
            #     print(f"len({temperatures[i:]})==1 --> BREAK")
            #     print(f"                    {temperatures[::-1]} \n")
            #     print(f"                    {temperatures_inverted} [{temp_check}] [{temperatures[i]}] {answer} [temperatures_inverted] [check] [i_temp]")
            #     if i_temp>temp_check:
            #         answer.append(0)
            #     else:
            #         answer.append(1)
            #     answer.append(0)                   
            #     break     


            # print(f"         XX           {temperatures[::-1]} \n")
            # print(f"         XX           {temperatures_inverted} [{temp_check}] [{temperatures[i]}] {answer} [temperatures_inverted] [check] [i_temp]")

            if len(temperatures_inverted)<1:                
                # if i_temp>temp_check:
                #     answer.append(0)
                # else:
                #     answer.append(1)
                if not temp_check:
                    print(f"len({temperatures_inverted})==1 --> BREAK")
                    print("I AM IN USE")
                    answer.append(0)                   
                    break
            
               
 


            if day_counter == len(temperatures[i:]):
                day_counter = 1
                temperatures_inverted = temperatures[:i:-1]
                i += 1



            if temp_check > i_temp:                 
                print(f"{i}[{day_counter}] : True   {i_temp}<{temp_check} {temperatures_inverted}")
                i += 1
                answer.append(day_counter)          
                day_counter = 1 
                # print("                 XOXO            ", temperatures_inverted)
                if not temperatures_inverted:
                    print(F"               is NOT temperatures_inverted")

                    temperatures_inverted = temperatures[:i:-1]
                    answer.append(0)
                    # day_counter = 1
                else:         
                    print(F"               is temperatures_inverted {temperatures_inverted}")
                    # temperatures_inverted = temperatures[:i:-1]
                    temp_check = temperatures_inverted.pop()
                    print(F"               NEW: {temperatures_inverted} [{temp_check}] [{temperatures[i]}]")
                    print("")

            else:                                  
                print(f"{i}[{day_counter}] : False  {i_temp}>{temp_check} {temperatures_inverted}")
                if not temperatures_inverted:
                    answer.append(0)
                    if len(temperatures[i:])==2:
                        # if temperatures[-1]==temperatures[-2]:
                        #     #TODO
                        #     print("TODO")
                        #     answer.append(0)
                        #     day_counter = 1
                        #     i +=1
                        #     temperatures_inverted = temperatures[:i:-1]
                        # else:
                        answer.append(0)
                    if len(temperatures[i:])<1:
                        answer.append(0)
                        break
                    else:
                        # print("XXXX", temperatures[i:])

                    # else:
                    #     answer.append(0)
                        # break

                    # print("****",temperatures[i:])
                    
                        print(F"               is NOT temperatures_inverted")
                        day_counter = 1
                        i +=1
                        temperatures_inverted = temperatures[:i:-1]
                else:
                    day_counter += 1                
                    temp_check = temperatures_inverted.pop()

        return answer


def main():
    test_cases = [
        # [73,74,75,71,69,72,76,73],
        # [30,40,50,60],
        # [30,60,90],
        # [55,38,53,81,61,93,97,32,43,78],
        [34,80,80,34,34,80,80,80,80,34],

    ]

    s = Solution()
    answers = []
    for case in test_cases:
        answers.append(s.dailyTemperatures(case))
        
    print("\n")
    print("-"*30)
    for i in answers:
        print(i)



if __name__=='__main__':
    main()

'''
inputs:
[73,74,75,71,69,72,76,73],
[30,40,50,60],
[30,60,90],
[55,38,53,81,61,93,97,32,43,78]

expected results:
[1,1,4,2,1,1,0,0]
[1,1,1,0]
[1,1,0]
[3,1,1,2,1,1,0,1,1,0]
'''
        
# # __________________________test zone______________________________
# print("\n")
# # print("_"*30)

# print(f"temperatures:       {temperatures}")
# print(f"temperatures[i:]:   {temperatures[i:]}")
# print(f"temperatures_inverted:   {temperatures_inverted}[{temp_check}] :temp_check")
# # print(f"temp_check = temperatures_inverted.pop({day_counter}):   {temperatures_inverted.pop(day_counter)}")
# # print(f"temp_check = temperatures_inverted.pop():   {temp_check}")

# print()
# print(f"i: {i}  |  day_counter: {day_counter}")
# print(f"i_temp[{i}]: {i_temp}")
# print(f"temp_check[{day_counter}]: {temp_check}")
# print(f"i[day_counter]: {i}[{day_counter}]")
# print("\n")
# # print(f"Error: None of the above occoured")
# # print("\n")
# # __________________________test zone______________________________

