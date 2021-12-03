from datamanager import doggonames, doggobirth, doggogender

def getDoggo(doggoname):
    doggoList = []
    for i in range(len(doggonames)):
        if doggonames[i] == doggoname:
            doggoList.append([doggonames[i], doggobirth[i], doggogender[i]])
    return doggoList