#pi_blackbox_server/test_server.py

import os
import unittest

from bb_server import app

class ServerTest(unittest.TestCase):
    ### SETUP ###

    ### Gets run before every test 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        pass

    def TearDown(self):
        pass

    ### TESTS ###
        #test get to main page
    def test_index_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Pi Blackbox")
 
        #test GET motor state
    def test_get_motor_state(self):
        response = self.app.get('/motorstate', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Motor State 1")
        self.assertTrue("Motor State" in response.data)

       #test PUT motor state
    def test_put_motor_state(self):
        response = self.app.put('/motorstate/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200) # 405 means method not available
        get_response = self.app.get('/motorstate', follow_redirects=True)
        self.assertEqual(get_response.data, 'Motor State 1')
        
        #test load settings
    def test_put_motor_load(self):
        response = self.app.put('/loadpower', follow_redirects = True) 
        #self.assertEqual(response.data, '30')    
        self.assertEqual(response.status_code, 405) 
        
        
        
        #response = self.app.get('/loadpower', follow_redirects = True)
        #print response.data 
        #self.assertEqual(response.data, '30')               
        #self.assertEqual(response.status_code, 200)
        
        #get test report  
    def test_load_path_get(self):
        response = self.app.get('/performanceData/report', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
     
        #get test report  
    #def test_get_report(self):
        #response = self.app.get('/performanceData/report', follow_redirects = True)
        #print response.data                
        #self.assertEqual(response.status_code, 200)
        
        
        
        
    #test Put motor pin number
    #def test_cant_put_motor_pin(self):
        #response = self.app.put('/motorpin/1', follow_redirects=True)
        #self.assertEqual(response.status_code, 200)
        #get_response = self.app.get('/motorpin', follow_redirects=True)
        #self.assertEqual(get_response.data, 'GPIO pin # 2') 
        
             #test motor state 
    #def test_cant_get_motor_state_int(self):
        #response = self.app.get('/motorstate/1', follow_redirects=True)
        #self.assertEqual(response.status_code, 405) # 405 means method not available 
        
    
    
    
### Tests we need ###
# get Load Settings -- OK###
# Get log file location OK###
# get performance data OK###

# Put motor pin number
# put load setting
# put log status


if __name__ == "__main__":
    unittest.main()
