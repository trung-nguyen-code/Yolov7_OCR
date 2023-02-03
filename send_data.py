import requests
import json
import os


def send_data(img_path, action, vehicle_code):
    root = './'
    path = os.path.join(root, img_path)
    files = {
        'file': (path, open(path, 'rb'), 'image/jpg')
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


def check_vehicle_code_format(vehicle_code: str):
    vehicle_code = vehicle_code.replace(
        '-', '').replace('.', '').rstrip().lstrip().strip()
    vehicle_len = len(vehicle_code)
    if vehicle_len == 8 or vehicle_len == 9:
        return True
    return False
