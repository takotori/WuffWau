import click
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
         ":peach:", ":leo:", ":circus_tent:", ":flying_saucer:", ":rose:", ":test_tube:", ":fishing_pole_and_fish:",
         ":leaves:", ":skull:", ":chicken:", ":octopus:", ":trident:", ":mag:", ":gem:", ":ringed_planet:", ":herb:",
         ":hourglass_flowing_sand:", ":owl:", ":game_die:", ":game_die:", ":chipmunk:", ":crystal_ball:", ":art:",
         ":woman_zombie:", ":fallen_leaf:", ":peacock:"]


def getRandomEmoji():
    # todo some emojis need more than 1 thing
    return choice(emoji)


@click.group()
@click.option('-y', '--year')
def cli(year):
    getData(year)


@cli.command()
@click.argument('doggoname')
def find(doggoname):
    allDoggos = getDoggo(doggoname)
    if not allDoggos:
        print(f'No dogs with name {doggoname} found')
        return
    buildTable(allDoggos)


@cli.command()
@click.option('-o', '--outputdir')
def create(outputdir):
    # todo test with custom outputdir
    doggo = createDoggos(outputdir)
    print("Here's your new dog!\n"
          f'Name: {doggo[0]}\n'
          f'Birth year: {doggo[1]}\n'
          f'Sex: {doggo[2]}\n'
          f'The image of the new dog can be found here: {doggo[3]}\n')


@cli.command()
def stats():
    names = getDoggoNameLengths()
    genderCount = getMaleFemaleDoggoCount()
    famousDoggos = ', '.join(getFamousDoggos())
    longestNames = ', '.join(names["longestName"])
    shortestNames = ', '.join(names["shortestName"])
    print(f'Shortest names: {shortestNames}')
    print(f'Longest names: {longestNames}')
    print('----------------------------------------------------------')
    print(f'Most common names: {famousDoggos}')
    print('----------------------------------------------------------')
    print(f'Male: {genderCount["male"]}')
    print(f'Female: {genderCount["female"]}')
    print(f'Unknown: {genderCount["unknown"]}')


def buildTable(allDoggos):
    console = Console()
    table = Table(title="The bestest doggos ever")
    table.add_column("Doggoname", justify="center", style="magenta")
    table.add_column("Geburtsdatum", justify="center", style="yellow")
    table.add_column("Geschlecht", justify="center", style="green")
    for doggo in allDoggos:
        table.add_row(f'{doggo[0]}',
                      f'{doggo[1]}',
                      f'{doggo[2]}')
    console.print(table)


if __name__ == '__main__':
    cli()
