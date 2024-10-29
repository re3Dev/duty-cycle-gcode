import time
import requests


url = "http://localhost/printer/gcode/script?script=VIB_CYCLE"

def post_gcode():
    try:
        response = requests.post(url)
        if response.status_code == 200:
            print("Successfully sent duty cycle command.")
        else:
            print(f"Failed to send duty cycle command. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

while True:
    post_gcode()
    time.sleep(30)
