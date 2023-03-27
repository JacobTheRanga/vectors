"""
Custom Vector Operation Calculator

This script allows the user to use any
mathematical operator to combine multiple
vectors

Input Format: [[[v1x, v1y, ...], [v2x, v2y, ...], ...], 'operator']
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
    dimensions = int(input('No. Dimensions: '))
    inputs = [
                [[
                    float(input(f'Vector {num+1}[{i}]: '))
                for i in range(dimensions)
                ]
            for num in range(int(input('No. Vectors: ')))],
            input('Operator: ')
            ]
    return calc(inputs)