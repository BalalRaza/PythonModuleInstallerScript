import json
import pip

def install(package):
    return pip.main(['install', package])

fileName = input('Enter the JSON file name without extension: ')
fileName += '.json'
with open(fileName) as f:
    data = json.load(f)

if 'dependencies' in data:
    flag = False
    failed = []
    for r in data['dependencies']:
        pckg = str(r) + '==' + str(data['dependencies'][r])
        rc = install(pckg)
        if rc != 0:
            flag = True
            failed.append(str(r))
    if flag:
        print('List of modules that failed to download:')
        for s in failed:
            print(s)
    else:
        print('Success')
else:
    print("No dependencies found")







