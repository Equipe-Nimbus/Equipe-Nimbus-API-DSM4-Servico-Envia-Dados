import requests
import time
import random

def send_data():
    url = "http://localhost:8001/medicao/guardar"
    headers = {'Content-Type': 'application/json'}

    while True:
        
        data = {
            "uuid": "ioenfiono43737bwfibfw9i8b",
            "unix": int(time.time()),
            "bateria": random.randint(1, 100),
            "vel_vento": random.randint(0, 100),
            "temperatura": random.randint(-30, 50)
        }

        response = requests.post(url, json=data, headers=headers)

        print(response.status_code)
        
        if response.text:
            print(response.json())
        else:
            print("No response body")

        time.sleep(5)

if __name__ == "__main__":
    send_data()