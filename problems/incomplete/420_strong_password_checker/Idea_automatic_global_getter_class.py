class FactorialCalculator:
    def __init__(self, x):
        self.x = x
        self.factorials = self.calculate_factorials()
        self.yourmother = ["gay", "fat"]

    def calculate_factorials(self):
        factorials = []
        factorial = 1
        for i in range(1, self.x + 1):
            factorial *= i
            factorials.append(factorial)
        return factorials

    def get_factorials(self):
        return self.factorials

class Factorials:
    def __init__(self, x):
        self.x = x
        self.factorials = self.calculate_factorials()
        self.yourmother = ["gay", "fat"]

    def __init__(self) -> None:
        self.get = self.calculate_factorials()

    def calculate_factorials(self):
        return "I am factorial, beep boop" 

class Getter():
    ''' The getter file will work as a local search engine for you project. 
    The getter will be able to call any unique methods and variables from any class in the file '''

    def __init__(self) -> None:
        # THE IDEA:
        # The getter will upon initialization check the file for any classes then;
        # generate a function that initializes them and makes getter the parent of them.  
        # TODO [ ]: make function that automaticly inherits from and initiates all other classes in this file
        # NOTE: Which also means that it will automaticlly handle any new classes.
        self.function_that_auto_handles_other_classes()
    
    def function_that_auto_handles_other_classes(self):
        pass

class Totally_Not_Telated_To_FactorialCalculator:
    def __init__(self, y) -> None:
        self.y = y
        self.z = self.calculate_z()

    def calculate_z(self,):
        ''' instead if initializing Factorials or calling it inside another class, You will simply use the getter class instead.
            that way it is easier, no brain workflow. Just make sure that all variable names are unique. 
            If you have multiple files you could also import the getterfile from other files and make this getter inherit it. 
            Note that you will only need to import the getter file.
        '''
        return self.y*GET.x
    
    def Graph_of_XY(self):
        return "I am Graph, fear me!" 


if __name__ == '__main__':
    GET=Getter()
    GET.x
    GET.Graph_of_XY()