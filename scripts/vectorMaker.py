from math import sin, cos, tan, sqrt

vector = lambda inputs: [
                            inputs[1][axis]
                        if axis in inputs[1]
                        else 
                            [
                                [
                                    [
                                        known
                                    for known in [1]
                                    if (plane[0::2] or plane[:-1] or plane[1:]) in (axis or axis[1]+axis[0])
                                    if len(known) == types
                                    
                                    ]
                                for types in [2,3]
                                ]
                            for plane in inputs[0]
                            ]
                        for axis in inputs[2]
                        ]

def inputs():
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
    return vector(inputs)