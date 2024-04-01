# API Request
<h4>Thank you Pathompong, our developer team at NARIT</h4>
You can request token from : <html>https://trt.narit.or.th/script</html>, however you must have account and proposal approval.
The code facilitates observation scheduling on the Thai Robotic Telescope (TRT) through an API request. Here's a breakdown of what it does:

You can check the schedule for each telescope and its status with
https://trt.narit.or.th/hub/api/checkobservation

For creating new observation, must use this url</br>
url = "https://trt.narit.or.th/hub/api/newobservation"

For cancellation, must use this url
url = "https://trt.narit.or.th/hub/api/cancelobservation"

### **1. Import crucial packages**

```python
import requests
import json
```

### **2. API Setup**

```python

# use for create new observation  
url = "https://trt.narit.or.th/hub/api/newobservation"

keep_id = []
```

- `url` stores the API address for sending requests.
- `keep_id` ****is an empty list that will be used to store the id of the observation API response.

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
| BinningXY | Binning factor X,Y  | pixels |
| CadenceInterval | Time between exposures | hh:mm:ss |
| MaxAirmass | Maximum airmass allowed for observations | number |
| PA | Position angle | degrees  |
| Dither | Dithering offset | arcsec unit (0: no dither, 1:3x3, 2:5x5) |
| ExpiryDate | Date and time the observation request expires | ISO format |
| StartDate | Start date and time of the observation | ISO format |
| EndDate | End date and time of the observation | ISO format |
| ExposuresMode | Mode of exposures | number (1 : SEQUENCE, 2 : INTERLACED) |
| M3Port | Port number  | number |
| Filter | List of filters | B, V, R, I |
| Suffix | Suffix add to image filenames for each filter | suffix (e.g. {}_B, {}_V, {}_R, , {}_I) |
| Exposure | Exposure time for each filter | seconds |
| Repeat | Number of times to repeat each filter observation | number |

### **4. Sending the API request**

```python
payload = json.dumps({"script": [ script] })
print(payload, "\n")
headers = {
              'Content-Type': 'application/json',
              'TRT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDk0MTdhNzQzNzUxYzBmNmNiZGRjMjAiLCJuYW1lIjoiS2FudGhhbmFrb3JuIE5veXNlbmEiLCJncm91cElkIjoxLCJncm91cE5hbWUiOiJyZXNlYXJjaGVyIiwicHJpb3JpdHlJZCI6IjY1OGFjYmJlMDhhYmY2MDI3ODNhMGFjOCIsInByaW9yaXR5Ijo5NSwic3RhcnREYXRlIjoiMjAyNC0wMS0wMVQwMDowMTowMC4wMDBaIiwiZXhwaXJlRGF0ZSI6IjIwMjQtMDQtMzBUMjM6NTk6MDAuMDAwWiIsImlhdCI6MTcwNDk1ODkwMiwiZXhwIjoxNzE0NDYyOTAyfQ.v9bQFhmrThw5sCpD1OAlpHWQa3v_v10EoiPuTxge2yE'
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

- Remember to replace `TRT` with your authentication token.
- You can adjust the observation parameters, values, and formats in the script.
- View the results on your TRT observation page or through the provided link: https://trt.narit.or.th/observation.


# API Cancellation

**1. Saving Observation IDs to ASCII Text**

This code stores observation IDs in an ASCII text file to comply with API requirements for data format because if you use ‘keep_id’ directly, the format of the ID will not match to use with API requirements.

```python
# Saving observation IDs to ASCII Text
file_to_write = "obs_id.txt"
file = open(file_to_write, 'w')
for i in keep_id:
    txt = i.replace('[', '').replace(']', '').replace('"', '')
    file.write(txt+"\n")
 file.close()

# Reading IDs from ASCII Text
rfile = open(file_to_write, 'r')
txt = rfile.read()
rfile.close()
print(txt.rsplit())

# Splitting IDs
keep_cid = txt.rsplit()
```

**2. API Cancellation**

```python
url = "https://trt.narit.or.th/hub/api/cancelobservation"

payload = json.dumps({
    "obs_id": keep_cid
})
print(payload)

headers = {
  'Content-Type': 'application/json',
  'TRT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDk0MTdhNzQzNzUxYzBmNmNiZGRjMjAiLCJuYW1lIjoiS2FudGhhbmFrb3JuIE5veXNlbmEiLCJncm91cElkIjoxLCJncm91cE5hbWUiOiJyZXNlYXJjaGVyIiwicHJpb3JpdHlJZCI6IjY1OGFjYmJlMDhhYmY2MDI3ODNhMGFjOCIsInByaW9yaXR5Ijo5NSwic3RhcnREYXRlIjoiMjAyNC0wMS0wMVQwMDowMTowMC4wMDBaIiwiZXhwaXJlRGF0ZSI6IjIwMjQtMDQtMzBUMjM6NTk6MDAuMDAwWiIsImlhdCI6MTcwNDk1ODkwMiwiZXhwIjoxNzE0NDYyOTAyfQ.v9bQFhmrThw5sCpD1OAlpHWQa3v_v10EgeIuTxge3ui'
}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

**Setting up the request**

- `url`**:** enter URL of the API address.
- `headers`: define content type and TRT authentication token in header.
- `payload = json.dumps({"obs_id": keep_cid})`
    - Construct a JSON data structure with an `obs_id` key set to the value of the `keep_cid` variable. This variable contains an identifier from a previous API response.
    - To cancel specific observations, include their corresponding `obs_id` values in the request.
        
        ```python
        payload = json.dumps({
            "obs_id": ["24ZKUG_1", "24YP9X_1", "24F6P5_1", "24WCZG_1", "24P14I_1"]
        })
        ```
        

**Sending the request**

The code utilizes the `requests` library to send a POST request to the API. POST signifies the HTTP method employed for creating or modifying data.

**Note:**

- Remember to replace `TRT` with your authentication token.
- View the results on your TRT observation page or through the provided link: https://trt.narit.or.th/observation.
