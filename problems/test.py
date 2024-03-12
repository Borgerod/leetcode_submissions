# # class Solution:

# #     @property
# #     def description(self) -> None:
# #         ''' Problem explaination: 
# #             you are given a string of math-related chars, (integers: range(-200, 200) and special_chars: ["+", "-", "*", "/"])
# #             your job is to combine those into a valid math equation, then return the answer.
           
# #            Example 1:

# #                 Input: tokens = ["2","1","+","3","*"]
# #                 Output: 9
# #                 Explanation: ((2 + 1) * 3) = 9 
        
        
# #             Rules:
# #             - divition: allways round up towards zero.  (round up to whole numbers)
# #             - no divition by zero 
# #             - will not begin with speacial (-1+1=0) and will contain double operator (1-(-1)=2)

# #         simply put: describe the math notation from here (https://en.wikipedia.org/wiki/Reverse_Polish_notation) into code.  
# #         ''' 

        
# #         ''' 
# #         it will work in pairs, then trios.
# #                     1    numbers will be paired, starting at the end of the list
# #                     2    then numbers and expresssion wil be trebled,(numbers paired with the closest expresion)
# #                     3    lets call the first treble as "x" for simplisity
# #                     *    then repeat the previous steps untill all numbers and expressions has been trebled. 
# #                     4    translate to conventional math notation (1+1=2)
# #                     5    solve the ecuation and return result. 
# #         2 1 10 / + ==>  2 [1 10] / +  ==> 2 ([1 10] /) + ==> 2 x + ==> ([2 x] - ) ==> ([2 ([1 10] /)] - ) ==> (2-(1/10))
# #         '''
  


# #     def makeStack(self, tokens[str]) -> list[str]:



# #     def evalRPN(self, tokens: list[str]) -> int:
# #         operator = ["+", "-", "*", "/"]
# #         sum = 0 
# #         res = 0 
# #         int_pair = []
# #         expression=""
# #         # x_list = []
# #         print(tokens, "\n")
# #         i=0
# #         stack=[]
# #         while i < len(tokens):
# #             print(f"i: {i} tokens: {tokens} stack: {stack}")
            

# #             # if stack and 



# #             if i+2 <= len(tokens):

# #                 if tokens[i+2] not in operator:
# #                 # will skip intill it finds a suitable match for criteria (int int operator)
# #                     print(f"{tokens[i+2]} is NOT an operator, moving tokens[i]:{tokens[i]} to stack")
# #                     stack.append(tokens[i])
# #                     tokens.pop(i)
# #                     i = -1
# #                 else:

# #                     int_pair.append(tokens[i])
# #                     # int_pair=[i,i+1]
# #                     if tokens[i+2] == "/":
# #                         expression = f"int({tokens[i]}{tokens[i+2]}{tokens[i+1]})"
# #                     else:
# #                         expression = f"({tokens[i]}{tokens[i+2]}{tokens[i+1]})"
# #                     int_pair.append(expression)
# #                     print(tokens)
# #                     tokens.pop(0),tokens.pop(0),tokens.pop(0)
                    
                    
                    
# #                     if stack:
# #                         tokens.insert(0,stack[-1])
# #                         stack.pop()
# #                     print(expression, tokens, stack)
 
# #                     print("FINAL STEP: returning final expression")
# #                     if len(tokens)==2:
# #                         print(f"len tokens = {len(tokens)}")
# #                         if tokens[-1] in operator:
# #                             print("FINAL EXPRESSION:",f"({tokens[0]}{tokens[1]}{expression})")
# #                             return eval(f"({tokens[0]}{tokens[1]}{expression})")
                            

# #                         #     if tokens:
# #                         #         print("TRUE, ", tokens)
# #                         # else:
# #                         #     print(f"ERROR; {tokens}")


# #                     # elif len(tokens)==1:
# #                     #     print(f"len tokens = {len(tokens)}")
# #                     #     print("ERROR, something weird happends:")
# #                     #     print(expression, tokens, stack)

# #                     # if len(tokens)==0:
# #                     #     print(True)
# #                     #     print(f"len tokens = {len(tokens)}")
# #                     #     #ready to return
# #                     #     print("FINAL", expression, tokens, stack)
# #                     #     return eval(expression)


