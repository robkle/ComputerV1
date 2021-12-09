import re
import sys

class ParseArg:
	def __init__(self, av):
		self.equ = {}
		self.process(av)

	def process(self, av):
		raw = av.replace(" ", "").split("=")
		self.trim(raw)
		if len(raw) != 2:
			sys.exit('Input contains an invalid equation!')
		self.parse(raw[0], 1)
		self.parse(raw[1], -1)

	def parse(self, side, sv):
		val = 1.0
		sign = 1
		parts = re.split('([+-]+)', side)
		self.trim(parts)
		if re.match('[+-]+', parts[-1]):
			sys.exit('Input contains an invalid equation!')
		for i in parts:
			if re.match('[+-]+', i):
				sign = -1 if i.count('-') % 2 == 1 else 1
			else:
				if re.match('\d*(\.?\d+)*\*?X\^\d+$', i):
					nums = re.split('\*?X\^', i)
					if (nums[0] != ''):
						val = float(nums[0])
					x = int(nums[1])
				elif re.match('\d*(\.?\d+)*\*?X$', i):
					nums = re.split('\*?X', i)
					if (nums[0] != ''):
						val = float(nums[0])
					x = 1
				elif re.match('^(\d+(\.?\d+)*)$', i):
					val = float(i)
					x = 0
				else:
					sys.exit('Input contains an invalid equation!')
				self.update(val * sign, x, sv)
				val = 1

	def trim(self, lst):
		for i in lst:
			if i == '':
				lst.remove(i)
	
	def update(self, val, x, sv):
		if (x in self.equ):
			self.equ[x] += val * sv
		else:
			self.equ[x] = val * sv

	def printequ(self):
		print('Reduced form: ', end = '')
		sorted_equ = dict(sorted(self.equ.items(), key=lambda item: item[0]))
		for x in sorted_equ:
			if list(sorted_equ.keys())[0] == x:
				print (int(sorted_equ[x]) \
						if sorted_equ[x] == int(sorted_equ[x]) \
						else sorted_equ[x], end = ' ')
			else:
				if float(sorted_equ[x]) < 0:
					print ('-', end = ' ')
				else:
					print ('+', end = ' ')
				print (abs(int(sorted_equ[x])) \
						if sorted_equ[x] == int(sorted_equ[x]) \
						else abs(sorted_equ[x]), end = ' ')
			print("* X^%d" % x, end = ' ')
		print('= 0')
