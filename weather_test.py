import requests
headers = {"token": "YOUR_TOKEN_HERE"} # Replace!
try:
    r = requests.get('https://www.ncei.noaa.gov/cdo-web/api/v2/datasets', headers=headers)
    r.raise_for_status() # Will raise error for 4xx/5xx
    print("Token seems to work for basic calls. Received datasets:", r.json())
except requests.exceptions.RequestException as e:
    print("Token might be invalid or API is down even for basic calls:", e)
    if r is not None: print(f"Status Code: {r.status_code}")