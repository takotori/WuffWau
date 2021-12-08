import requests
import csv

doggonames = []
doggobirth = []
doggogender = []

def getData(year):
    res = requests.get(
        "https://ckan.opendata.swiss/api/3/action/package_show?id=hundenamen-aus-dem-hundebestand-der-stadt-zurich2").json()
    map = {}

    for data in res["result"]["resources"]:
        map[data["title"]["de"][0:4]] = data["download_url"]
    response = requests.get(map[max(map.keys())]).text.splitlines()

    for doggo in csv.DictReader(response, ["Hundename", "Geburtsjahr", "Geschlecht"]):
        doggonames.append(doggo["Hundename"])
        doggobirth.append(doggo["Geburtsjahr"])
        doggogender.append(doggo["Geschlecht"])
