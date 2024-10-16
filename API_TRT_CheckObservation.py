import requests
import json

url = "https://trt.narit.or.th/hub/api/checkobservation"

payload = json.dumps({
  "obs_id": [
    "24ZKUG_1",
    "24YP9X_1",
    "24F6P5_1"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'TRT': 'your_token'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
