# from math import sin, cos, tan, sqrt

# knowns = lambda plane, axis, inputs, length: [
#                                                 known
#                                             for axisPoint in list(axis)
#                                             for known in list(inputs[1].keys())
#                                             if axisPoint in list(known)
#                                             if len(known) == len([i for i in list(known) if i in list(plane)])
#                                             if len(known) == length
#                                             ]
# vector = lambda inputs: [
#                             inputs[1][axis]
#                         if axis in inputs[1]
#                         else 
#                             sqrt(sum([i**2 for i in ]))
#                         if 
#                             [
#                                 sqrt(sum(map(lambda x: x**2, knownAxisPlane[0])))
#                             if len(knownAxisPlane[0]) == 2
#                             else 

#                             for knownAxisPlane in
#                                 [
#                                     [[
#                                         i
#                                     for i in knowns(plane, axis, inputs, 2)
#                                     ],
#                                     [
#                                         i
#                                     for i in knowns(plane, axis, inputs, 3)
#                                     ]]
#                                 for plane in inputs[0]
#                                 ]
#                             for plane in inputs[0]
#                             ]
#                         for axis in inputs[2]
#                         ]

# def inputs():
#     inputs = [
#                 [
#                     input(f'Right angle in plane [{plane+1}]: ').upper()
#                 for plane in range(int(input('No. of planes: ')))
#                 ],
#                 {
#                     input(f'Known Points [{numKnown+1}]: ').upper():
#                         float(input(f'Known Value [{numKnown+1}]: '))
#                 for numKnown in range(int(input('No. of known values: ')))
#                 },
#                 [
#                     input(f'Points marking Axis[{i}]: ').upper()
#                 for i in range(int(input('No. Dimensions: ')))
#                 ]
#             ]
#     return vector(inputs)