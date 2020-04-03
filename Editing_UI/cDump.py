import subprocess
import sys
import re
import time
import os

class cDump_func(object):
    def command_dd(filepath,dirpath):
        print('dd if=' + filepath + ' of=' + dirpath + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.img')
        dd = 'dd if=' + filepath +' of='+dirpath+time.strftime('%Y-%m-%d', time.localtime(time.time()))+'.img'
     #   p = subprocess.run(dd, shell=True, universal_newlines=True)
        os.system(dd)