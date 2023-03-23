"""
Vectors Command Line Tool

This script enables users to run all vector scripts
through the command line with efficiency, as well
as allowing the user to run scripts through
each other's inputs in order to solve complex problems

************************************************************

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

----------------------------------------------------------
Get info about all other scripts
----------------------------------------------------------

~/ vectors.py -i <script>

----------------------------------------------------------
Get usage info about this script
----------------------------------------------------------

~/ vectors.py -i

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
from argparse import ArgumentParser
from dotenv import set_key, load_dotenv
from os.path import exists
from sys import modules

parser = ArgumentParser(description='Vectors Calculation Scripts')
parser.add_argument('-l', '--list', 
                    action='store_const', const=True, 
                    help='List all executable scripts'
                    )
parser.add_argument('-c', '--config', 
                    nargs='*', 
                    help='Change config file settings. (rounding=4 | rounding 4)')
parser.add_argument('-i', '--info', 
                    nargs='?', const=True, 
                    help='Usage info for specific script')
parser.add_argument('scripts', 
                    nargs='?', 
                    help='Scripts wanting to execute in accending order. (script1/script2/script3)')
parser.add_argument('-v', '--values', 
                    action='store_const', const=True, 
                    help='Input values for the scripts all at once instead of using the inbuilt function dependent input systems')
args = parser.parse_args()

def listScripts():
    for i in [
                a.__name__.split('.')[1] 
            for a in modules.values() 
            if a.__name__.split('.')[0] == 'scripts' and a.__name__ != 'scripts'
            ]:
        print(f'    -   {i}')
    return print('Get usage info with:\n~/ vectors.py -i <script>')

def info(script):
    if script == True:
        return print(__doc__)
    return eval(f'print({script}.__doc__)')

def config(pair):
    if pair == []:
        return set_key('.env', input('Variable: ').upper(), input('Value: '))
    if len(pair) == 1:
        if '=' not in list(pair):
            return set_key('.env', pair[0].upper(), input('Value: '))
        pair = ''.join(pair).split('=')
    return set_key('.env', pair[0].upper(), pair[1])

def runScripts(scripts, values):
    if scripts == None:
        scripts = input('Scripts: ')
    functions = False
    if len(scripts.split('.')) > 1:
        functions = scripts.split('.')[1]
    scripts = scripts.split('.')[0]
    run = f"rounded.rounded({'.calc('.join([scripts.split('/')[len(scripts.split('/'))-i-1] for i in range(len(scripts.split('/')))])}.calc("
    if values != None:
        if functions:
            run = f'{run[:-5]}{functions}('
        return eval(f"{run}{eval(input('Values: '))}))")
    return eval(f"{run[:-5]}inputs())")

def main():
    if not exists('.env'):
        set_key('.env', 'ROUNDING', '4')
    load_dotenv('.env')
    if args.list != None:
        return listScripts()
    if args.info != None:
        return info(args.info)
    if args.config != None:
        return config(args.config)
    return runScripts(args.scripts, args.values)
if __name__ == '__main__':
    main()