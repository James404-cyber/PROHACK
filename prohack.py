import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Prohack").teaching_fix()
elif 'aarch' in arc:
	__import__("Prohack64").teaching_fix()
else:
	exit(f' Unknow device machine {arc}')
