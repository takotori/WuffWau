from main import getData
from collections import Counter

def getDoggoStats():
    print("testtesttest")

def getDoggoNameLengths():
    doggoNames = []

    for doggo in getData():
        doggoNames.append(len(doggo["Hundename"]))

    highestNr = max(doggoNames)
    lowestnr = min(doggoNames)

    longname = set()
    shortname = set()

    for doggo in getData():
        if len(doggo["Hundename"]) == highestNr:
            longname.add(doggo["Hundename"])
        elif len(doggo["Hundename"]) == lowestnr:
            shortname.add(doggo["Hundename"])

    print(longname)
    print(shortname)

def getFamousDoggos():
    doggoNames = []
    for doggo in getData():
        doggoNames.append(doggo["Hundename"])
    doggoNameCounter = Counter(doggoNames)

    for doggo in doggoNameCounter.most_common(10):
        print(doggo[0])

def getMaleFemaleDoggoCount():
    male = 0
    female = 0
    for doggo in getData():
        if doggo["Geschlecht"] == "m":
            male += 1
        else:
            female += 1
    print(f'Male Dogs: {male}, Female Dogs: {female}')
