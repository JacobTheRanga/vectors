from dotenv import load_dotenv
from os import environ

load_dotenv('../.env')

def rounded(inputs):
    roundNum = int(environ.get('ROUNDING'))
    try:
        return print([round(i, roundNum) for i in inputs])
    except:
        try:
            return print([[round(i, roundNum) for i in a] for a in inputs])
        except:
            try:
                return print([[[round(i, roundNum) for i in a] for a in c] for c in inputs])
            except:
                return print(round(inputs, roundNum))