"""
Calculate cross product of two vectors

Input Format: [[v1x, v1y, v1z], [v2x, v2y, v2z]]
"""

calc = lambda vectors: [vectors[0][1]*vectors[1][2] - vectors[0][2]*vectors[1][1],
                        vectors[0][2]*vectors[1][0] - vectors[0][0]*vectors[1][2],
                        vectors[0][0]*vectors[1][1] - vectors[0][1]*vectors[1][0]
                        ]

def inputs():
    inputs = [
                [
                    float(input(f'Vector {num+1}[{i}]: ')) 
                for i in range(3)
                ] 
            for num in range(2)
            ]
    return calc(inputs)