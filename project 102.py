import os
import shutil
source = "D:\\Whitehatjr\\Class102"
destination = "C:\\Users\\DIPRO\\Desktop"
listoffiles = os.listdir(source)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in[ '.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '\\' + filename
        path2 = destination + '\\' + "Document_Files"
        path3 = destination + '\\' + "Document_Files" + '\\' + filename
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)    