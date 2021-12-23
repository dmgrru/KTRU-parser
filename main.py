# -*- coding: utf-8 -*-
import urllib.request

url = 'https://zakupki.gov.ru/epz/ktru/printForm/view.html?printFormId=92812&source=defaultKtruPF'
fname = './ktru.html'
# fp = urllib.request.urlopen(url)
# mybytes = fp.read()
# #mystr = mybytes.decode("utf8")
# fp.close()
# f = open(fname, 'wb')
# f.write(mybytes)
# f.close()

f = open(fname, 'r+',  encoding="utf8")
while 1:
    lines = f.readlines()
    if not lines:
        break
        print(lines)
f.close()