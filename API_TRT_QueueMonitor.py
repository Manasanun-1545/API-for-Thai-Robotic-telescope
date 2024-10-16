import requests
import json

url = "https://trt.narit.or.th/hub/api/queuemonitor"

payload = json.dumps({
  "station": "SBO"
})
headers = {
  'Content-Type': 'application/json',
  'TRT': 'your_token'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
