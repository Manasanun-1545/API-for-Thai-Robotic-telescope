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
url = "Enter your API address"

payload = json.dumps({
    "obs_id": keep_cid
})
print(payload)

headers = {
  'Content-Type': 'application/json',
  'TRT': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZDk0MTdhNzQzNzUxYzBmNmNiZGRjMjAiLCJuYW1lIjoiS2FudGhhbmFrb3JuIE5veXNlbmEiLCJncm91cElkIjoxLCJncm91cE5hbWUiOiJyZXNlYXJjaGVyIiwicHJpb3JpdHlJZCI6IjY1OGFjYmJlMDhhYmY2MDI3ODNhMGFjOCIsInByaW9yaXR5Ijo5NSwic3RhcnREYXRlIjoiMjAyNC0wMS0wMVQwMDowMTowMC4wMDBaIiwiZXhwaXJlRGF0ZSI6IjIwMjQtMDQtMzBUMjM6NTk6MDAuMDAwWiIsImlhdCI6MTcwNDk1ODkwMiwiZXhwIjoxNzE0NDYyOTAyfQ.v9bQFhmrThw5sCpD1OAlpHWQa3v_v10EgeIuTxge2yE'
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

- Remember to replace `url` and `TRT` with your API address and authentication token.
- View the results on your TRT observation page or through the provided link: https://trt.narit.or.th/observation.
