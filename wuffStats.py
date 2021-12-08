from datamanager import doggonames, doggogender
from collections import Counter

def getDoggoNameLengths():
    longname = set()
    shortname = set()

    for doggo in doggonames:
        if len(doggo) == len(max(doggonames, key=len)):
            longname.add(doggo)
        elif len(doggo) == len(min(doggonames, key=len)):
            shortname.add(doggo)
    return {"longestName": longname, "shortestName": shortname}

def getFamousDoggos():
    famousdoggo = []
    for doggo in Counter(doggonames).most_common(10):
        famousdoggo.append(doggo[0])
    return famousdoggo


def getMaleFemaleDoggoCount():
    male = doggogender.count("m")
    female = doggogender.count("w")
    return {"male": male, "female": female, "unknown": len(doggogender) - male - female}
