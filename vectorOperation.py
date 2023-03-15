from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

rounded = lambda vector: [round(i, int(environ.get('ROUNDING'))) for i in vector]
vector = lambda inputs, operator: [
                                        eval(operator.join(
                                            [
                                                inputs[num][i]
                                            for num in range(len(inputs))
                                            ]
                                        ))
                                    for i in range(3)
                                    ]

def main():
    inputs = [
                [
                    input(f'Vector {num+1}[{i}]: ')
                for i in range(3)
                ]
            for num in range(int(input('How many vectors? ')))
            ]
    operator = input('Operator: ')
    return print(rounded(vector(inputs, operator)))

if __name__ == '__main__':
    main()