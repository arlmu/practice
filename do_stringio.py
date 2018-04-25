#!/usr/bin/python3
#-*- coding: utf-8 -*-

from io import StringIO

#write to StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world')

print(f.getvalue())


#read from StringIO
f = StringIO('Hello\n world!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
