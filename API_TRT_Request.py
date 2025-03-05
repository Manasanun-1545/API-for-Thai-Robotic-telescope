import requests
import json

url = "https://trt.narit.or.th/hub/api/newobservation"

payload = json.dumps({
  "script": [
    {
      "ObjectName": "M53",
      "StationName": "SRO",
      "RA": "13:12:55.24",
      "DEC": "+18:10:05.4",
      "Subframe": "3",
      "BinningXY": "1,1",
      "CadenceInterval": "00:00:00",
      "MaxAirmass": "3",
      "PA": "0",
      "Dither": "1",
      "ExpiryDate": "2025-02-25 16:11:21",
      "StartDate": "2025-01-30 16:11:21",
      "EndDate": "2025-02-24 16:11:21",
      "ExposuresMode": "1",
      "M3Port": "1",
      "Filter": [
        "B",
        "V",
        "R"
      ],
      "Suffix": [
        "suffixB",
        "suffixV",
        "suffixR"
      ],
      "Exposure": [
        "6",
        "6",
        "6"
      ],
      "Repeat": [
        "6",
        "6",
        "6"
      ],
      "isQuicklook": "1"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'TRT': 'yourtoken'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
