
import csv
import shutil
import sys
import os
from PIL import Image
# import glob
# from pathlib import Path


# srcPath = sys.argv[1]

def copyImage(src, dest, dFolder, filename):
    print("COPY FUNC!")
    try:
        if os.path.exists(dFolder):
            im = Image.open(src)
            imR = im.resize((150,150), Image.ANTIALIAS)
            imR.save(dest, quality=100)
            # shutil.copy(src, dest)
            print("saved cropped image!")
            os.remove(src)
            print("deleted source image")
            # print("COPIED!")
        else:
            os.makedirs(dFolder)
            im = Image.open(src)
            imR = im.resize((150,150), Image.ANTIALIAS)
            imR.save(dest, quality=95)
            # shutil.copy(src, dest)
            print("saved cropped image after creating folder!")
            # os.remove(src)
            # print("removed source file!")
            # print("COPIED!2")
    except:
        print("Error!")
        # print("LUL")
        pass

fileList = []


with open('faces.csv', 'r') as facesFile:
    count  = 0
    reader = csv.reader(facesFile)
    for row in reader:
        # ['487', '97', '6014', 'Y Rajamani', 'baf52251-e2ac-44fc-a338-cc74abc72777.png'] //arr of strings
        count+=1
        # 6014 baf52251-e2ac-44fc-a338-cc74abc72777.png //string 
        # print(row[2], row[4])
        filename = row[4]
        # print(f"FILENAME: {filename}")
        foldername = row[2]
        fileList.append([filename, foldername])
        print(f"processing:")
        # print(f"file: {filename}\nfolder:{foldername}")
        toDestImageFolder = "sandbox" + os.sep + foldername
        fromSrcImageFolder = "nium_faces_dump"
        print(f"From: {fromSrcImageFolder}")
        print(f"To: {toDestImageFolder}")
        # print()
        
        fromD = fromSrcImageFolder+"/"+filename
        # print(f"FromD: {fromD}")
        toD = toDestImageFolder+"/"+filename
        # print(f"toD: {toD}")
        print(f"From: {fromD}")
        print(f"To: {toD}")
        copyImage(fromD, toD, toDestImageFolder, filename)
        # if os.path.exists(toDestImageFolder):
        #     shutil.copy(fromSrcImageFolder+"/"+filename, toDestImageFolder+"/"+filename)
        # else:
        #     os.makedirs(toDestImageFolder)
        #     shutil.copy(fromSrcImageFolder+"/"+filename, toDestImageFolder+"/"+filename)

    # print(srcPath)
# print(fileList)

# for l in fileList:
#     copyImage(l[0], l[1])