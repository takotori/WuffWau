import argparse
from rich.table import Table
from rich.console import Console
from wuffCreate import createDoggos
from wuffFind import getDoggo
from wuffStats import getDoggoNameLengths, getFamousDoggos, getMaleFemaleDoggoCount
from datamanager import getData

from random import choice

emoji = [":bear:", ":robot:", ":cherry_blossom:", ":comet:", ":hammer:", ":star2:", ":corn:", ":izakaya_lantern:",
         ":apple:", ":heart:", ":anchor:", ":crescent_moon:", ":smiling_imp:", ":kiss:", ":ambulance:",
         ":evergreen_tree:", ":rice_ball:", ":people_holding_hands:", ":croissant:", ":butterfly:", ":fire:",
         ":crossed_swords:", ":pirate_flag:", ":dizzy:", ":sheep:", ":space_invader:", ":candy:", ":snowman:",
         ":peach:",
         ":leo:", ":circus_tent:", ":flying_saucer:", ":rose:", ":test_tube:", ":fishing_pole_and_fish:",
         ":leaves:", ":skull:", ":chicken:", ":octopus:", ":trident:", ":mag:", ":gem:", ":ringed_planet:", ":herb:",
         ":hourglass_flowing_sand:", ":feather:", ":game_die:", ":game_die:", ":chipmunk:", ":crystal_ball:", ":art:",
         ":woman_zombie:", ":fallen_leaf:", ":peacock:"]


def run(create, info, stats, find):
    getData()
    # todo custom year
    console = Console()
    if create:
        doggo = createDoggos(create)
        print("Here's your new dog!\n"
              f'Name: {doggo[0]}\n'
              f'Birth year: {doggo[1]}\n'
              f'Sex: {doggo[2]}\n'
              f'The image of the new dog can be found here: {doggo[3]}\n')
    elif info:
        print("help")
    elif stats:
        #todo add unknown gender
        print("test")
    elif find:
        table = Table(title = "The bestest doggos ever")
        table.add_column("Doggoname", justify="center", style="magenta")
        table.add_column("Geburtsdatum", justify="center", style="yellow")
        table.add_column("Geschlecht", justify="center", style="green")
        for doggo in getDoggo(find):
            table.add_row(f'{getRandomEmoji()}{doggo[0]}{getRandomEmoji()}',
                          f'{getRandomEmoji()}{doggo[1]}{getRandomEmoji()}',
                          f'{getRandomEmoji()}{doggo[2]}{getRandomEmoji()}')
        console.print(table)
    else:
        print('No flag given.')


def getRandomEmoji():
    # todo some emojis need more than 1 thing
    return choice(emoji)

def get_parser():
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group()
    g.add_argument("-c", "--create", help="Create a new dog", action='store_const', const=1)
    # todo add new argument for custom output dir
    g.add_argument("-i", "--info", help="Get some help")
    g.add_argument("-s", "--stats", help="Fetch doggo stats", action='store_true')
    g.add_argument("-f", "--find", help="Find a dog by name")
    return parser

def main(args=None):
    args = get_parser().parse_args(args)
    run(create = args.create, info = args.info, stats = args.stats, find = args.find)

if __name__ == '__main__':
    main()
