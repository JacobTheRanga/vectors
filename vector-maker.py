from math import sin, asin, cos, acos, tan, atan

def angleMap(num):
    for i in range(num):


def main():
    inputTypes = input('Type of inputs[eg. angle-2 length-1]: ').split(' ')
    for i in inputTypes:
        i = i.split('-')
        if i[0] == 'angle':
            return angleMap(i[1])
        return lengthMap(i[1])
        


if __name__ == '__main__':
    main()