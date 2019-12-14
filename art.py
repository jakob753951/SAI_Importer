from os import listdir
from os.path import isfile, join

paths = ["blotmap", "brushtex", "papertex"]

elemaps = [f for f in listdir("elemap") if isfile(join("elemap", f))]

for path in paths:
    allFiles = [f for f in listdir(path) if isfile(join(path, f))]

    if(path == "blotmap"):
        path = "brushform"
    with open(f'{path}.conf', 'w') as outFile:
        for filename in allFiles:
            
            if(path == "brushform"):
                outString = f'1,blotmap\\{filename}\n'
            else:
                outString = f'1,{path}\\{filename}\n'

            outFile.write(outString)
            print(outString)
        if path in ["brushform"]:
            for elemap in elemaps:
                outString = f'2,elemap\\{elemap}\n'
                outFile.write(outString)
                print(outString)