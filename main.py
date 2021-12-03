import argparse
from rich.table import Table
from rich.console import Console
from rich.style import Style
from wuffCreate import createDoggos
from wuffFind import getDoggo
from wuffStats import getDoggoNameLengths, getFamousDoggos, getMaleFemaleDoggoCount
from datamanager import getData

def run(create, info, stats, find):
    getData()
    console = Console()
    if create:
        print(createDoggos(create))


    elif info:
        print("help")
    elif stats:
        #todo custom year
        #todo add unknown gender
        print("test")
    elif find:
        table = Table(title = "The bestest doggos ever")
        table.add_column("Doggoname", justify="center", style="magenta")
        table.add_column("Geburtsdatum", justify="center", style="yellow")
        table.add_column("Geschlecht", justify="center", style="green")
        for doggo in getDoggo(find):
            table.add_row(doggo[0], doggo[1], doggo[2])
        console.print(table)
    else:
        print('No flag given.')


def get_parser():
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-c", "--create", help = "Create a new dog", default=None)
    g.add_argument("-i", "--info", help = "Get some help")
    g.add_argument("-s", "--stats", help = "Fetch doggo stats", action = 'store_true')
    g.add_argument("-f", "--find", help = "Find a dog by name")
    return parser

def main(args=None):
    args = get_parser().parse_args(args)
    run(create = args.create, info = args.info, stats = args.stats, find = args.find)

if __name__ == '__main__':
    main()
