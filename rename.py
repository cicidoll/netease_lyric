import os
 
#path为批量文件的文件夹的路径
path = './lyric'
 
#文件夹中所有文件的文件名
file_names = os.listdir(path)
 
#循环遍历所有文件名
for name in file_names:
	if name[-4:] == '.txt':
		os.renames(os.path.join(path,name),os.path.join(path, (name[:-3]+"lrc") ))
