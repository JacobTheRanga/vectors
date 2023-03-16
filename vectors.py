from scripts import *
import argparse

parser = argparse.ArgumentParser(description='Vectors Calculation Scripts')
parser.add_argument('scripts', help='Scripts wanting to execute in accending order. Format: script1/script2/script3')
parser.add_argument('-v', '--values', nargs='?', const=True, help='Input values for the scripts')
parser.add_argument('-i', '--input', nargs='?', const=True, help='Use function specific input system')
args = parser.parse_args()

def main():
    run = f"rounded.rounded({'.calc('.join([args.scripts.split('/')[len(args.scripts.split('/'))-i-1] for i in range(len(args.scripts.split('/')))])}.calc("
    if args.values != None:
        return eval(f"{run}{eval(input('Values: '))}))")
    return eval(f"{run[:-5]}inputs())")

if __name__ == '__main__':
    main()