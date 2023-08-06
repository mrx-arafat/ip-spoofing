
# -*- coding: utf-8 -*-
 
import requests
 
reponse = requests.get(
    'http://challenge01.root-me.org/web-serveur/ch68/',
    headers={'Client-IP': '192.168.1.103'}
    )
 
if reponse.status_code == 200:
    print(reponse.text)
else:
    print('Error')