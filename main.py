import click
import requests
import csv

def getData():
    res = requests.get("https://ckan.opendata.swiss/api/3/action/package_show?id=hundenamen-aus-dem-hundebestand-der-stadt-zurich2").json()

    map = {}
    for data in res["result"]["resources"]:
        map[data["title"]["de"][0:4]] = data["download_url"]

    response = requests.get(map[max(map.keys())]).text.splitlines()

    reader = csv.DictReader(response, ["Hundename", "Geburtsjahr", "Geschlecht"])

    return reader



if __name__ == '__main__':
    getDoggo("Zorro")
