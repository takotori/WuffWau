import argparse
import rich
from wuffCreate import createDoggos
from wuffFind import getDoggo
from wuffStats import getDoggoNameLengths, getFamousDoggos, getMaleFemaleDoggoCount
from datamanager import getData

def run(create, info, stats, find):
    getData()

    if create:
        createDoggos(create)
    elif info:
        print("help")
    elif stats:
        print("test")
    elif find:
        getDoggo(find)
    else:
        print('No flag given.')


def get_parser():
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-c", "--create", help = "Create a new dog")
    g.add_argument("-i", "--info", help = "Get some help")
    g.add_argument("-s", "--stats", help = "Fetch doggo stats")
    g.add_argument("-f", "--find", help = "Find a dog by name")
    return parser

def main(args=None):
    args = get_parser().parse_args(args)
    run(create = args.create, info = args.info, stats = args.stats, find = args.find)

if __name__ == '__main__':
    main()
