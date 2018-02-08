import os
import re

def getListFiles(path):
    assert os.path.isdir(path), '%s not exist.' % path
    ret = []
    eds=[]
    for root, dirs, files in os.walk(path):
        #print ('%s, %s, %s' % (root, dirs, files))
        for filespath in files:
            ret.append(os.path.join(root,filespath))
        print(ret)
        for item in ret:
            having=re.search('lbl',item)
            if not having:
                eds.append(item)
        return eds
        '''pattern=re.compile(r'.+?\\eds.+?eds')
        filepath=re.findall(pattern,str(ret))
        print(filepath)'''
        return
file=getListFiles(r'D:\电离层数据\火星电离层\mgs-m-rss-5-sdp-v1\mors_1007\eds')
print(file)