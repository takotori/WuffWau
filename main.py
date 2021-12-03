import click
import requests
import csv

def getData():
    res = requests.get("https://ckan.opendata.swiss/api/3/action/package_show?id=hundenamen-aus-dem-hundebestand-der-stadt-zurich2").json()

    map = {}
    for data in res["result"]["resources"]:
        map[data["title"]["de"][0:4]] = data["download_url"]
    response = requests.get(map[max(map.keys())]).text.splitlines()
    return csv.DictReader(response, ["Hundename", "Geburtsjahr", "Geschlecht"])

def getDoggo(doggoname):
    for doggo in getData():
        if doggo["Hundename"] == doggoname:
            print(f'{doggo["Hundename"]} {doggo["Geburtsjahr"]} {doggo["Geschlecht"]}')

def getDoggoStats():
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



if __name__ == '__main__':
    getBeegDoggoStats()