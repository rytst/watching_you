import requests



def send_line(token, msg):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': msg}


    # POST with parameter
    r = requests.post(url, headers=headers, params=payload)

