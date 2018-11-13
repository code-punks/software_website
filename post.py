import requests
import json

def main():
    #req = requests.get('http://127.0.0.1:8000/api/users/')
    # print("HTTP Status Code: " + str(req.status_code))
    # print(req.headers)
    # json_response = json.loads(req.content)
    # print("Pokemon Name: " + json_response['name'])

    query={'rfid':'12345'}
    req = requests.get('http://127.0.0.1:8000/api/profiles/', params=query)
    response = json.loads(req.content)
    
    user_url = response[0]['user']

    req = requests.get(user_url)
    user_id = json.loads(req.content)['id']
    print(user_id)
if __name__ == '__main__':
    main()