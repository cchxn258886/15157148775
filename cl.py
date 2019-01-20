#author Bape Aaron   rybapp201811
import time
import os
import shutil
import datetime

today = datetime.date.today()
print(today)
the_mouth_firstday = today.replace(day=1)
the_last_month = the_mouth_firstday - datetime.timedelta(days=1)
the_last_month1 = the_last_month.strftime('%Y%m%d')# stt 格式时间
usemonth = the_last_month.strftime('%Y%m')
log_dir_name = 'rybapp'+ usemonth
print(log_dir_name)

dirpath = os.getcwd()


def log(message):
    dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir, 'error.log'), 'a') as fh:
        fh.write(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S') + '        ' + message + "\n")


list1 = []
list2 = []

class move(object):   #class
    def __init__(self,dirpath):
        self.dirpath = dirpath
    def get_file_name(self):
        for file_name in os.listdir():
            if os.path.isfile(file_name):
                dir_file_name = os.path.join(dirpath,file_name)
                if the_last_month1 > time.strftime('%Y%m%d',time.localtime(os.path.getmtime(dir_file_name))):
                    list1.append(dir_file_name)
        return list1   #得到目录下文件
    def get_directory_name(self):
        for directory_name  in os.listdir():
            if os.path.isdir(directory_name):
                dir_directory_name = os.path.join(dirpath,directory_name)
                list2.append(dir_directory_name)
        return list2   #得到文件夹


dir = move(dirpath)
all_file_name = dir.get_file_name()
all_dir_name = dir.get_directory_name()
print(all_file_name)
print(all_dir_name)
try:
    if os.path.exists(os.path.join(dirpath,log_dir_name)):
        for file_name in all_file_name:
            shutil.move(os.path.join(dirpath,file_name),os.path.join(dirpath,log_dir_name))
    else:
        os.mkdir(os.path.join(dirpath,log_dir_name))
        for file_name in all_file_name:
            shutil.move(os.path.join(dirpath,file_name),os.path.join(dirpath,log_dir_name))
    shutil.move(os.path.join(dirpath,log_dir_name),'/data/nfsmount/./')
except Exception as e:
    log('detail %s'%str(e))
