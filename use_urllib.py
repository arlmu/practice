#! /usr/bin/python3
# -*- coding: utf-8 -*-

from urllib import request, parse

#get:

with request.urlopen('https://www.baidu.com') as f:
    data = f.read()
    print('Staus:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' %(k,v))
    print('Data:', data.decode('utf-8'))



#advanced get:

req = request.Request('http://www.douban.com/')
#req.add_header('User-Agent', 'Mozilla/6.0(iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26(KHTML, like Gecko) Verson/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('User-Agent','Mozilla/5.0(X11;Ubuntu;Linux x86_64;rv:59.0)Gecko/20100202 Firefox/59.0')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
