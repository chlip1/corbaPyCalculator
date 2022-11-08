import sys
from omniORB import CORBA 
import Calculator, Calculator__POA

class Calc_i(Calculator__POA.Calc):
	def sum(self, val1, val2):
		print("Wykonano dodawanie na serwerze")
		return val1 + val2

	def subtract(self, val1, val2):
		print("Wykonano odejmowanie na serwerze")
		return val1 - val2

	def multiply(self, val1, val2):
		print("Wykonano mnozenie na serwerze")
		return val1 * val2
	
	def divide(self, val1, val2):
		print("Wykonano dzielenie na serwerze")
		return val1 / val2

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

ei = Calc_i()
eo = ei._this()	

print(orb.object_to_string(eo))

poaManager = poa._get_the_POAManager()
poaManager.activate()

orb.run()