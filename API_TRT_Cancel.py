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
