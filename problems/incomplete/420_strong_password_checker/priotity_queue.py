
class Solution:
        
    def insert(self, d):
        self.q.append(d)

    def delete(self):
        try:
            m = 0
            for i in range(len(self.q)):
                if self.q[i] > self.q[m]:
                    m = i
            item = self.q[m]
            del self.q[m]
            return item
        except IndexError:
            print("Queue empty.")
            exit()

    def is_empty(self):
        return len(self.q) == 0
    
    def getPriorityQueue(self, inputs:list[int]):
        self.q = []
        for i in inputs:
            self.insert(i)
            print(f"current quueue: {self.q}")

        
        print(f"\nfinal queue: {self.q}")
        print("Removed elements:")
        
        while not self.is_empty():
            print(self.delete())

        return
if __name__ == '__main__':
    inputs= [12,1,14,7]
    s = Solution()
    s.getPriorityQueue(inputs)

