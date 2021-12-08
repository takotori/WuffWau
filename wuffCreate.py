from datamanager import doggonames, doggobirth
from random import choice
import shutil
from pathlib import Path
import os
import requests

def createDoggos(destination=None):
    doggoname = choice(list(set(doggonames)))
    doggobirthyear = choice(list(set(doggobirth)))
    return [doggoname, doggobirthyear, choice(["m", "w"]), getDoggoPicture(destination, doggoname, doggobirthyear)]

def getDoggoPicture(destination, doggoname, doggobirthyear):
    url = requests.get("https://random.dog/woof.json").json()["url"]

    if destination is None:
        destination = os.getcwd()

    pathstr = f'{destination}\\{doggoname}_{doggobirthyear}.{url.split(".")[-1]}'
    path = Path(pathstr)

    try:
        with open(path, 'x') as f:
            pass
    except OSError as e:
        raise SystemExit(e)

    with open(path, 'wb') as file:
        shutil.copyfileobj(requests.get(url, stream=True).raw, file)
    return pathstr
