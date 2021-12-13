import requests
import csv

doggonames = []
doggobirth = []
doggogender = []


def getData(year):
    url = "https://ckan.opendata.swiss/api/3/action/package_show?id=hundenamen-aus-dem-hundebestand-der-stadt-zurich2"
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    map = {}
    for data in res.json()["result"]["resources"]:
        map[data["title"]["de"][0:4]] = data["download_url"]

    if year is not None:
        if year in map:
            request = requests.get(map[year])
        else:
            raise ValueError(f'No data for year {year} available')
    else:
        request = requests.get(map[max(map.keys())])

    request.encoding = "utf-8"
    insertToLists(request.text.splitlines())


def insertToLists(response):
    for doggo in csv.DictReader(response, ["Hundename", "Geburtsjahr", "Geschlecht"]):
        doggonames.append(doggo["Hundename"])
        doggobirth.append(doggo["Geburtsjahr"])
        doggogender.append(doggo["Geschlecht"])
