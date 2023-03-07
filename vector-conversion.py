from math import sqrt

def unitVector(vector, dimensions):
    modulus = 0
    for i in range(dimensions):
        modulus += vector[i]**2
    modulus = sqrt(modulus)
    for i in range(dimensions):
        vector[i] = round(vector[i]/modulus, 4)
    print('Unit Vector: ', vector)
    txt = input('Convert to position?[Y/N] ')
    if txt.lower() == 'y':
        magnitude = float(input('Magnitude: '))
        return positionVector(vector, magnitude, dimensions)

def positionVector(vector, magnitude, dimensions):
    for i in range(dimensions):
        vector[i] = round(vector[i]*magnitude, 4)
    return print('Position Vector: ', vector)

def main():
    vectorType = input('Current Vector Type: ')
    dimensions = int(input('Vector Dimensions: '))
    vectorIn = []
    for i in range(dimensions):
        vectorIn.append(float(input(f'Vector [{i}]: ')))
    if vectorType.split()[0] != 'unit':
        return unitVector(vectorIn, dimensions)
    magnitude = float(input('Magnitude: '))
    return positionVector(vectorIn, magnitude, dimensions)

if __name__ == '__main__':
    main()