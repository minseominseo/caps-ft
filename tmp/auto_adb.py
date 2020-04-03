# -*- coding:utf-8 -*-
import os
import subprocess
import sys


# adb C:에 다운받아서 압축 풀기
# 그 위치 환경변수로 적용
env = os.environ
newPath = r'C:\\platform-tools' + env['PATH']


# adb devices로 접속 확인
# unauthentized 뜰 경우 print"해당 기기의 드라이버 설치"
devices_output = subprocess.check_output('adb devices', shell=True, universal_newlines=True)
print(devices_output)
if 'unauthorized' in devices_output:
    print('install driver of the devices'.encode())
    sys.exit(1)


# 존재하는 partitions 확인
partitions_list = subprocess.check_output(['adb', 'shell', 'cat', '/proc/partitions'], shell=True, universal_newlines=True)
print(partitions_list)


# disk dump
disk = input('원하는 파티션을 선택하시오.\nex)dd if=/dev/block/mmcblk0 of=/sdcard/test.img\n:')
disk = 'su -c \'mount -o remount,rw /; ' + disk + '\''
command = disk.split()
p = subprocess.Popen(['adb', 'shell'] +command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)


print('Done!')
