import random

class FlightSimulator:
	def __init__(self):
		self.angle = random.randint(0, 90)
		self.disturbance = random.randint(1,7)

	def ajust(self,how_much):
		self.angle -= how_much
	
	def disturbance (self):
		self.disturbance = random.randint(1,7)
		self.angle += disturbance 


		
