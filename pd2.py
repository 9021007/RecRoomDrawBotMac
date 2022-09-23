import subprocess

def getPixelValues(x,y):
    out = subprocess.check_output(['cliclick', 'cp:' + str(x) +',' + str(y)])
    new = str(out).replace('b', '').replace("'", '').replace('\\', '').replace('n', '') 
    arr = tuple(int(x.strip()) for x in new.split(' '))
    print(arr)
    return arr