# Observation scheduling on TRT through an API request.

# API address
import requests
import json

url = "https://trt.narit.or.th/hub/api/newobservation"
keep_id = []

#Example for script observation to input parameters
script= dict([("ObjectName", "M32"),                                                                                                 
                ("StationName", "SRO"),                                                                                              
                ("RA", "05:35:17.29"),                                                     
                ("DEC", "-05:23:27.9"),                                                   
                ("BinningXY", "1,1"),                                                                                                
                ("CadenceInterval", "00:00:00"),                                                                                     
                ("MaxAirmass", "3"),                                                                                                 
                ("PA", "0"),                                                                                                         
                ("Dither", "0"),                                                                                                     
                ("ExpiryDate", "2021-07-31 16:11:21"),                                                                            
                ("StartDate", "2021-06-20 16:11:21"),                                                                      
                ("EndDate", "2021-06-26 16:11:21"),                                                                               
                ("ExposuresMode", "1"),                                                                                              
                ("M3Port", "1"),                                                                                                     
                ("Filter", ["B", "V", "R", "I"]),                                                                                    
                ("Suffix", ["{}_B".format(M32),"{}_V".format(M32),"{}_R".format(M32), "{}_I".format(M32)]),      
                ("Exposure", ["120","120","120", "120"]),                                                                            
                ("Repeat", ["5","5","5", "5"])                                                                                       
              ])

# Convert text to Json format
payload = json.dumps({"script": [ script] })
print(payload, "\n")
headers = {
              'Content-Type': 'application/json',
              'TRT': 'your_token'
          }
response = requests.request("POST", url, headers=headers, data=payload)
keep_id.append(response.text)
print(response.text)
