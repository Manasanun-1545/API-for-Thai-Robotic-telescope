# API Request

The code facilitates observation scheduling on the Thai Robotic Telescope (TRT) through an API request. Here's a breakdown of what it does:

### **1. Import crucial packages**

```python
import requests
import json
```

### **2. API Setup**

```python
url = "Enter Your API address"
keep_id = []
```

- `url` stores the API address for sending requests. Replace it with your personal API. 
(e.g. "http://199.999.9.99:9900/hub/api/newobservation")
- `keep_id` ****is an empty list that will be used to store the id of the observation API response .

### **3. Observation parameters**

`script` is a dictionary containing observation parameters. You can define the parameters, values, and formats in this part.

```python
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
```

| Parameter | Definition | Accepted Input Format |
| --- | --- | --- |
| ObjectName | Target name for observation | object name |
| StationName | Specify TRT observatory | SRO, SBO, or GAO |
| RA | Right Ascension of the object | hh:mm:ss |
| DEC | Declination of the object | dd:mm:ss |
| BinningXY | Binning factor X,Y  | pixels 
 |
| CadenceInterval | Time between exposures | hh:mm:ss |
| MaxAirmass | Maximum airmass allowed for observations | number |
| PA | Position angle | degrees  |
| Dither | Dithering offset | arcsec unit
(0: no dither, 1:3x3, 2:5x5) |
| ExpiryDate | Date and time the observation request expires | ISO format |
| StartDate | Start date and time of the observation | ISO format |
| EndDate | End date and time of the observation | ISO format |
| ExposuresMode | Mode of exposures | number 
(1 : SEQUENCE, 2 : INTERLACED) |
| M3Port | Port number  | number |
| Filter | List of filters | B, V, R, I |
| Suffix | Suffix add to image filenames for each filter | suffix 
(e.g. {}_B, {}_V, {}_R, , {}_I) |
| Exposure | Exposure time for each filter | seconds |
| Repeat | Number of times to repeat each filter observation | number |

### **4. Sending the API request**

```python
payload = json.dumps({"script": [ script] })
print(payload, "\n")
headers = {
              'Content-Type': 'application/json',
              'TRT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDk0MTdhNzQzNzUxYzBmNmNiZGRjMjAiLCJuYW1lIjoiS2FudGhhbmFrb3JuIE5veXNlbmEiLCJncm91cElkIjoxLCJncm91cE5hbWUiOiJyZXNlYXJjaGVyIiwicHJpb3JpdHlJZCI6IjY1OGFjYmJlMDhhYmY2MDI3ODNhMGFjOCIsInByaW9yaXR5Ijo5NSwic3RhcnREYXRlIjoiMjAyNC0wMS0wMVQwMDowMTowMC4wMDBaIiwiZXhwaXJlRGF0ZSI6IjIwMjQtMDQtMzBUMjM6NTk6MDAuMDAwWiIsImlhdCI6MTcwNDk1ODkwMiwiZXhwIjoxNzE0NDYyOTAyfQ.v9bQFhmrThw5sCpD1OAlpHWQa3v_v10EgeIuTxge2yE'
          }
response = requests.request("POST", url, headers=headers, data=payload)
keep_id.append(response.text)
print(response.text)
```

This section describes the process of sending the observation request to the target API:

- Preparing the Request Data
    
    The code transforms your observation parameters stored in `script` into a JSON format, ensuring that the information is readable by the API.
    
- Setting up the Communication Headers:
    
    The headers specify the API request details, including JSON content type and your TRT authentication token. 
    
- Sending the Request:
    
    The request, containing observation parameters and headers, is sent to the API endpoint (URL). The responses are stored in `keep_id` and printed.
    
    ```json
    # Example of the responses
    {"script": [{"ObjectName": "M32", "StationName": "SRO", "RA": "05:35:17.29", "DEC": "-05:23:27.9",
     "Subframe": "1", "BinningXY": "1,1", "CadenceInterval": "00:00:00", "MaxAirmass": "3", "PA": "0", 
     "Dither": "0", "ExpiryDate": "2024-02-20 16:11:21", "StartDate": "2024-02-16 16:11:21",
     "EndDate": "2024-02-17 16:11:21", "ExposuresMode": "1", "M3Port": "1", "Filter": ["B", "V", "R", "I"],
     "Suffix": ["M32_B", "M32_V", "M32_R", "M32_I"], "Exposure": ["120", "120", "120", "120"],
     "Repeat": ["5", "5", "5", "5"]}]}
    ```
    

**Note:** 

- Remember to replace `url` and `TRT` with your API address and authentication token.
- You can adjust the observation parameters, values, and formats in the script.
- View the results on your TRT observation page or through the provided link: https://trt.narit.or.th/observation.
