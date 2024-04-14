
'''
example: 
    browser activity in regards to "go back" and "go forward" buttons
'''
backward_history = [1,2,3]
forward_history = []

browsing_session = []
browsing_forward_session = []
# how to add:
print("before addition")
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)


#how to remove:
browsing_session.pop()
print("after removal")
print(browsing_session)


class Browsing_history: #Stack
    def __init__(self):
        self._browsing_session = []
        self._forward_session = []

    def append(self, val):
        self._browsing_session.append(val)
        return self._browsing_session
    
    @property
    def pop(self):
        self._forward_session.append(self.peek())
        self._browsing_session = self._browsing_session[:-1]
        return self._browsing_session
    
    @property
    def peek(self):
        if self._browsing_session:
            return self._browsing_session[-1]
        else:
            return None
    
    @property
    def peek_forward(self):
        if self._forward_session:
            return self._forward_session[-1]
        else:
            return None

    @property
    def get_forward_session(self):
        return self._forward_session


# browsing_session = Browsing_history()
# browsing_session.append(4)
# browsing_session.append(1)
# browsing_session.append(2)

# print(browsing_session.peek())
# print(browsing_session.pop())
# print(browsing_session.get_forward_session())
# print(browsing_session.peek_forward)