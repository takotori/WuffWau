import click
from rich.table import Table
from rich.console import Console
from wuffCreate import createDoggos
from wuffFind import getDoggo
from wuffStats import getDoggoNameLengths, getFamousDoggos, getMaleFemaleDoggoCount
from datamanager import getData

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
    doggo = createDoggos(outputdir)
    print("Here's your new dog!\n"
          f'Name: {doggo[0]}\n'
          f'Birth year: {doggo[1]}\n'
          f'Sex: {doggo[2]}\n'
          f'The image of the new dog can be found here: {doggo[3]}\n')


@cli.command()
def stats():
    console = Console()
    names = getDoggoNameLengths()
    genderCount = getMaleFemaleDoggoCount()
    console.rule("[bold red] Longest/Shortest Names")

    print(f'Shortest names: {", ".join(names["shortestName"])}\n'
          f'Longest names: {", ".join(names["longestName"])}')

    console.rule("[bold red] Top 10 common names")

    print(f'Most common names: {", ".join(getFamousDoggos())}')

    console.rule("[bold red] Gender Count")

    print(f'Male: {genderCount["male"]}\n'
          f'Female: {genderCount["female"]}\n'
          f'Unknown: {genderCount["unknown"]}')


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
