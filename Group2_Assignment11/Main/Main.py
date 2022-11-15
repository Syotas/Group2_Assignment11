'''
Created on Nov 15, 2022

@author: syota
'''

import http.client

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "441570b6afmshf8d0f3900be8b61p13d10ejsnf93880368108"
    }

conn.request("GET", "/teams?id=1", headers=headers)

res = conn.getresponse()
data = res.read()

print(data)