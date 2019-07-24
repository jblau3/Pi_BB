class Hardware():
	
	#import json # for perfRPT
	
	def __init__(self):		
		self.load_power = 25
		self.motorPin = 2
		self.motor_state = 1
		self.motorPower = 30.0

	#begin motor........................................................
	
	### MOTOR GPIO PIN
	def set_motorPin(self, motorPin):
	    print "Setting motor pin %i"%motorPin
	    self.motorPin=motorPin
	
	### MOTOR SET STATE
	def set_motor_state(self, motor_state):    
		motor_state = self.motor_state
		if motor_state == 1:
			print "Setting motor state ON"
		else:
			print "Setting motor state to OFF"			
		self.motor_state = motor_state	
		return self.motor_state	
	
	### MOTOR GET STATE	
	def get_motor_state(self):
	### responsible for reading gpio pin state
		return self.motor_state
		
	### MOTOR SET POWER
	def set_motor_power(self, motorPower):
		motor_power= self.motorPower
		print "Setting motor power %i"%motorPower
	
	###MOTOR GET POWER	
	def get_motor_power(self):
	### responsible for reading motor power
	    return self.motorPower	
	    
	#end motor........................................................
	
	
	#for setting heat load power      
	def set_heat_power(self, load_power):
	### responsible for power to the cooler heat load
		print "Setting heat load watts to %i"%load_power
		self.load_power=load_power
		
		
	#load power ON/OFF	
	#def set_power_state_ON_OFF
		
        
	def get_load_power(self):
	### responsible for reading applied power
		return self.load_power
		
	
		
		
	
		
    
        
        
         
      
                
