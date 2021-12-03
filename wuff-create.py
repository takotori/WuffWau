from main import getData
from random import choice
import shutil
from pathlib import Path
import os
import requests

def createDoggos(destination=None):
    doggonames = set()
    doggobirth = set()

    for doggo in getData():
        doggonames.add(doggo["Hundename"])
        doggobirth.add(doggo["Geburtsjahr"])

    doggoname = choice(list(doggonames))
    doggobirthyear = choice(list(doggobirth))

    url = requests.get("https://random.dog/woof.json").json()["url"]
    picture = requests.get(url, stream=True)

    if destination == None:
        destination = os.getcwd()

    pathstr = f'{destination}\\{doggoname}_{doggobirthyear}.{url.split(".")[-1]}'
    path = Path(pathstr)

    with open(path, 'wb') as file:
        shutil.copyfileobj(picture.raw, file)

    return [doggoname, doggobirthyear, choice(["m", "w"]), pathstr]
