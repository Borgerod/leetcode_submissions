import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class FactorialCalculator:
    def __init__(self, x):
        self.x = x
        self.bases = self.generate_bases()
        self.factorials = self.calculate_factorials()

    def calculate_factorials(self):
        factorials = []
        factorial = 1
        for i in range(1, self.x + 1):
            factorial *= i
            factorials.append(factorial)
        return factorials
    def generate_bases(self):
        return list(range(1,self.x+1))
    
    def get_factorials(self):
        return self.factorials

class IntegerGraphCreator:
    def __init__(self, x, y):
        self.x = x #bases
        self.y = y #factorials
        # self.graph = self.create_graph()

    def create_graph(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y)

        ax.set(xlabel='base value', ylabel='factorial value',
            title=f'Factorials from range ({self.x[0]}!, {self.x[-1]}!)')
        ax.grid()

        fig.savefig("test.png")
        plt.show()


class PolynomialFormulaGenerator:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values
        self.coefficients = self.fit_polynomial()

    def fit_polynomial(self):
        # Fit a polynomial to the data
        return np.polyfit(self.x_values, self.y_values, len(self.x_values) - 1)

    def get_formula(self):
        # Create a string representation of the polynomial formula
        formula = 'f(x) = '
        for i in range(len(self.coefficients)):
            term = f'{self.coefficients[i]:.2f}'  # Format the coefficient
            if i < len(self.coefficients) - 1:
                term += f'x^{len(self.coefficients) - i - 1}'
                if self.coefficients[i + 1] >= 0:
                    term += ' + '
                else:
                    term += ' - '
            formula += term

        return formula



def main():
    '''
        descr
    '''
    x = 100 #20!
    fc = FactorialCalculator(x)
   

    graph_creator = IntegerGraphCreator(fc.bases, fc.factorials)
    graph_creator.create_graph()
    print(fc.bases, fc.factorials)


    formula_generator = PolynomialFormulaGenerator(fc.bases, fc.factorials)
    formula = formula_generator.get_formula()
    print(formula)


if __name__ == '__main__':
    main()


'''
f(x) = 0.55x^19 - -72.87x^18 + 4061.45x^17 - -116227.64x^16 + 1405576.51x^15 + 13691865.80x^14 - -715089866.59x^13 + 6696121503.40x^12 + 142799116064.97x^11 - -5569455492774.29x^10 + 93492306067042.94x^9 - -1010187061764246.12x^8 + 7682856979062092.00x^7 - -42284280194452120.00x^6 + 168739794116433600.00x^5 - -480570532862950848.00x^4 + 943323559679947136.00x^3 - -1197647236185415680.00x^2 + 870694559645354496.00x^1 - -269016617961390656.00
f(x) = -269016617961390656.00 + 870694559645354496.00x - 1197647236185415680.00x^2 + 943323559679947136.00x^3 - 480570532862950848.00x^4 + 168739794116433600.00x^5 - 42284280194452120.00x^6 + 7682856979062092.00x^7 - 1010187061764246.12x^8 + 93492306067042.94x^9 - 5569455492774.29x^10 + 142799116064.97x^11 + 6696121503.40x^12 - 715089866.59x^13 + 13691865.80x^14 + 1405576.51x^15 - 116227.64x^16 + 4061.45x^17 - 72.87x^18 + 0.55x^19
f(x) ≈ 0.55x^19 - 72.87x^18 + 4061.45x^17 - 116227.64x^16 + 1405576.51x^15 + 1.36918658e7x^14 - 7.15089867e8x^13 + 6.69612150e9x^12 + 1.42799116e11x^11 - 5.56945549e12x^10 + 9.34923061e13x^9 - 1.01018706e15x^8 + 7.68285700e15x^7 - 4.22842802e16x^6 + 1.68739794e17x^5 - 4.80570533e17x^4 + 9.43323560e17x^3 - 1.19764724e18x^2 + 8.70694560e17x - 2.69016618e17

'''