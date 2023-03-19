import platform
import os
if not os.path.exists("storage"):os.system('termux-setup-storage')
#os.system('termux-setup-storage')
#os.system('git pull')
#try:os.system('mkdir /sdcard/PROHACK-DATA')
#except:pass
#try:os.system('mkdir /sdcard/PROHACK-DATA/OK')
#except:pass
#try:os.system('mkdir /sdcard/PROHACK-DATA/CP')
#except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
        __import__("Pre").ninex()
elif 'aarch' in arc:
        __import__("kgf").ninex()
else:
        exit(f' Unknow device machine {arc}')
