import timeit

class Solution1:
    def __init__(self):
        self.stack = []

    def push_method1(self, val):
        return self.stack.append(val)

class Solution2:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity
        self.size = 0
        self.capacity = capacity
        self.head = 0  # Points to the next available position

    def push_method_custom(self, val):
        if self.size == self.capacity:
            # If the stack is full, double its capacity (circular buffer)
            self.capacity *= 2
            new_stack = [None] * self.capacity

            # Copy elements to the new stack
            for i in range(self.size):
                new_stack[i] = self.stack[(self.head + i) % self.size]

            self.stack = new_stack
            self.head = 0

        self.stack[(self.head + self.size) % self.capacity] = val
        self.size += 1

# Test the performance
solution1 = Solution1()
solution2 = Solution2()

time_method1 = timeit.timeit(lambda: solution1.push_method1(42), number=1000000)
time_method2 = timeit.timeit(lambda: solution2.push_method_custom(42), number=1000000)

print("Time taken by push_method1:", time_method1)
print("Time taken by push_method_custom:", time_method2)