# #             print("current expression: ", expression)
# #             i+=1
   

# #         return sum
    




# # class Stack:
# #     def __init__(self):
# #         self.stack = []
# #         self.first_operator = ""
        
# #     def push(self, val: int) -> None:
# #         self.stack.append(val)
        
# #     def pop(self) -> None:
# #         self.stack.pop()
# #     def typeConverter(self, ) -> list[int, str]:
# #         ''' 
# #             used by Stack.findTypeSequence(), 
# #             will convert the stack of strings back to its original typing
# #         '''
# #         return [int(x) if x.isdigit() or (x[0] == '-' and x[1:].isdigit()) else x for x in self.stack]



# #     def findTypeSequence(self)->None:
# #         ''' 
# #             will temporarily convert list to its original format (ints will be int, operators will be strings) 
# #             then look for the first instance of "int int str"
# #             this will be the starting point of the algorithm. 
# #             NOTE: might change to "look for every instances of..") 
# #         '''
        
        
# #         i=0
# #         sequence = [int, int, str]
# #         type_converted_stack = self.typeConverter()

# #         while True:
            
        
# #     def top(self) -> int:
# #         return self.stack[-1]
        
# #     def firstOperator(self) -> int:
# #         return self.first_Operator
            





# # if __name__ == '__main__':
# #     for i, case in enumerate([
# #         # ["2","1","+","3","*"],
# #         # ["4","13","5","/","+"],
# #         ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
# #     ]): 
# #         print(
# #        f"Result case_{i}: {Solution().evalRPN(case)}"
# #     )
       

# def find_first_sequence_occurrence(self,)-> list[int,int,str]:
#     ''' finds the first occurrence'''
#     sequence = [int, int, str]
#     stack = [10, 6, 9, 3, '+', -11, '*', '/', '*', 17, '+', 5, '+']

#     first_occurrence = []

#     for i in range(len(stack) - len(sequence) + 1):
#         current_sequence = stack[i:i + len(sequence)]

#         if all(isinstance(current_sequence[j], sequence[j]) for j in range(len(sequence))):
#             first_occurrence.append(current_sequence)
#     return first_occurrence



# def find_sequence_occurrences(self,)-> list[int,int,str]:
#     ''' will find all '''
#     sequence = [int, int, str]
#     stack = [10, 6, 9, 3, '+', -11, '*', '/', '*', 17, '+', 5, '+']

#     occurrences = []

#     for i in range(len(stack) - len(sequence) + 1):
#         current_sequence = stack[i:i + len(sequence)]

#         if all(isinstance(current_sequence[j], sequence[j]) for j in range(len(sequence))):
#             occurrences.append(current_sequence)
#     return occurrences

# operators = ['+','-','/','*',]


# I want you to remake this, but apply the logic: 

# x=None
# every time when a nested-list is found, i want you to set x equal to that list, then replace that nested-list with x.
# once x has been found, the iteration will restart at i=0 and the stack should look like this [10, 6, int(x), -11, '*', '/', '*', 17, '+', 5, '+'] where x = [9, 3, '+'], 
# then you will then repeat the previous steps and proceed to look for the next sequence of [int, int, str]. 
# the formula will continue to run untill it can no longer apply this logic and can not find any more [int int str] sequences. 

def find_and_group_sequence(sequence, stack, operators):
    i = 0
    x = None
    found_all_sequences = False
    while True:
        found_sequence = False

        while i < len(stack):
            current_item = stack[i]

            if isinstance(current_item, list):
                x = current_item
                stack[i] = x
                found_sequence = True
                break
            elif i <= len(stack) - len(sequence) + 1 and all(isinstance(stack[i + j], sequence[j]) for j in range(len(sequence))):
                # Found a sequence match
                sub_list = stack[i:i + len(sequence)]
                stack[i:i + len(sequence)] = [sub_list]
                found_sequence = True
                break
            else:
                print(stack)
                found_all_sequences = True
        

        if found_all_sequences:
            break
        else:
            i = 0

# Example usage
operators = ['+', '-', '/', '*']
sequence = [int, int, str]
stack = [10, 6, 9, 3, '+', -11, '*', '/', '*', 17, '+', 5, '+']

find_and_group_sequence(sequence, stack, operators)

print(stack)
