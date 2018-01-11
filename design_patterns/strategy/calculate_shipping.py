from shipping import Default, Express, Sedex10


class Order(object):

	def __init__(self, value):
		self.__value = value

	@property
	def value(self):
		return self.__value


class CalculateShipping(object):

	def execute_calcule(self, order, shipping):
		total = shipping.calculate(order)
		print(total)
		


calc = CalculateShipping()
order = Order(500)


calc.execute_calcule(order,Default())
calc.execute_calcule(order,Express())
calc.execute_calcule(order,Sedex10())