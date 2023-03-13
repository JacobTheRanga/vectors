from math import sin, cos, tan, sqrt

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
                **{
                    'rightAngle':
                        input(f'Right Angle points on Plane {plane+1}: ').upper()
                }
            }
        for plane in range(int(input('No. Planes: ')))
        ]

if __name__ == '__main__':
    main()