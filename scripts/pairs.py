"""
Calculate pairs of vectors which are either
parallel or orthogonal

Input Format: [[v1x, v1y, v1z], [v2x, v2y, v2z], ...]
"""

from scripts import dotProduct

parallel = lambda vectors: pairs(vectors, 180)
orthogonal = lambda vectors: pairs(vectors, 90)

pairs = lambda vectors, num: [
                            [vectors[i], vectors[a]]
                        for i in range(len(vectors))
                        for a in range(len(vectors))
                        if dotProduct.calc([vectors[i], vectors[a]]) == num and
                        a > i
                        ]

def inputs():
    dimensions = int(input('No. of dimensions: '))
    inputs = [
                [
                    float(input(f'Vector {i+1}[{dimension}]: '))
                for dimension in range(dimensions)
                ]
            for i in range(int(input('No. of vectors: ')))
            ]
    if input('Parallel or Orthogonal: ').lower() == 'parallel':
        return parallel(inputs)
    return orthogonal(inputs)