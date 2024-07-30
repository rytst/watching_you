import requests



def send(token, msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': msg}



    # POST with parameter
    requests.post(url, headers=headers, params=payload)

