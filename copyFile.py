import os
import random
from random import randint
import shutil

def getDirAndCopyFile(sourcePath):

    if not os.path.exists(sourcePath):
        return

    absourcePathtrain = os.path.join(sourcePath,"train.txt")
    result = []

    for folder in ( folder for folder in os.listdir(sourcePath) if os.path.isdir(sourcePath+'/'+folder)):
        # folder
        count =0

        for fileTempName  in os.listdir(sourcePath+'/'+folder):
            shortName,extension = os.path.splitext(fileTempName)
            if extension == ".xml":
                count = count +1
        #print count
        if count <1000:
            increase = 1000 - count
            f = open(absourcePathtrain, 'r')


            for num, line in enumerate(f, 1):
                #print num 
                if folder in line:
                    print folder
                    result.append(num)
            f.close()

            for i in range(increase):
                pick = random.choice(range(1, max(result)-1))
                print pick
                f = open(absourcePathtrain, 'rb')
                #print f.readlines()
                temLine = f.readlines()
                #temLine = temLine.strip('\n')
                #print temLine[pick]
                head,tail = os.path.split(temLine[pick])
                print tail
                f.close()
                shortName2,extension2 = os.path.splitext(tail)
                absourcePathxml = os.path.join(sourcePath+'/'+folder, tail).strip('\n')
                absourcePathxml.replace('\\n',"")
                #print absourcePathxml
                absourcePathjpg = os.path.join(sourcePath+'/'+folder, shortName2+".jpg")
               # print absourcePathxml
                tempInt= randint(10000, 99999)
                fileName = shortName2 + str(tempInt)
                xmlName = fileName + ".xml"
                jpgName = fileName +".jpg"
                xmlPath = os.path.join(sourcePath+'/'+folder, xmlName)
                jpgPath = os.path.join(sourcePath+'/'+folder, jpgName)
                absourcePathxml.replace('\\n',"")
                #print xmlPath
                #print jpgPath
                shutil.copy(absourcePathxml
                    ,xmlPath)
                shutil.copy(absourcePathjpg,jpgPath)
                f = open(absourcePathtrain, 'a')
                f.write(xmlPath+'\n')
                #f.write(jpgPath+'\n')
                f.close()

if __name__ == '__main__':  
    getDirAndCopyFile("batch1")


