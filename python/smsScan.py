
#coding=utf-8
import os
import codecs
import re

__metaclass__ = type

class Message():
	"""  """
	def __init__(self):
		self.type = 'RECV'
		self.phoneno = '0'
		self.name = ''
		self.time = ''
		self.content = ''
		self.answer = ''

def toJsonString(msgs):
	allStr = '[\n'
	for msg in msgs:
		allStr += '{'
		allStr += 'phone : '
		allStr += ('"'+msg.phoneno+'", ')
		allStr += 'time : '
		allStr += ('"'+msg.time+'", ')
		allStr += 'answer : '
		allStr += ('"'+msg.answer+'"')
		allStr += '}'

		if msg != msgs[-1]:
			allStr += ','
			
		allStr += '\n'
	allStr += ']'
	return allStr

# to do
def retrieveAnswer(content):
	return content

def readFile(name, msgs):
	oFile = codecs.open(name, 'r', 'utf-8-sig')
	lines = oFile.readlines()
	oFile.close()

	i = 0
	for line in lines:
		#if i==0: continue
		#print 'aaaa'

		if not re.search('^sms,deliver,', line):
			print "line:"+line + ' not match ^sms,deleiver'
			continue
		m = re.match('sms,deliver,(.+),(.+),,(.+,\d{3}),(.+)', line)

		if not m:
			print "line:"+line + ' not match groups'
			continue

		msg = Message()
		msg.phoneno = m.group(1)
		msg.name = m.group(2)
		msg.time = m.group(3)
		msg.content = m.group(4)
		msg.answer = retrieveAnswer(msg.content)
		
		msg.phoneno = re.sub('["\t]|\+86', '', msg.phoneno)

		msgs.append(msg)
		#print msg.content.encode('utf-8')
		i = i+1
"""
	i = 0
	for line in lines:
		if i > 0: 
			print line.encode('utf-8')
		i = i + 1
		if i > 1: break
"""
def writeFile(name, msgs):
	oFile = codecs.open(name, 'w', 'utf-8')
	oFile.write(toJsonString(msgs))
	oFile.close()