from os import access
import requests
import json
import time
import os
from version2 import read_string
from detect import detect_export
import _thread
from threading import Thread

# def send_data(img, action,vehicleCode):
#     files = {
#         'file': (img, open(img, 'rb'), 'image/jpg')
#     }
#     data = {
#         'vehicleCode': vehicleCode
#     }
#
# 	# url = 'https://c214-171-241-81-206.ap.ngrok.io/'
#     url_api = 'https://def7-171-241-81-206.ap.ngrok.io/api/v1/data/' + action
#     res = requests.post(url_api, files = files, data = data)
#     try:
#         data = res.json()
#         status_code = res.status_code
#         print('response data:', data, ', status code:', status_code)
#     except requests.exceptions.RequestException:
#         print('response text:', res.text)

directory = "runs\detect\exp2\crops\licence-plate"


# for filename in os.listdir(directory):
#     print(filename)
#     imagePath = os.path.join(directory,filename)
#     number = read_string(imagePath)
#     print(number)
#     # send_data(imagePath, 'in', number)
#send_data(imagePath, 'out', text)
# imagePath = os.path.join(directory,filename)

img_path = os.path.join(directory,'vehicle.jpg')

# _thread.start_new_thread(detect_export,())
# _thread.start_new_thread(read_string,(img_path,))
#_thread.start_new_thread(send_data(img_path,'in',read_string(img_path)))

thread = Thread(target= detect_export)
thread2 = Thread(target= read_string)
thread.start()
thread2.start()
thread.join()
thread2.join()
print('Finished')
