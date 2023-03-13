from math import acos, sqrt, degrees
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

def main():
    squared = lambda x: sum([i**2 for i in x])
    calc = lambda vectors: acos(sum(
                                    [vectors[0][i]*vectors[1][i] 
                                    for i in range(len(vectors[0]))]
                                    )
                                /sqrt(
                                    squared(vectors[0])*squared(vectors[1])
                                    )
                                )
    dimensions = int(input('How many dimensions to the vectors: '))
    vectors = [[float(input(f'Vector {vector+1} [{dimension}]: ')) 
                for dimension in range(dimensions)] 
                for vector in range(2)]
    result = round(degrees(calc(vectors)), int(environ.get('ROUNDING')))
    return print(f'{result}{chr(176)}')

if __name__ == '__main__':
    main()