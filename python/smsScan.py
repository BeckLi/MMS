
#coding=UTF-8
import os
import codecs
import re

__metaclass__ = type

class Message():
	"""  """
	def __init__(self):
		self.type = 'RECV'
		self.phoneno = '0'
		self.content = ''
		self.answer = ''

def myFunction():
	print "xxadafsdf"

def readFile(name, msgs):
	oFile = codecs.open(name, 'r', 'utf-8-sig')
	lines = oFile.readlines()
	oFile.close()

	i = 0
	for line in lines:
		#if i==0: continue
		#print 'aaaa'
		if not re.search('^sms,deliver,', line):
			continue

		msg = Message()
		msg.content = line
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

	for msg in msgs:
		oFile.write(msg.content)
	#oFile.write(os.linesep)
	oFile.close()