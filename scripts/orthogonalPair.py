from scripts import dotProduct

calc = lambda vectors: [
                            [vectors[i], vectors[a]]
                        for i in range(len(vectors))
                        for a in range(len(vectors))
                        if dotProduct.calc([vectors[i], vectors[a]]) == 90 and
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
    return calc(inputs)