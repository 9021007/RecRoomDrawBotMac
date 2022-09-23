import pyperclip
import os
import time

print("macOS String Importer by Bobrobot1")
time.sleep(0.2)
print("Make sure you have cliclick installed, and have given your editor permission to control your cursor.")
time.sleep(0.2)
# Prompt user for cursor smoothing setting

smooth = input("Enable cursor smoothibility? (y/n) ")
if(smooth == 'y'):
    smoothsetting = '-e 200'
    print("Cursor smoothibility enabled.")
elif(smooth == 'n'):
    smoothsetting = ''
    print("Cursor smoothibility disabled.")
else:
    print("Error 1: not 'y' or 'n'")
    exit()

# Promot iser for verbose cursor logs

verbose = input("Enable verbose cursor? (y/n) ")
if(verbose == 'y'):
    verbosesetting = '-m verbose'
    print("Verbose cursor enabled.")
elif(verbose == 'n'):
    verbosesetting = ''
    print("Verbose cursor disabled.")
else:
    print("Error 1: not 'y' or 'n'")
    exit()

# Promot user for wait multiplier

waitmultiplier = 1
wait = input("Set wait multiplier? (y/n) ")
if(wait == 'y'):
    customwait = input("Enter wait multiplier: ")
    try:
        waitmultiplier = float(customwait)
        print("Wait multiplier set to " + customwait)
    except ValueError:
        print("Not a number")
        exit()

elif(wait == 'n'):
    waitmultiplier = 1
    print("Wait multiplier set to 1 (default).")
else:
    print("Error 2: not 'y' or 'n'")
    exit()

# Prompt user for path to file

file = input("Enter file name: ")

try:
  with open(file, 'r') as s:
    lines = s.readlines()
    print("File read")
except:
    print("Error 3: No file named " + file +  " was found.") 
    print("file '" + file + "' eithevr does not exist, or this program does not have permission to read it.") 
    exit()

# Process file

print("Attempting filter")
lines = [line.replace('\n', '') for line in lines]
print("Success.")

# Display line count

print("Line Count Detected: " + str(len(lines)))

# Prompt user for data offset

offset = input("Enter offset: ")
try:
    offset = int(offset)
except ValueError:
    print("Not a number")
    exit()

# Prompt user to hover on advance buttton

if offset > 0:
    input("Center mouse on advance button, then press enter to continue.")
    for i in range(0, offset):
        os.system("cliclick " + verbosesetting + " -r c:. w:100")
        print("Skipped " + str(i) + " lines")

# Instruct user to hover on crosshair

input("Center mouse on crosshair, then press enter to continue.")

# Iterate through data

os.system("cliclick -m verbose -r c:. ")
for i in lines:
    if lines.index(i) > offset:
        # Copy to clipboard
        pyperclip.copy(i)
        # Cursor actions
        code = "cliclick " + verbosesetting + " -r " + smoothsetting + " m:-380,+180 c:. m:+750,+50 c:. w:" + str(300 * waitmultiplier) + " m:-400,-350 c:. w:" + str(300 * waitmultiplier) + " kd:cmd w:50 t:'v' w:50 ku:cmd m:+460,+470 w:20 c:. w:" + str(300 * waitmultiplier) + " c:. w:" + str(300 * waitmultiplier)
        os.system(code)
        # Update progress readout
        print("Line " + str(lines.index(i)) + " imported.")
        print(str(round(100 * (lines.index(i) + 1) / len(lines), 2)) + "% imported")
        print("Estemated time: " + str((((1.2 * waitmultiplier) + 0.1) * len(lines)) - (((1.2 * waitmultiplier) + 0.1) * lines.indexv(i))) + " seconds")
    else: 
        # Displayed when skipping loop due to offset
        print("Detected offset of " + str(lines.index(i)) + " lines")
