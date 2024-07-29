# @time     ：2024/7/18 14:03
# @author   : 莉光哈哈哈
# @file     : test53_copy_files.py
# @software : PyCharm
'''
拷贝文件
'''
from shutil import *
from glob import glob

print('BEFORE:', glob('shutil_copyfile.*'))
copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')
print('AFTER:', glob('shutil_copyfile.*'))

'''copyfile()------调用了底层函数copyfileobj()
shutil.copyfileobj(fsrc, fdst[, length]): 复制文件内容（不包含元数据）从类文件对象src到类文件对dst。
可选参数length指定缓冲区的大小，负数表示一次性读入。默认会把数据切分成小块拷贝，以免占用太多内存。
注意：拷贝是从fsrc的当前文件开始'''

from shutil import *
import os
from StringIO import StringIO
import sys


class VerboseStringIO(StringIO):
    def read(self, n=-1):
        next = StringIO.read(self.n)
        print('read(%d) bytes')
        return next


lorem_ipsum = '''Lorem ipsum dolor sit amet.Vestibulum aliquam mollis dolor.Ut rutrum mi vel sem. Vestibulum ante 
ipsum.'''

print("Deafult")
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output)

print()

print("All at once:")
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, -1)

print()

print("Blocks of 256.")
input = VerboseStringIO(lorem_ipsum)
output = StringIO()
copyfileobj(input, output, 256)

'''
shutil.copy(src,dst)-----复制文件src到文件或目录dst，如果dst是目录，使用src相同的文件名创建（或者覆盖），权限位也会复制。src和dst的是字符串形式的路径名
'''
from shutil import *
import os

os.mkdir('example')
print('BEFORE:', os.listdir('example'))
copy('shutil_copy.py', 'example')
print('AFTER:', os.listdir('example'))

'''
shutil.copy2(src,dat)-----类似shutil.copy，元数据也复制，实际上先调用shutil.copy，然后使用copystat。这类似于Unix命令cp  -p
'''
from shutil import *
import os
import time


def show_file_info(filename):
    stat_info = os.stat(filename)
    print("\tMode:", stat_info.st_mode)
    print("\tCreated:", time.ctime(stat_info.st_ctime))
    print("\tAccessed:", time.ctime(stat_info.st_atime))
    print("\tModified:", time.ctime(stat_info.st_mtime))


os.mkdir('example')
print("SOURCE:")
show_file_info('shutil_copy2.py')
copy2('shutil_copy.py', 'example')
print('DEST:')
show_file_info('example/shutil_copy2.py')


'''
shutil.ignore_patterns(*patterns)为copytree的辅助函数，提供glob功能
'''
from shutil import copytree,ignore_patterns
copytree(source,destination,ignore=ignore_patterns('.pytest_cache'))


'''
拷贝文件元数据
shutil.copymode(src,dst)-----从SRC复制权限位到DST。该文件的内容，所有者和组不受影响。src和dst的是字符串形式的路径名
'''
from shutil import *
from commands import *
import os

with open('file_to_change.txt','wt') as f:
    f.write('content')

os.chmod('file_to_change.txt',0444)

print("BEFORE:")
print getstatus('file_to_change.txt')
copymode('shutil_copymode.py','file_to_change.txt')
print("AFTER:")
print getstatus('file_to_change.txt')


'''
shutil.copystat(src,dst)-----从src复制权限位，然后访问时间，最后修改时间，flag到dst。该文件的内容，所有者和组不受影响。src和dst的是给定的字符串路径名
'''
from shutil import *
import os
import time

def show_file_info(filename):
    stat_info=os.stat(filename)
    print("\tMode:",stat_info.st_mode)
    print("\tCreated:",time.ctime(stat_info.st_ctime))
    print("\tAccessed:",time.ctime(stat_info.st_atime))
    print("\tModified:",time.ctime(stat_info.st_mtime))

with open('file_to_change.txt','wt') as f:
    f.write('content')

os.chmod('file_to_change.txt',0444)

print("BEFORE:")
show_file_info('file_to_change.txt')
copystat('shutil_copystat.py','file_to_change.txt')
print("AFTER:")
show_file_info('file_to_change.txt')


'''
压缩解压缩
'''
import shutil

ret=shutil.make_archive("wwwww",'gztar',root_dir='')

rets=shutil.mak
e_archive("/User/wupeiqi/wwwww",'gztar')


'''
tarfile模块处理
'''
import tarfile,os

#压缩
tar=tarfile.open('your.tar','w')
tar.add(os.path.dirname(__file__),arcname="nonosd")
tar.add("firth.xml",arcname="first.xml")
tar.close()



