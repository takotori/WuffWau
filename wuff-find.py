from main import getData

def getDoggo(doggoname):
    for doggo in getData():
        if doggo["Hundename"] == doggoname:
            print(f'{doggo["Hundename"]} {doggo["Geburtsjahr"]} {doggo["Geschlecht"]}')
