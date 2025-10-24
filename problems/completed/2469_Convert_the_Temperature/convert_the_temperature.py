class Solution:
    '''
        Temperature converter - Convert 'Celsius' to ['Kelvin', 'Fahrenheit'].
            error_margin: 10^-5 |  1e-5
    '''
    def convertTemperature(self, celsius: float) -> list[float]:
        ''' 1.0) The simplest, quickest i can think of
            :param celsius: Temperature in Celsius
            :return: [Kelvin, Fahrenheit]
        '''
        c = celsius             #celsius
        k = c + 273.15          #kelvin
        f = c * 1.80 + 32.00    #fahrenheit
        return [k, f]           #ans[kelvin, fahrenheit]



    def convertTemperature(self, celsius: float) -> list[float]:
        ''' 1.1) cleaned
            :param celsius: Temperature in Celsius
            :return: [Kelvin, Fahrenheit]
        '''
        return [celsius + 273.15, celsius * 1.80 + 32.00]

if __name__ == '__main__':

    cases = [
        36.5,
        122.11,
        0.0,
        1000.0,
        273.15,
        32.0,
        999.99,
        0.01,
    ]

    #> OPTION 1 (for single inputs)
    s = Solution()
    for i, celsius in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {s.convertTemperature(celsius)}\n")


''' #> ___ generated cases _______________________________

cases = [
    36.5,
    122.11,
    0.0,
    1000.0,
    273.15,
    32.0,
    999.99,
    0.01,
]

36.5
122.11
0.0
1000.0
273.15
32.0
999.99
0.01

'''