# Unit01 - 07 查詢路徑下所有檔案
import os

# 輸入查詢路徑
yourPath = input()
ID =[]

# 顯示查詢結果
allFileList = os.listdir(yourPath)
print(allFileList)

# 逐一清查file list of folder
for file in allFileList:
    if os.path.isdir(os.path.join(yourPath, file)):
        print("This is a directory: " + file)
    elif os.path.isfile(os.path.join(yourPath, file)):
        print("This is a file: "+ file)
        ID.append(file[file.index('_')+1 : file.index('.')])
print(ID)

