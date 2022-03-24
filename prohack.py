import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Prohack").lisensi()
elif 'aarch' in arc:
	__import__("Prohack64").lisensi()
else:
	exit(f' Unknow device machine {arc}')
