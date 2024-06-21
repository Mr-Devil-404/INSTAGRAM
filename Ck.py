import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
mahadi=platform.architecture()[0]
if mahadi=="32bit":__import__("mahadi")
elif mahadi=="64bit":__import__("mahadi64")
