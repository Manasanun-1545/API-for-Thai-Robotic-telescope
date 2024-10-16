import requests

url = "https://trt.narit.or.th/hub/api/checkbalance"

payload = ""
headers = {
  'TRT': 'your_token'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
