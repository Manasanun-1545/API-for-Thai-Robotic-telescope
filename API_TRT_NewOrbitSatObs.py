import requests
import json

url = "https://trt.narit.or.th/hub/api/neworbitsatobs"

payload = json.dumps({
  "script": [
    {
      "ObjectName": "DELTA 4",
      "StationName": "KKN",
      "TLE1": "1 39534U 14008B   25132.51921871  .00000074  00000-0  00000+0 0  9994",
      "TLE2": "2 39534  53.0347 181.1014 0209915 104.2084 258.2240  1.90803826 78194",
      "Subframe": "3",
      "BinningXY": "1,1",
      "CadenceInterval": "00:00:00",
      "MaxAirmass": "3",
      "PA": "0",
      "Dither": "0",
      "ExpiryDate": "2026-02-25 16:11:21",
      "StartDate": "2025-01-30 16:11:21",
      "EndDate": "2026-02-25 16:11:21",
      "ExposuresMode": "1",
      "M3Port": "1",
      "Filter": [
        "B",
        "U",
        "R"
      ],
      "Suffix": [
        "suffixB",
        "suffixU",
        "suffixR"
      ],
      "Exposure": [
        "3",
        "3",
        "3"
      ],
      "Repeat": [
        "2",
        "2",
        "2"
      ],
      "isQuicklook": "1"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'TRT': 'your token'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
