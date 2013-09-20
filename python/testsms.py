#codeing=UTF-8

from smsScan import *

msg1 = Message()
msg1.phoneno = '12345678'
msg1.content = 'hasdhahhsdfa'

msgs = []


#readFile(r'sms.csv', msgs)

#writeFile(r'sms.json', msgs)

str = 'sms,deliver,	+8613817206888,cherry,,2013. 2.17 23:53,430,asdasd'
print re.split(',\t?', str)