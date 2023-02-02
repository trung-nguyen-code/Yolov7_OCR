import requests
import json
import os


def send_data(img_path, action, vehicle_code):
    files = {
        'file': (img_path, open(img_path, 'rb'), 'image/jpg')
    }
    data = {
        'vehicleCode': vehicle_code
    }

    server_url = 'http://35.240.201.34'
    url_api = server_url + '/api/v1/data/' + action
    res = requests.post(url_api, files=files, data=data)
    try:
        data = res.json()
        status_code = res.status_code
        print('response data:', data, ', status code:', status_code)
    except requests.exceptions.RequestException:
        print('response text:', res.text)

def check_vehicle_code_format(vehicle_code):
    pass