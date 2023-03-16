from math import sqrt

unitCalc = lambda vector: [i/sqrt(sum([x**2 for x in vector])) for i in vector]
changeMagnitude = lambda vector, magnitude: [i*magnitude for i in unitCalc(vector)]

def inputs():
    vector = [float(input(f'Vector [{i}]: ')) for i in range(int(input('Vector Dimensions: ')))]
    if input('Unit vector or change magnitude: ') == 'unit':
        return unitCalc(vector)
    return changeMagnitude(vector)