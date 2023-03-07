from math import acos, sqrt, degrees

def main():
    vectors = []
    dimensions = int(input('How many dimensions to the vectors: '))
    for vectorNum in range(2):
        vector = []
        for dimentionNum in range(dimensions):
            vector.append(float(input(f'Vector {vectorNum+1} [{dimentionNum}]: ')))
        vectors.append(vector)
    multiModulus = 1
    for i in range(2):
        modulus = 0
        for a in range(dimensions):
            modulus += vectors[i][a]**2
        multiModulus *= sqrt(modulus)
    sumVector = 0
    for i in range(dimensions):
        timesVector = 1
        for a in range(2):
            timesVector *= vectors[a][i]
        sumVector += timesVector
    result = acos(sumVector/multiModulus)
    return print(round(degrees(result), 4), 'degrees')

if __name__ == '__main__':
    main()