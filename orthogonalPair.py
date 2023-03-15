from dotenv import load_dotenv
from os import environ
from dotProduct import calc

load_dotenv('.env')

rounded = lambda vectors: [[[round(c, environ.get('ROUNDING')) for c in i ]for i in a] for a in vectors]
pairs = lambda vectors: [
                            [vectors[i], vectors[a]]
                        for i in range(len(vectors))
                        for a in range(len(vectors))
                        if calc([vectors[i], vectors[a]]) == 90
                        if a != i
                        ]

def main():
    dimensions = int(input('No. of dimensions: '))
    inputs = [
                [
                    float(input(f'Vector {i+1}[{dimension}]: '))
                for dimension in range(dimensions)
                ]
            for i in range(int(input('No. of vectors: ')))
            ]
    for i in rounded(pairs(inputs)):
        print(i)

if __name__ == '__main__':
    main()
    