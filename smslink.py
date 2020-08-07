import requests
from requests.auth import HTTPBasicAuth
import json


url = "https://secure.smslink.ro/sms/gateway/communicate/index.php"
params = {'connection_id':'Your Conection ID',
           'password' : 'Your Password',
            'to'      : '01234567',
            'message' : 'Your Message'
          }
r = requests.get(url = url, params = params)
print(r.text)
print(r.status_code)
