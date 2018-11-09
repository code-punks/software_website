import sys
import requests

URL = 'http://127.0.0.1:8000/assign_rfid'

client = requests.session()

# Retrieve the CSRF token first
client.get(URL)  # sets cookie
print(client.cookies)
if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    csrftoken = client.cookies['csrftoken']
else:
    # older versions
    csrftoken = client.cookies['csrf']

post_data = dict(csrfmiddlewaretoken=csrftoken,custom_0 = 1234 ,custom_1 = 1234)
r = client.post(URL, data=post_data, headers=dict(Referer=URL))