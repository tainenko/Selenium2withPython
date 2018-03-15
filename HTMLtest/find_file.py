import os
#定義文件目錄
result_dir='D:\\testpro\\report'
lists=os.listdir(result_dir)

#重新接時間對目錄下的文件進行排序
lists.sort(key=lambda fn:os.path.getmtime(result_dir+'\\'+fn))
print('最新的文件為:'+list[-1])
file=os.path.join(result_dir,lists[-1])
print(file)