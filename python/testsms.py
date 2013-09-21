#coding=utf-8

from smsScan import *

msg1 = Message()
msg1.phoneno = '12345678'
msg1.content = 'hasdhahhsdfa'

msgs = []


readFile(r'../sms.csv', msgs)

writeFile(r'../sms.json', msgs)
"""
s = 'sms,deliver,"	+8613818908666",Cherry,,2013. 2.17 23:53,430,各种功能都试一遍啊'
print s.decode('utf-8').encode('gbk')
lst = re.split(',\t?', s)
for seg in lst:
	print seg.decode('utf-8').encode('gbk')

print re.sub('["\t]|\+86', '', lst[2]).decode('utf-8').encode('gbk')

m = re.match('sms,deliver,.+,.+,,.+,\d{3},(.+)', s)
if m:
	print m.group(1).decode('utf-8').encode('gbk').strip()

print 'abc\n\n\n'.strip()
"""