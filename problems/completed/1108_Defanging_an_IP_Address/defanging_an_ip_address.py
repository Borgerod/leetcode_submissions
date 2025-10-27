class Solution:
    '''
    "defanged IP address" - replace every "." with "[.]".
    '''
    def defangIPaddr(self, address: str) -> str:
        
        '''
        1.0) while loop. one copy - in-place not possible (maybe if you convert it to something else like bytearray )
        '''
        i = 0
        address = list(address)
        while i < len(address):
            if address[i] == ".": address[i] = "[.]"
            i += 1
        return "".join(address)
    
    def defangIPaddr(self, address: str) -> str:      
        '''
        2.0) simplest method
        '''
        return address.replace(".", "[.]")
        
    def defangIPaddr(self, address: str) -> str:      
        '''
        3.0) attempt at a in-place (round-about way)
        '''
        return "".join(["[.]" if i == "." else i for i in list(address)])
        
        




    

if __name__ == '__main__':


    cases = [
        "1.1.1.1",
        "255.100.50.0",
        "0.0.0.0",
        "255.255.255.255",
        "255.0.0.255",
        "0.255.255.0",
        "255.255.0.255",
        "1.255.254.253",
    ]


    #> OPTION 1 (for single inputs)
    s = Solution()
    for i, address in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {s.defangIPaddr(address)}\n")




''' LEETCODE:
    
    "1.1.1.1"
    "255.100.50.0"
    "0.0.0.0"
    "255.255.255.255"
    "255.0.0.255"
    "0.255.255.0"
    "255.255.0.255"
    "1.255.254.253"

'''
