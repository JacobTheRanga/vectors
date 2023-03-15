from math import sin, cos, tan, sqrt
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

pythag = lambda b, c: sqrt(abs(c**2 - b**2))
rounded = lambda vector: [round(i, environ.get('ROUNDING')) for i in vector]

vector = lambda inputs: [
                            axis
                        if axis in inputs[1]
                        else
                            [
                                {
                                    known:
                                        inputs[1][known]
                                for point in list(axis)
                                for known in list(inputs[1].keys())
                                if len(known) == i
                                if point in list(known)
                                }
                            for i in [2, 3]
                            ]
                        for axis in inputs[2]
                        ]

def main():
    inputs = [
                [
                    input(f'Right angle in plane [{plane+1}]: ').upper()
                for plane in range(int(input('No. of planes: ')))
                ],
                {
                    input(f'Known Points [{numKnown+1}]: ').upper():
                        float(input(f'Known Value [{numKnown+1}]: '))
                for numKnown in range(int(input('No. of known values: ')))
                },
                [
                    input(f'Points marking Axis[{i}]: ').upper()
                for i in range(int(input('No. Dimensions: ')))
                ]
            ]
    print(vector(inputs))
    
if __name__ == '__main__':
    main()