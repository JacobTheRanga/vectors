calc = lambda inputs, operator: [
                                    eval(operator.join(
                                        [
                                            inputs[num][i]
                                        for num in range(len(inputs))
                                        ]
                                    ))
                                for i in range(3)
                                ]

def inputs():
    inputs = [
                [
                    input(f'Vector {num+1}[{i}]: ')
                for i in range(3)
                ]
            for num in range(int(input('How many vectors? ')))
            ]
    operator = input('Operator: ')
    return calc(inputs, operator)