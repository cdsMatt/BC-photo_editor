#codeByMatt
from PIL import Image
import os, time, random, re

os.chdir(os.path.realpath(os.path.dirname(__file__)))

asciiLogo = open(r"./src/ascii_logo.txt", "r")
Lines = asciiLogo.readlines()
count = 0

for line in Lines:
    count += 1
    print("{}".format(line.strip()))
    time.sleep(random.uniform(0.01,0.02))

importDirectory = r"./input"
print(f"\nSet up input folder to: {importDirectory}")
time.sleep(0.01)

tempDirectory = r"./temp"
print(f"Set up temp folder to: {tempDirectory}")
time.sleep(0.01)

exportDirectory = r"./output"
print(f"Set up export folder to: {exportDirectory}")
time.sleep(0.01)

logoPath = r"./src/logo_w.png"
print(f"Logo overlay set to file: {logoPath}")
time.sleep(0.01)

Logo = Image.open(logoPath)
print("Logo succesfully loaded")
time.sleep(0.01)

filesToWork = os.listdir(importDirectory)
print(f"Succesfully loaded images from folder {importDirectory}")
time.sleep(0.01)

print("Sorting list of files...")

temp = list()
for item in filesToWork:
    name, ext = item.split(".")
    rename = re.sub("[^0-9]", "", name)
    temp.append((int(rename), ext, name))
temp.sort()

print("List sorted!")

imageCount = len(temp)
print(f"Image count: {imageCount}")
time.sleep(0.01)

print(f"\nStarting converting to PNG RGBA...\n")
time.sleep(0.01)

startName = input("Zadaj cislo fotky alebo 'Enter': ")
print("\n")

if len(startName) > 0:
    for item in temp:
        ext = item[1]
        orname = f"{item[2]}.{ext}"
        itemName = str(item[0]) + "." + str(item[1])
        print(f"Converting {orname} ----> {startName}.{ext}")
        image = Image.open(f"{importDirectory}/{orname}").convert("RGBA")
        image.save(f"{tempDirectory}/{startName}.png")
        startName = int(startName) + 1

elif len(startName) == 0:
    for item in temp:
        ext = item[1]
        orname = f"{item[2]}.{ext}"
        itemName = str(item[0]) + "." + str(item[1])
        print(f"Converting {orname}")
        image = Image.open(f"{importDirectory}/{orname}").convert("RGBA")
        image.save(f"{tempDirectory}/{item[0]}.png")

print(f"\nStarting procesing...")
time.sleep(0.01)

filesFromTemp = os.listdir(tempDirectory)
print(f"\nSuccesfully loaded images from folder {tempDirectory}\n")
time.sleep(0.01)

temp = list()
for item in filesFromTemp:
    name, ext = item.split(".")
    temp.append((int(name),ext))
temp.sort()

for item in temp:
    item = str(item[0]) + "." + str(item[1])
    print(f"Process name: {item}")
    image = Image.open(f"{tempDirectory}/{item}").convert("RGBA")
    imageName = item.split(".")[0]
    image = image.resize(Logo.size)
    edit = Image.alpha_composite(image, Logo)
    edit.save(f"{exportDirectory}/{item}")
    # remove from temp
    path = os.path.join(tempDirectory, item)
    os.remove(path)

print(f"\nAll files succesfully edited\n")

answ = input("Press any key to exit...\n")

if answ:
    print("Bye...")
    time.sleep(2)
    quit()
