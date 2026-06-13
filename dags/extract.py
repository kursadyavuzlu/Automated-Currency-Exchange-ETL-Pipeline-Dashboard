import requests

def extract_data():
    url = "https://api.frankfurter.dev/v2/rates"
    
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"API Hatası! Status Code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"ERROR! : {e}")
        return None
