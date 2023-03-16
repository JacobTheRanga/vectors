from dotenv import load_dotenv
from os import environ
from os.path import dirname

load_dotenv(f'{dirname(dirname(__file__))}/.env')

def rounded(inputs):
    roundNum = int(environ.get('ROUNDING'))
    try:
        return print([round(i, roundNum) for i in inputs])
    except:
        try:
            for i in [[[round(i, roundNum) for i in a] for a in c] for c in inputs]:
                print(i)
            return
        except:
            return print(round(inputs, roundNum))