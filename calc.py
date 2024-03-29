import sys
from parse import ParseArg

class Calc(ParseArg):
	def solve(self):
		self.clean()
		self.polynomial()
		if self.pol == 1:
			self.linear()
		elif self.pol == 2:
			self.quadratic()
	
	def clean(self):
		temp = {}
		for x in self.equ:
			if self.equ[x] != 0:
				temp[x] = self.equ[x]
		if bool(temp) == False:
			sys.exit('Each real number is a solution!')
		self.s_equ = dict(sorted(temp.items(), key=lambda item: item[0]))
		self.pol = [*self.s_equ][-1]
		i = 0
		while i < self.pol:
			if i in self.s_equ.keys():
				pass
			else:
				self.s_equ[i] = 0
			i += 1
		
	def polynomial(self):
		print ('Polynomial degree: %d' % int(self.pol))
		if self.pol > 2:
			sys.exit('The polynomial degree is strictly greater than 2, I can\'t solve.')
		if self.pol == 0:
			sys.exit('Invalid equation!')
	
	def linear(self):
		result = -(self.s_equ[0]) / self.s_equ[1]
		print ('The solution is:')
		print (int(result) if result == int(result) else round(result, 6))
	
	def quadratic(self):
		result = [0] * 2
		if self.s_equ[1] ** 2 < (4 * self.s_equ[2] * self.s_equ[0]):
			sys.exit('Discriminant is negative. The polynominal doesn\'t have real solutions.')
		result[0] = (-self.s_equ[1] - \
			(self.s_equ[1] ** 2 - (4 * self.s_equ[2] * self.s_equ[0])) ** 0.5) \
			/ (2 * self.s_equ[2])  
		result[1] = (-self.s_equ[1] + \
			(self.s_equ[1] ** 2 - (4 * self.s_equ[2] * self.s_equ[0])) ** 0.5) \
			/ (2 * self.s_equ[2])
		print('Discriminant is strictly positive, the two solutions are:') 
		print (int(result[0]) if result[0] == int(result[0]) \
				else round(result[0], 6))
		print (int(result[1]) if result[1] == int(result[1]) \
				else round(result[1], 6))
