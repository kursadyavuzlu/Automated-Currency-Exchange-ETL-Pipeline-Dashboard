import requests

url="https://api.frankfurter.dev/v2/rates"

#response = requests.get(url, timeout=10)

#if response.status_code == 200:
#    print(response.json())
#else:
#    print("FAIL REQUEST, Status Code: {response.status_code}")

try:
    response = requests.get(url, timeout=10)
    print(response.json())
    print("\n Succesful.")
except requests.exceptions.RequestException as e:
    print("ERROR! : {e}")


