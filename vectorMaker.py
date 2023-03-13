from math import sin, cos, tan, sqrt
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

pythag = lambda b, c: sqrt(abs(c**2 - b**2))
rounded = lambda vector: [round(i, environ.get('ROUNDING')) for i in vector]
checkKnown = lambda inputs, plane: [
                                        known
                                    for known in list(inputs[1].keys()) 
                                    if known or 
                                    (known[1]+known[0]) or 
                                    (known[2]+known[1]+known[0]) in
                                    [
                                        plane[0::2], plane[1:], plane[:2], 
                                        (plane[1:]+plane[0]), (plane[2]+plane[:2])
                                    ]
                                ]
knowns = lambda inputs: [
                            [
                                [   
                                    known
                                for known in checkKnown(inputs, plane)
                                if len(known) == 2
                                ],
                                [
                                    known
                                for known in checkKnown(inputs, plane)
                                if len(known) == 3
                                ]
                            ]
                        for plane in inputs[0]
                        ]

def calc(inputs):
    print(knowns(inputs))

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
    print(rounded(calc(inputs)))
    
if __name__ == '__main__':
    main()