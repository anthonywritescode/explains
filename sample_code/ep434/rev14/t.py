import re


reg = re.compile(r'a(?>bc|b)c')
reg.match('abcc')
reg.match('abc')

reg = re.compile(r'".++"')
reg.match('"foo"')

reg = re.compile(r'"[^"]++"')
reg.match('"foo"')
