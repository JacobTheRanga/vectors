from math import sin, cos, tan, sqrt
from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

pythag = lambda b, c: sqrt(abs(c**2 - b**2))
rounded = lambda vector: [round(i, environ.get('ROUNDING')) for i in vector]

def calc(inputs, axes):
    for plane in inputs:
        if len((length:=list(plane['Length'].keys()))) == 2 and\
        plane['rightAngle'][0::2] in length:
            return pythag(length[0], length[1])  

def main():
    inputs = [
            {
                **{
                    inputType: 
                        {
                            input(f'{inputType} Points on Plane {plane+1}: ').upper(): 
                                float(input(f'{inputType} {i+1} on Plane {plane+1} Value: ')) 
                        for i in range(int(input(f'No. {inputType} in Plane {plane+1}: ')))
                        }
                for inputType in ['Angle', 'Length']
                },
                'rightAngle':
                    input(f'Right Angle points on Plane {plane+1}: ').upper()
            }
        for plane in range(int(input('No. Planes: ')))
        ]
    axes = [
                input(f'Points marking Axis[{i}]: ') 
            for i in range(int(input('No. Dimensions: ')))
            ]
    print(rounded(calc(inputs, axes)))
    
if __name__ == '__main__':
    main()