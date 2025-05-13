# Unit01 - 08 Management of File Directory
import os
import shutil

# 先確認file path下有沒有file或是directory
if os.path.exists('files'):
    shutil.rmtree('files')
os.mkdir('files')

# 建立預計要有的folder數量
n = int(input("Please enter a number for creating the subdirectory: "))

# 建立預期目錄架構
os.chdir('files')
for i in range(1, n+1):
    os.mkdir('f'+str(i))
print(sorted(os.listdir()))
print("-----first step for creating the directory --------")

os.rename('f1', 'folder1')
print(sorted(os.listdir()))
print("-----second step for change the name of subdirectory --------")

os.rmdir('folder1')
print(sorted(os.listdir()))
print("-----third step for removing the sub subdirectory --------")

os.chdir('../')
shutil.rmtree('files')
print("-----final step for removing the directory --------")

