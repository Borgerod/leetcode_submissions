


class Solution:
    ''' 
    my answer, based on "Python3 || Simple Intution using Stack"
    '''
    def evalRPN(self, tokens: list[str]) -> int:
        st=[]
        for i in tokens:
            if i=="+":
                a,b=st.pop(),st.pop()
                st.append(b+a)
            elif i=="-":
                a,b=st.pop(),st.pop()
                st.append(b-a)
            elif i=="*":
                a,b=st.pop(),st.pop()
                st.append(b*a)
            elif i=="/":
                a,b=st.pop(),st.pop()
                st.append(int(b/a))
            else:
                st.append(int(i))
        return st[0]


class Solution:
    ''' 
    my answer, based on "Python3 || Simple Intution using Stack"
    '''
    def evalRPN(self, tokens: list[str]) -> int:
        st=[]
        special = ["+", "-", "*", "/"]
        index = 0
        for i in tokens:
            index+=1
            if i in special:

                a,b=st.pop(),st.pop()
                print(a,i,b)
                print(type(a),type(i),type(b))
                st.append(str(int(eval("".join([b, i, a])))))
                print(f"[{index}]: {b}{i}{a}={st}")
            else:
                st.append(i)
                print(f"[{index}]: {i}=>{st[:-1]}={st}")
        return int(st[0])


def main():
    test_cases = [
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ]
    s,i = Solution(), 0
    for tokens in test_cases:
        i+=1
        res = s.evalRPN(tokens)
        print(f" case {i}: {res} ")

if __name__ == '__main__':
    main()