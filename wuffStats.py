from datamanager import doggonames, doggogender
from collections import Counter

def getDoggoNameLengths():
    longname = set()
    shortname = set()

    for doggo in doggonames:
        if len(doggo["Hundename"]) == max(doggonames):
            longname.add(doggo["Hundename"])
        elif len(doggo["Hundename"]) == min(doggonames):
            shortname.add(doggo["Hundename"])
    return {"longestName": longname, "shortestName": shortname}

def getFamousDoggos():
    famousdoggo = []
    for doggo in Counter(doggonames).most_common(10):
        famousdoggo.append(doggo[0])
    return famousdoggo

def getMaleFemaleDoggoCount():
    male = 0
    female = 0
    for doggo in doggogender:
        if doggo["Geschlecht"] == "m":
            male += 1
        else:
            female += 1
    return {"male": male, "female": female}
