# Thai Robotic Telescope (TRT) API Documentation

You can request <b>"token"</b> from: https://trt.narit.or.th/script

**Note:** You must have an account and proposal approval to obtain a token.

---

## Available API Endpoints

| Purpose | URL |
| --- | --- |
| Check your credit balance | `https://trt.narit.or.th/hub/api/checkbalance` |
| Create new observation | `https://trt.narit.or.th/hub/api/newobservation` |
| Create new satellite observation with TLE* | `https://trt.narit.or.th/hub/api/neworbitsatobs` |
| Cancel observation | `https://trt.narit.or.th/hub/api/cancelobservation` |
| Check your observation | `https://trt.narit.or.th/hub/api/checkobservation` |
| Check dome status | `https://trt.narit.or.th/hub/api/checkdome` |
| Check all observations by observatory | `https://trt.narit.or.th/hub/api/queuemonitor` |
| Get your files | `https://trt.narit.or.th/hub/api/getfilepath` |

**Available for some observatory only*

---

## Creating New Observation

### Standard Format

```python
import requests
import json

url = "https://trt.narit.or.th/hub/api/newobservation"

payload = json.dumps({
  "script": [
    {
      "ObjectName": "M33",
      "StationName": "SBO",
      "RA": "13:12:55.24",
      "DEC": "+18:10:05.4",
      "Subframe": "3",
      "BinningXY": "1,1",
      "CadenceInterval": "00:00:00",
      "MaxAirmass": "3",
      "PA": "",
      "Dither": "1",
      "ExpiryDate": "",
      "StartDate": "",
      "EndDate": "",
      "ExposuresMode": "1",
      "M3Port": "1",
      "Filter": [
        "Z",
        "U",
        "R"
      ],
      "Suffix": [
        "suffixZ",
        "suffixU",
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
      "isQuicklook": "0"
    }
  ]
})

headers = {
  'Content-Type': 'application/json',
  'TRT': 'YOUR_TOKEN_HERE'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

---

## Parameter Reference

### Required Parameters

| Parameter | Description | Format | Example |
| --- | --- | --- | --- |
| `ObjectName` | Target name for observation | String | `"M33"` |
| `StationName` | TRT observatory | `SRO`, `SBO`, `GAO`, `CTO` | `"SBO"` |
| `RA` | Right Ascension | `hh:mm:ss.ss` | `"13:12:55.24"` |
| `DEC` | Declination | `±dd:mm:ss.s` | `"+18:10:05.4"` |
| `Subframe` | Subframe setting | Number (string) | `"3"` |
| `BinningXY` | Binning factor X,Y | `"X,Y"` | `"1,1"` |
| `CadenceInterval` | Time between exposures | `hh:mm:ss` | `"00:00:00"` |
| `MaxAirmass` | Maximum airmass allowed | Number (string) | `"3"` |
| `Dither` | Dithering pattern | `0` = no dither<br>`1` = 3×3<br>`2` = 5×5 | `"1"` |
| `ExposuresMode` | Exposure mode | `1` = SEQUENCE<br>`2` = INTERLACED | `"1"` |
| `M3Port` | Mirror port number | Number (string) | `"1"` |
| `Filter` | List of filters to use | Array of strings | `["Z", "U", "R"]` |
| `Suffix` | Filename suffix for each filter | Array of strings | `["suffixZ", "suffixU", "suffixR"]` |
| `Exposure` | Exposure time (seconds) for each filter | Array of numbers (string) | `["6", "6", "6"]` |
| `Repeat` | Number of repeats for each filter | Array of numbers (string) | `["6", "6", "6"]` |
| `isQuicklook` | Enable quicklook mode | `0` = disabled<br>`1` = enabled | `"0"` |

### Optional Parameters

| Parameter | Description | Format | Example | Notes |
| --- | --- | --- | --- | --- |
| `PA` | Position angle (degrees) | Number (string) or empty | `"45"` or `""` | Use `""` if not specified |
| `ExpiryDate` | Observation request expiry date | ISO format or empty | `"2026-02-25 16:11:21"` or `""` | Use `""` if not specified |
| `StartDate` | Observation start date | ISO format or empty | `"2026-01-19 04:11:21"` or `""` | Use `""` if not specified |
| `EndDate` | Observation end date | ISO format or empty | `"2026-01-20 16:11:21"` or `""` | Use `""` if not specified |

### Available Filters

Filters may vary by observatory. Common filters include:
> **Note:** Filters available at each observatory may differ. Please check the specific filters available on the TRT website for your chosen observatory before planning your observations.
- `B` - Blue
- `V` - Visual
- `R` - Red
- `I` - Infrared
- `Z` - Z-band
- `U` - Ultraviolet
---




## Usage Examples

### Example 1: Basic Observation (No Optional Parameters)

```python
import requests
import json

