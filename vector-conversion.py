from math import *

def unitVector(vector, dimensions):
    modulus = 1
    for i in dimensions:
        modulus *= vector[i]**2
    modulus = sqrt(modulus)


def positionVector(vector, dimensions):
    

def main():
    vectorType = input('Vector Type: ')
    dimensions = int(input('How many dimensions to the vector: '))
    vectorIn = []
    numToDimensions = ['x','y','z']
    for i in range(dimensions):
        vectorIn.append(float(input(f'Vector [{numToDimensions[i]}]')))
    if vectorType != 'unit':
        return unitVector(vectorIn, dimensions)
    return positionVector(vectorIn, dimensions)

if __name__ == '__main__':
    main()