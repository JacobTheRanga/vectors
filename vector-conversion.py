from math import sqrt

def unitVector(vector, dimensions):
    modulus = 0
    for i in range(dimensions):
        modulus += vector[i]**2
    modulus = sqrt(modulus)
    for i in range(dimensions):
        vector[i] = round(vector[i]/modulus, 4)
    return print('Unit Vector: ', vector)

def positionVector(vector, magnitude, dimensions):
    for i in range(dimensions):
        vector[i] = round(vector[i]*magnitude, 4)
    return print('Position Vector: ', vector)

def main():
    vectorType = input('Current Vector Type: ')
    dimensions = int(input('How many dimensions to the vector: '))
    vectorIn = []
    for i in range(dimensions):
        vectorIn.append(float(input(f'Vector [{i}]: ')))
    if vectorType.split()[0] != 'unit':
        return unitVector(vectorIn, dimensions)
    magnitude = float(input('What is the magnitude: '))
    return positionVector(vectorIn, magnitude, dimensions)

if __name__ == '__main__':
    main()