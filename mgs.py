import numpy
import matplotlib
import matplotlib.pyplot as plt
import os
import re

def getListFiles(path):#返回当前路径所有额eds文件路径
    assert os.path.isdir(path), '%s not exist.' % path
    ret = []
    eds=[]
    for root, dirs, files in os.walk(path):    #读取路径当前目录，子目录，文件
        #print ('%s, %s, %s' % (root, dirs, files))
        for filespath in files:
            ret.append(os.path.join(root,filespath))
        #print(ret)
        for item in ret:
            having=re.search('lbl',item)#正则表达式匹配所有.lbl文档
            if not having:
                eds.append(item)     #把在所有的eds文本放入eds列表
        return eds

def getline(thefilepath, desired_line_number):#读取文本文档的指定行，返回读取数据矩阵
    #global line
    if desired_line_number < 1:
        return ''
    liness=[]
    matrax=[]
    while True:
        for current_line_number, line in enumerate(open(thefilepath, 'r')):
            if current_line_number >= desired_line_number - 1 :
                lines=line.split(',')
                for i in lines:
                    liness.append(float(i))
                matrax.append(liness)
                liness=[]
        return matrax
#data=getline(r'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1007\eds\8358d47a.eds',2)
paths=['D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1007\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1010\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1011\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1015\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1019\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1023\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1024\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1027\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1028\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1029\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1030\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1035\eds',
'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1036\eds']#mgs数据所在文件夹
files=[]
for path in paths:
    file=getListFiles(path)
    files.extend(file)
#print(files,len(files))
i=0
datas=[]
for file in files:
    data= getline(file, 2)
    datas.extend(data)
print(len(datas))
lon=[]
lati=[]
for items in datas:
    lon.append(items[3])
    lati.append(items[2])
print(len(lon))
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(lon,lati,marker='.')
ax.set_xlabel('longitude')
ax.set_ylabel(' latitude ')
ax.grid(color='g', linestyle='-', linewidth=0.5)
fig.show()

