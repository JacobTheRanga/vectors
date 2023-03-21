"""
Usage:

---------------------------------------
Run script with an input guide:
---------------------------------------

~/ vectors.py <script>
= <script>.inputs()

-----------------------------------------------
Run script with an already established input:
-----------------------------------------------

~/ vectors.py -v <script>
= <script>.calc(<values>)

------------------------------------------------------------------------
Run multiple scripts through each other's inputs with an input guide:
------------------------------------------------------------------------

~/ vectors.py <script1>/<script2>/<script3>
= <script3>.calc(<script2>.calc(<script3>.inputs()))

==========================================================================

Config:

------------------------------
Change config variable:
------------------------------

~/ vectors.py -c
Variable: <variable>
Value: <value>

or

~/ vectors.py -c <variable>
Value: <value>

or

~/ vectors.py -c <variable> <value>

or

~/ vectors.py -c <variable>=<value>
"""

from scripts import *
import argparse
from dotenv import set_key, load_dotenv
from os.path import exists

parser = argparse.ArgumentParser(description='Vectors Calculation Scripts')
parser.add_argument('-c', '--config', nargs='*', help='Change config file settings. (rounding=4 | rounding 4)')
parser.add_argument('scripts', nargs='?', help='Scripts wanting to execute in accending order. (script1/script2/script3)')
parser.add_argument('-v', '--values', action='store_const', const=True, help='Input values for the scripts all at once instead of using the inbuilt function dependent input systems')
args = parser.parse_args()

def config(pair):
    if pair == []:
        return set_key('.env', input('Variable: ').upper(), input('Value: '))
    if len(pair) == 1:
        if '=' not in list(pair):
            return set_key('.env', pair[0].upper(), input('Value: '))
        pair = ''.join(pair).split('=')
    return set_key('.env', pair[0].upper(), pair[1])

def main():
    if not exists('.env'):
        set_key('.env', 'ROUNDING', '4')
    load_dotenv('.env')
    if args.config != None:
        return config(args.config)
    if args.scripts == None:
        args.scripts = input('Scripts: ')
    run = f"rounded.rounded({'.calc('.join([args.scripts.split('/')[len(args.scripts.split('/'))-i-1] for i in range(len(args.scripts.split('/')))])}.calc("
    if args.values != None:
        return eval(f"{run}{eval(input('Values: '))}))")
    return eval(f"{run[:-5]}inputs())")

if __name__ == '__main__':
    main()