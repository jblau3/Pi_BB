import json

class PerfRPT():
        
        def __init__(self):
               self.path = "C:\Temp\PerfData.txt"  
                	
        def set_path(self, path):
        ### responsible for getting the path
                path = self.path
		print "Setting path of log file %s"%path
		#self.path = path
        
        def get_path(self):
        ### responsible for reading the path
		return self.path         
        
        def set_perfRPT(self, perfRPT):
        ### responsible for getting performance data
                print "Getting performace report %s"%perfRPT
                self.perfRPT = perfRPT
        
        def get_perfRPT(self):
        ### responsible for reading the performance report
                report = {
                     "motor voltage": 23432145,
                     "load current": 15,
                     "motor current": 5,
                 }                 
        # Convert into json
                jsonReport = json.dumps(report)                   
                return jsonReport
        
