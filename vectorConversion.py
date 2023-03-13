from math import sqrt
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

modulus = lambda vector: sqrt(sum([x**2 for x in vector]))
unitCalc = lambda vector: [i/modulus(vector) for i in vector]
changeMagnitude = lambda vector, magnitude: [i*magnitude for i in unitCalc(vector)]
rounded = lambda vector: [round(i, int(environ.get('ROUNDING'))) for i in vector]

def main():
    vector = [float(input(f'Vector [{i}]: ')) for i in range(int(input('Vector Dimensions: ')))]
    if input('Unit vector or change magnitude: ') == 'unit':
        return print(rounded(unitCalc(vector)))
    return print(rounded(changeMagnitude(vector)))

if __name__ == '__main__':
    main()