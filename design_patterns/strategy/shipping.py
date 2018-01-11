# HERE ARE ALL CALCULES MODES OF SHIPPING


class Default(object):

	def calculate(self, orderi):
		return orderi.value * 0.05


class Express(object):	

	def calculate(self, order):
		return order.value * 0.1


class Sedex10(object):	

	def calculate(self, order):
		return order.value * 0.2
