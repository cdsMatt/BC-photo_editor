#codeByMatt
from PIL import Image
import os, time, random, re

os.chdir(os.path.realpath(os.path.dirname(__file__)))

importDirectory = r"./input"
print(f"\nSet up input folder to: {importDirectory}")

tempDirectory = r"./temp"
print(f"Set up temp folder to: {tempDirectory}")

exportDirectory = r"./output"
print(f"Set up export folder to: {exportDirectory}")

logoPath = r"./src/logo_w.png"
print(f"Logo overlay set to file: {logoPath}")

Logo = Image.open(logoPath)
print("Logo succesfully loaded")

filesToWork = os.listdir(importDirectory)
print(f"Succesfully loaded images from folder {importDirectory}")

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

print(f"\nStarting converting to PNG RGBA...\n")

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

filesFromTemp = os.listdir(tempDirectory)
print(f"\nSuccesfully loaded images from folder {tempDirectory}\n")

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
    quit()
