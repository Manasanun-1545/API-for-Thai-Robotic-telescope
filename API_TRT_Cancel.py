# API Cancellation
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

url = "https://trt.narit.or.th/hub/api/cancelobservation"

payload = json.dumps({
    "obs_id": keep_cid
})
print(payload)

headers = {
  'Content-Type': 'application/json',
  'TRT': 'your_token'
}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
