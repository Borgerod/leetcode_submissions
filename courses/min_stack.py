class MinStack:
    '''
    I refuse to submit a copy paste answer from chatgpt like 80% of the other partisipants. 
    '''

    def __init__(self):
        self.stack = []
        

    def top(self) -> int:
        return self.stack[-1]
        

    def push(self, val: int) -> None:
        return self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        i, min_ = 0, 0
        while i > -(len(self.stack)):
            i -= 1
            if self.stack[i] < min_ or i == -1: min_ = self.stack[i]
        return min_        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        


if __name__ == '__main__':
    for statements, vals in [
        [
            ["MinStack","push","push","push","getMin","pop","top","getMin"],
            [[],[-2],[0],[-3],[],[],[],[]],
        ],
    ]:  
        param_counter = 0
        for statement, val in zip(statements, vals):
            if statement == "MinStack":
                if not val:
                    obj = eval(f"{statement}()")
                else:
                    obj = eval(f"{statement}({val[0]})")

            elif statement in ["getMin","top"]: 
                    param_counter += 1
                    exec("_".join(["param", str(param_counter)])+f" = obj.{statement}()")        
            else:
                action="obj."
                if not val:
                    eval(f"obj.{statement}()")
                elif len(val)>1:
                    eval(f"obj.{statement}({val})")
                else:
                    eval(f"obj.{statement}(({val[0]}))")
  