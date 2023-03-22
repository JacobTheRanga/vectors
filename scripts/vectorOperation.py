"""
Custom Vector Operation Calculator

This script allows the user to use any operation
"""

calc = lambda inputs: [
                            eval(inputs[1].join(
                                [
                                    str(inputs[0][num][i])
                                for num in range(len(inputs[0]))
                                ]
                            ))
                        for i in range(len(inputs[0][0]))
                        ]

def inputs():
    inputs = [
                [[
                    input(f'Vector {num+1}[{i}]: ')
                for i in range(int(input('No. Dimensions: ')))
                ]
            for num in range(int(input('No. Vectors: ')))],
            input('Operator: ')
            ]
    return calc([inputs])