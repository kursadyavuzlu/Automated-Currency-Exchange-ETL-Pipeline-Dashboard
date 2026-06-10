import requests
from transform import transform_data

url="https://api.frankfurter.dev/v2/rates"

try:
    response = requests.get(url, timeout=10)
    raw_data = response.json()

    clear_data = transform_data(raw_data)

    print(f"Total processed currency count: {len(clear_data)}")
    print(f"First cleansed data sample: ", clear_data[0])

    print("\n Succesful.")

except requests.exceptions.RequestException as e:
    print("ERROR! : {e}")
