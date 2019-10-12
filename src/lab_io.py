import os

print('hello', 'world')

workPath = os.getcwd()
print('当前路径：', workPath)

myFile = workPath + '\\src'
print('我的路径：', myFile)

if os.path.exists(myFile):
    print('文件夹', myFile, '已经存在了')
else:
    os.mkdir(myFile)

os.chdir(myFile)

print('Done')
