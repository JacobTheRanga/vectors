from math import acos, sqrt, degrees

def main():
    vectors = []
    numToDimention = ['x','y','z']
    dimentions = int(input('How many dimentions to the vectors: '))
    quantity = int(input('How many vectors: '))
    for vectorNum in range(quantity):
        vector = []
        for dimentionNum in range(dimentions):
            vector.append(float(input(f'Vector {vectorNum+1} [{numToDimention[dimentionNum]}]: ')))
        vectors.append(vector)
    multiModulus = 1
    for i in vectors:
        modulus = 0
        for a in i:
            modulus += a**2
        multiModulus *= sqrt(modulus)
    sumVector = 0
    for i in range(dimentions):
        timesVector = 1
        for a in range(quantity):
            timesVector *= vectors[a][i]
        sumVector += timesVector
    result = acos(sumVector/modulus)
    return print(round(degrees(result), 4), 'degrees')

if __name__ == '__main__':
    main()