url = "https://trt.narit.or.th/hub/api/newobservation"

payload = json.dumps({
  "script": [
    {
      "ObjectName": "NGC1234",
      "StationName": "SRO",
      "RA": "05:35:17.29",
      "DEC": "-05:23:27.9",
      "Subframe": "1",
      "BinningXY": "1,1",
      "CadenceInterval": "00:00:00",
      "MaxAirmass": "2",
      "PA": "",
      "Dither": "0",
      "ExpiryDate": "",
      "StartDate": "",
      "EndDate": "",
      "ExposuresMode": "1",
      "M3Port": "1",
      "Filter": ["B", "V", "R", "I"],
      "Suffix": ["B_filter", "V_filter", "R_filter", "I_filter"],
      "Exposure": ["120", "120", "120", "120"],
      "Repeat": ["5", "5", "5", "5"],
      "isQuicklook": "0"
    }
  ]
})

headers = {
  'Content-Type': 'application/json',
  'TRT': 'YOUR_TOKEN_HERE'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```

### Example 2: With Date/Time Constraints and Position Angle

```python
import requests
import json

url = "https://trt.narit.or.th/hub/api/newobservation"

payload = json.dumps({
  "script": [
    {
      "ObjectName": "M31",
      "StationName": "SBO",
      "RA": "00:42:44.33",
      "DEC": "+41:16:09.4",
      "Subframe": "2",
      "BinningXY": "2,2",
      "CadenceInterval": "00:10:00",
      "MaxAirmass": "3",
      "PA": "90",
      "Dither": "1",
      "ExpiryDate": "2026-03-31 23:59:00",
      "StartDate": "2026-02-01 18:00:00",
      "EndDate": "2026-02-28 23:59:00",
      "ExposuresMode": "2",
      "M3Port": "1",
      "Filter": ["R", "I"],
      "Suffix": ["R_band", "I_band"],
      "Exposure": ["180", "180"],
      "Repeat": ["10", "10"],
      "isQuicklook": "1"
    }
  ]
})

headers = {
  'Content-Type': 'application/json',
  'TRT': 'YOUR_TOKEN_HERE'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```
---

## SSL Certificate Issues

If your system cannot verify the SSL certificate of the API, here are ways to fix it:

### Option 1: Update SSL Certificates (Recommended)
Check and update your system's CA certificates.

### Option 2: Bypass SSL Verification (Not Recommended)

```python
response = requests.post(url, json=payload, verify=False)
```

**Warning:** Bypassing SSL verification is not recommended for production environments as it reduces security.

---

## Important Notes

1. **Authentication Token**: Always replace `'YOUR_TOKEN_HERE'` with your actual authentication token obtained from https://trt.narit.or.th/script

2. **Optional Parameters**: The following parameters can be left as empty strings `""` if not needed:
   - `PA` (Position Angle)
   - `ExpiryDate`
   - `StartDate`
   - `EndDate`

3. **Array Lengths**: Make sure the arrays for `Filter`, `Suffix`, `Exposure`, and `Repeat` have the same length.

4. **Date Format**: Use ISO format for dates: `YYYY-MM-DD HH:MM:SS`

5. **Monitor Observations**: View your observations at https://trt.narit.or.th/observation

6. **API Response**: The API will return observation IDs upon successful submission. Store these IDs if you need to cancel observations later.

---

## Common Error Troubleshooting

| Error | Possible Cause | Solution |
| --- | --- | --- |
| Authentication Error | Invalid or expired token | Request a new token from https://trt.narit.or.th/script |
| Invalid Format | Incorrect JSON structure | Verify payload matches standard format |
| Array Length Mismatch | Filter, Suffix, Exposure, Repeat arrays have different lengths | Ensure all arrays have the same length |
| SSL Certificate Error | System cannot verify SSL certificate | Update CA certificates or use verify=False (not recommended) |
| Invalid Station Name | Station name not recognized | Use only: SRO, SBO, GAO, CTO|

---

## Additional Resources

- **Request Token**: https://trt.narit.or.th/script
- **View Observations**: https://trt.narit.or.th/observation
- **Support**: Contact trt_operation@narit.or.th

---

**Last Updated**: January 2026

**Version**: 2.0
