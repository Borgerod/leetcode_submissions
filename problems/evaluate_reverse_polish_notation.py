class Solution:

    @property
    def description(self) -> None:
        ''' Problem explaination: 
            you are given a string of math-related chars, (integers: range(-200, 200) and special_chars: ["+", "-", "*", "/"])
            your job is to combine those into a valid math equation, then return the answer.
           
           Example 1:

                Input: tokens = ["2","1","+","3","*"]
                Output: 9
                Explanation: ((2 + 1) * 3) = 9 
        
        
            Rules:
            - divition: allways round up towards zero.  (round up to whole numbers)
            - no divition by zero 
            - will not begin with speacial (-1+1=0) and will contain double operator (1-(-1)=2)

        simply put: describe the math notation from here (https://en.wikipedia.org/wiki/Reverse_Polish_notation) into code.  
        ''' 

        
        ''' 
        it will work in pairs, then trios.
                    1    numbers will be paired, starting at the end of the list
                    2    then numbers and expresssion wil be trebled,(numbers paired with the closest expresion)
                    3    lets call the first treble as "x" for simplisity
                    *    then repeat the previous steps untill all numbers and expressions has been trebled. 
                    4    translate to conventional math notation (1+1=2)
                    5    solve the ecuation and return result. 
        2 1 10 / + ==>  2 [1 10] / +  ==> 2 ([1 10] /) + ==> 2 x + ==> ([2 x] - ) ==> ([2 ([1 10] /)] - ) ==> (2-(1/10))
        '''
  
        
    def evalRPN(self, tokens: list[str]) -> int:
        operator = ["+", "-", "*", "/"]
        sum = 0 
        res = 0 
        int_pair = []
        expression=""
        # x_list = []
        print(tokens, "\n")
        i=0
        stack=[]
        while i < len(tokens):
            print(f"i: {i} tokens: {tokens} stack: {stack}")
            

            # if stack and 



            if i+2 <= len(tokens):
                # print(tokens[i+2])
                # print(f"{i+2} <= {len(tokens)}")
                # if tokens[i+2] not in operator:
                # # will skip intill it finds a suitable match for criteria (int int operator)
                #     print(f"{tokens[i+2]} is NOT an operator")
                #     stack.append(tokens[i])
                #     tokens.pop(i)
                #     i = -1
                # else:
                if tokens[i+2] not in operator:
                # will skip intill it finds a suitable match for criteria (int int operator)
                    print(f"{tokens[i+2]} is NOT an operator, moving tokens[i]:{tokens[i]} to stack")
                    stack.append(tokens[i])
                    tokens.pop(i)
                    i = -1
                else:

                    int_pair.append(tokens[i])
                    # int_pair=[i,i+1]
                    if tokens[i+2] == "/":
                        expression = f"int({tokens[i]}{tokens[i+2]}{tokens[i+1]})"
                    else:
                        expression = f"({tokens[i]}{tokens[i+2]}{tokens[i+1]})"
                    int_pair.append(expression)
                    print(tokens)
                    tokens.pop(0),tokens.pop(0),tokens.pop(0)
                    
                    
                    
                    if stack:
                        tokens.insert(0,stack[-1])
                        stack.pop()
                    print(expression, tokens, stack)
                    
                        # i -=1
                    # else:

                    # print(expression)
                    # print("int_pair: ",int_pair)


            

                    # if tokens[i] not in operator:
                    #     int_pair.append(tokens[i])
                    #     print(int_pair)
                    print("NEXT STEP")
                    if len(tokens)==2:
                        print(f"len tokens = {len(tokens)}")
                        if tokens[-1] in operator:
                            print("FINAL EXPRESSION:",f"({tokens[0]}{tokens[1]}{expression})")
                            return eval(f"({tokens[0]}{tokens[1]}{expression})")
                            

                            if tokens:
                                print("TRUE, ", tokens)
                        else:
                            print(f"ERROR; {tokens}")


                    elif len(tokens)==1:
                        print(f"len tokens = {len(tokens)}")
                        print("ERROR, something weird happends:")
                        print(expression, tokens, stack)

                    if len(tokens)==0:
                        print(True)
                        print(f"len tokens = {len(tokens)}")
                        #ready to return
                        print("FINAL", expression, tokens, stack)
                        return eval(expression)


                    # if tokens[i] in operator and len(int_pair)==2:
                    #     res = eval(f"{int_pair[0]}{tokens[i]}{int_pair[1]}")
                    #     expression = f"({int_pair[0]}{i}{int_pair[1]})"
                    #     print(expression)
                    #     int_pair.clear()

                    # elif tokens[i] in operator and len(int_pair)==1:
                    #     int_pair.append(res)
                    #     res = eval(f"{int_pair[0]}{tokens[i]}{int_pair[1]}")
                    #     expression = f"({int_pair[0]}{i}{int_pair[1]})"
                    #     print(expression)
                    #     sum += res

                    #     int_pair.clear()
            # else:
            #     i+=1
            print("current expression: ", expression)
            i+=1
            # print()
            
            # else:
                # stack.append(i)
                # i+=1
            # i+=1
        # print(stack)

        # for i in tokens:
        #     if i not in operator:
        #         int_pair.append(i)
                
        #     elif i in operator and len(int_pair)==2:
        #         res = eval(f"{int_pair[0]}{i}{int_pair[1]}")
        #         expression = f"({int_pair[0]}{i}{int_pair[1]})"
        #         print(expression)
        #         # x_list.append((expression))
        #         int_pair.clear()
            
        #     elif i in operator and len(int_pair)==1:
                
                
        #         int_pair.append(res)
                
        #         res = eval(f"{int_pair[0]}{i}{int_pair[1]}")
        #         expression = f"{expression}{i}{int_pair[1]}"
        #         print(expression)
        #         sum += res
        #         int_pair.clear()
        #     else:
        #         continue

        #     print(int_pair)
        #     print(res)
        #     print(sum)

            

        return sum


# class Stack:
#     def __init__(self):
#         self.polish_notation = self.items = []
#         self.conventional = []
#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("pop from an empty stack")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("peek from an empty stack")

#     def size(self):
#         return len(self.items)





'''# x=[x 3 *]
# x= ((2+1)*3)
x=int((1+2)*3)
# y=[4 x + ]
y= int(4+(13/5))
# y=((13/5)+4)
# z=[10 6 9 3 + -11 * / * 17 + 5 +]
# z=[x 17 + 5 +]
z=(((int(6/((9+3)*(-11)))*10)+17)+5)
# z = int((((((9+3)*(-11))/6)*10)+17)+5)
print("x: ", x)
print("y: ", y)
print("z: ", z)'''

if __name__ == '__main__':
    #? for custom samples
    # from input_generator import Generator
    # sample = Generator(int).list("small")

    for i, case in enumerate([
        # ["2","1","+","3","*"],
        # ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ]): 
        print(
       f"Result case_{i}: {Solution().evalRPN(case)}"
    )
        # Solution().evalRPN(case)
    # print(sample)




