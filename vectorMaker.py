from math import sin, asin, cos, acos, tan, atan, sqrt

def mapInputs(plane):
    mappedInputs = {}
    mappedInputs['inputNums'] = {}
    inputTypes = input(f'Type of inputs for plane {plane+1} [eg. angle-2 length-1]: ')
    inputTypes = inputTypes.split(' ')
    mappedInputs['rightAngle'] = input(f'Points describing right angle on plane {plane+1} [e.g ABC]: ')
    points = mappedInputs['rightAngle'].split('')
    mappedInputs['modulus'] = points[0]+points[2]
    for i in inputTypes:
        i = i.split('-')
        mappedInputs[i[0]] = [[],[]]
        i[1] = int(i[1])
        mappedInputs['inputNums'][i[0]] = i[1]
        for a in range(i[1]):
            points = input(f'Points for {i[0]} {a+1} [eg, AB]: ')
            value = float(input(f'Value of {i[0]} {a+1}: '))
            mappedInputs[i[0]].append(points)
            mappedInputs[i[0]].append(value)
    return mappedInputs

def trig(angles, lengths, modulus):
    
        
def pythag(lengths, modulus):
    points = lengths[0]
    for i in points:
        if points != modulus:
            b = points
            for i in (n:=modulus.split('')):
                if i in (m:=b.split('')):
                    del m[i]
                    del n[i]
                    newPoints = n[0] + m[0]
    return [[newPoints, b], [sqrt(lengths[modulus]^2 - lengths[b]^2), lengths[b]]]

def planeCalc(plane, inputNums):
    if inputNums['length'] <= 1:
        return trig(plane['angle'], plane['length'], plane['modulus'])
    return pythag(plane['length'], plane['modulus'])
    

def vectorCreate(planes, axis):
    for i in planes:
        inputNums = i['inputNums']
        plane = i[1:]
        planes[i] = planeCalc(plane, inputNums)   

def main():
    planesNum = int(input('Dimensional Planes: '))
    planes = []
    axis = input('Axis in terms of points[e.g AB AC AD]: ')
    axis = axis.split(' ')
    for i in range(planesNum):
        planes.append(mapInputs(i))
    vector = vectorCreate(planes, axis)
    for i in vector:
        vector[i] = round(i, 4)
    print(vector)

if __name__ == '__main__':
    main()