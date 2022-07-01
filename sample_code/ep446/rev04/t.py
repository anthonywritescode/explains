import os
import subprocess

os.system('rm -rf astpretty')
os.system('git clone -qq https://github.com/asottile/astpretty')
subprocess.call('cd astpretty', shell=True)
subprocess.call(('git', 'status'), cwd='astpretty')
