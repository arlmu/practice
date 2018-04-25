#!/usr/bin/python3
# -*- codinf: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

print(' size last modified name')
print('---------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d %s %s%s' % (fsize, mtime, f, flag))
