"""
Convert between vector types

There are two sub-scripts within
this script

    -   unitCalc
    -   changeMagnitude

Input Format: [vx, vy, ...]
"""

from math import sqrt

unitCalc = lambda vector: [i/sqrt(sum([x**2 for x in vector])) for i in vector]
changeMagnitude = lambda inputs: [i*inputs[1] for i in unitCalc(inputs[0])]

def inputs():
    vector = [float(input(f'Vector [{i}]: ')) for i in range(int(input('Vector Dimensions: ')))]
    if input('Unit vector or change magnitude: ') == 'unit':
        return unitCalc(vector)
    return changeMagnitude([vector, float(input('Magnitude: '))])