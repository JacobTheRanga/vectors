"""
Dot Product Calculator

This script finds the angle between
two vectors using the formula

a.b = |a|*|b|*cos(θ)

which is rearraged to get
angle θ

θ = acos((a.b)/(|a|*|b|))

Input Format: [[v1x, v1y, ...], [v2x, v2y, ...]]
"""

from math import acos, sqrt, degrees

# calc = acos((V0x*V1x + V0y*V1y...)/sqrt((v0x^2+v0y^2...)*(v1x^2+v1y^2...)))
sq = lambda x: sum([i**2 for i in x])
calc = lambda vectors: degrees(
                            acos(
                                sum(
                                [vectors[0][i]*vectors[1][i] 
                                for i in range(len(vectors[0]))]
                                )
                                /sqrt(
                                sq(vectors[0])*sq(vectors[1])
                                )
                            )
                        )

def inputs():
    dimensions = int(input('How many dimensions to the vectors: '))
    # vectors [[v0x, v0y...][v1x, v1y...]]
    vectors = [[float(input(f'Vector {vector+1} [{dimension}]: ')) 
                for dimension in range(dimensions)] 
                for vector in range(2)]
    return calc(vectors)