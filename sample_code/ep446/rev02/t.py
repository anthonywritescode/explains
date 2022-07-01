import os
import subprocess

os.system('rm -rf astpretty')
os.system('git clone -qq https://github.com/asottile/astpretty')
subprocess.call(('cd', 'astpretty'))
print('before git status!')
os.system('git status')
