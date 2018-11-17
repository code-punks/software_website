import requests
import json

def main():

    s=requests.Session()
    q = s.get('http://192.168.43.140:8000/api/api-auth/login')
    if 'csrftoken' in s.cookies:
        csrftoken = s.cookies['csrftoken']
    else:
        csrftoken = s.cookies['csrf']
    payload = {'username': 'admin', 'password': 'bhavay123','csrfmiddlewaretoken': csrftoken,'next':''}
    s.post('http://192.168.43.140:8000/api/api-auth/login/',data=payload, headers=dict(Referer='http://192.168.43.140:8000/api/api-auth/login/'))
    data = s.get('http://192.168.43.140:8000/api/assignrfid')
    d = json.loads(data.content)
    for i in range(1,len(d)):
        user_link = d[i]['user']
        req = s.get(user_link)
        user_data = json.loads(req.content)
        user_id = user_data['id']
        user_name = user_data['username']
        link  = "http://192.168.43.140:8000/api/assignrfid/" + str(user_id) + "/"
        query =  {
            # "csrfmiddlewaretoken": csrftoken,
            "url": link,
            "user": user_link,
            "rfid": "123456"
        }
        print("haan bhaiya")
        response = s.put(link,data = query,headers = {"Content-Type": "application/json"})
        print(response.text)
if __name__ == '__main__':
    main()