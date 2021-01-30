import os
import sys
import hashlib
from pathlib import Path
import shutil

#Creates folders for different file types
def makeFolders(downloadDirectory, fileTypes):
    for fileType in fileTypes.keys():
        directory = downloadDirectory + "\\" + fileType
        
        if not os.path.exists(directory):
            os.mkdir(directory)

#Moves file to its proper folder and delete any duplicates
def moveFile(moveFile, downloadDirectory, fileTypes):
    #The file format is what is after the period in the file name
    if "." in moveFile:
        temp = moveFile.split(".")
        fileFormat = temp[-1]
        fileFormat = fileFormat.lower()
        #print(fileFormat) 
    else:
        return

    for fileType in fileTypes.keys():
        #print(fileTypes)
        if fileFormat in fileTypes[fileType]:
           # print(moveFile)
            srcPath = downloadDirectory + "\\" + moveFile
            dstPath = downloadDirectory + "\\\\" + fileType + "\\\\" + moveFile
           # print(srcPath)
            print(dstPath)
            #If the file doesn't have a duplicate in the new folder, move it
            if not os.path.isfile(dstPath):
                #os.rename(srcPath, dstPath)
                shutil.move(srcPath,  dstPath)
            #If the file already exists with that name and has the same md5 sum
            elif os.path.isfile(dstPath) and \
                checkSum(srcPath) == checkSum(dstPath):
                os.remove(srcPath)
                print("removed " + srcPath)
            
    return

#Get md5 checksum of a file. Chunk size is how much of the file to read at a time.
def checkSum(fileDir, chunkSize = 8192):
        md5 = hashlib.md5()
        f = open(fileDir)
        while True:
            chunk = f.read(chunkSize)
            #If the chunk is empty, reached end of file so stop
            if not chunk:
                break
            md5.update(chunk)
        f.close()
        return md5.hexdigest()
		
def organize(path):

    #Dictionary contains file types as keys and lists of their corresponding file formats
    fileTypes = {}
    fileTypes["Images"] = ["jpg", "gif", "png", "jpeg", "bmp"]
    fileTypes["Audio"] = ["mp3", "wav", "aiff", "flac", "aac"]
    fileTypes["Video"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", \
                          "MOV", "mp4"]
    fileTypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf"]
    fileTypes["Executables"] = ["exe"]
    fileTypes["Compressed"] = ["zip", "tar", "7", "rar"]
    fileTypes["VM_ISO"] = ["vmdk", "ova", "iso"]
    fileTypes["Programming"] = ["c", "java", "py", "cpp"]
    
    #The second command line argument is the download directory
    #path = sys.argv[1]
    li = os.listdir(path)
    #li = list(Path(path).glob('**/*.*'))
    
    makeFolders(path, fileTypes)
    
    '''for filename in downloadFiles:
        print(path+ "\\" + filename)
        moveFile(filename, path, fileTypes)
    '''
    
    for file in li:
        #print(str(file))
        #print(type(str(file)))
        #file_n = open(str(file), encoding="utf8")
        #moveFile(file, path, fileTypes, str(file))
        moveFile(file, path, fileTypes)
