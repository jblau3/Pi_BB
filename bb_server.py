from flask import Flask
from hardware import Hardware
from perfRPT import PerfRPT

app = Flask(__name__)  

hardware = Hardware()
perfRPT = PerfRPT()

hardware.set_motorPin(1)
hardware.set_motor_state(0)
hardware.set_motor_power(10)

perfRPT.set_path("pathA")
perfRPT.set_perfRPT("perfReport")
perfRPT.get_path()

 
#open the log file
f = open("logFile.txt", "a") 
f.write("\n Motor state is %i"%(hardware.get_motor_state())) 
f.write("\n The power has been set to %i"%(hardware.get_load_power()))
f.close()
  
@app.route("/")
def index():
    return "Pi Blackbox"
    
 ## MOTOR GET STATE
@app.route("/motorstate", methods=['GET'])
def motor_state_get():     
    return "Motor State %i"%(hardware.get_motor_state())  # we have work to do here. 
    
 ## MOTOR GET POWER
@app.route("/motorpower", methods=['GET'])
def motor_power_get():     
    return "Motor State %f"%(hardware.get_motor_power())  # we have work to do here. 
    
 ## MOTOR PUT STATE
@app.route("/motorstate/<int:state>", methods=['PUT'])
def motor_state_put(state):
   hardware.set_motor_state(state)
   return str(state)
    
 ## MOTOR PUT GPIO PIN
@app.route("/motorPin/<int:pinNumber>", methods=['PUT'])
def set_motorPin(motorPin):
    perfRPT.set_motorPin(motorPin)
    return str(motorPin)   
   
 ##BEGIN LOAD RESISTOR....................................................................... 
    
 ## LOAD RESISTOR POWER     
@app.route("/loadpower/<int:powerSetting>", methods=['PUT'])
def put_load_power(powerSetting):
    hardware.set_heat_power(powerSetting)
    return str(powerSetting)   
    #return report
    
    
 ## LOAD RESISTOR POWER GET
@app.route("/loadpower", methods=['GET'])
def get_load_power():
    load = hardware.get_load_power()
    return str(load)
      
## BEGIN REPORT PATH 
#@app.route("/performanceData/report", methods=['GET'])
#def get_report():
    #return str report()

@app.route("/performanceData/report", methods=['GET'])
def load_path_get():
    return "The file location is %s"%(perfRPT.get_path())  # we have work to do here.        



if __name__ == "__main__":
    app.run()


        
