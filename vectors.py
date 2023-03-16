from scripts import *
import argparse

parser = argparse.ArgumentParser(description='Vectors Calculation Scripts')
parser.add_argument('scripts', help='Scripts wanting to execute. Format: script1,script2,script3')
parser.add_argument('values', nargs='?', const=True, help='Input values for the scripts')
args = parser.parse_args()

def main():
    run = f"rounded.rounded({'.calc('.join(args.scripts.split(','))}.calc("
    if args.values != None:
        return eval(f"{run}{args.values}))")
    return eval(f"{run[:-5]}inputs())")

if __name__ == '__main__':
    main()