from datamanager import doggonames, doggobirth, doggogender

def getDoggo(doggoname):
    for i in range(len(doggoname)):
        if doggonames[i] == doggoname:
            print(f'{doggonames[i]} {doggobirth[i]} {doggogender[i]}')
