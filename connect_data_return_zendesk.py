"""
Stella Connect Data Return API
Requires:
    `pip install PyJWT`
    `pip install requests`
Usage:
    Change the API_KEY, SECRET, START_DATE, and END_DATE
    `python stellaconnect_data.py`  
"""
from __future__ import print_function

import datetime

import jwt
import requests
import json

API_KEY = ''
SECRET = ''
START_DATE = datetime.date.today()- datetime.timedelta(days=1)  
END_DATE = datetime.date.today()

ALGORITHM = 'HS256'
BASE_URL = ''
URL = '{}?start_date={}&end_date={}'.format(BASE_URL, START_DATE, END_DATE)

data = {
    'iat': datetime.datetime.now(),
    'exp': datetime.datetime.now() + datetime.timedelta(days=1)
}
token = jwt.encode(data, SECRET, algorithm=ALGORITHM)

headers = {'Authorization': token, 'x-api-key': API_KEY}
response = requests.get(URL, headers=headers)

print(response.status_code)
if response.status_code < 400:
    print(response.json())
else:
    print(response.text)
    exit()
"""
I wrote the bottom portion which takes data returned from Stella Service API and pushes into Zendesk.
I exclude tickets that start with DESK because they are irrevelant and tickets with no interaction ID. All the remaining tickets push
custom field data onto the solved ticket.  Depending on the value of one of the custom fields called
star rating, a new create will be created.
"""

USER = 'user email'+ '/token'
PWD = ''
HEADERS = {'content-type': 'application/json'}

session= requests.Session()
session.auth= (USER, PWD)
session.headers = HEADERS


UPDATE_TKT_URL = 'https://your-subdomain.zendesk.com/api/v2/tickets/'
CREATE_TKT_URL = 'https://your-subdomain.zendesk.com/api/v2/tickets.json'

#create service recovery variables
SUBJECT = 'Service Recovery'
BAD_RATING = [1,2,3]

response_data = response.json()

for feedback in response_data['responses']:
    if feedback['ext_interaction_id'] is None:
        print ('Manual request no interaction ID')
    elif 'DESK' in feedback['ext_interaction_id']:
        print ('DESK Request')
    else:
        star_rating = feedback['star_rating']
        comments = feedback['comments']
        tkt_id = feedback['ext_interaction_id']
        url =  UPDATE_TKT_URL + tkt_id + '.json'
        data = {'ticket': {'custom_fields': [{'id': YOUR_STAR_RATING_FIELD_ID, 'value': star_rating}, {'id': YOUR_COMMENTS_FIELD_ID, 'value': comments}]}}
        payload = json.dumps(data)
        response = session.put(url, data=payload)
        # Check response
        if response.status_code != 200:
            print('Status:', response.status_code, tkt_id)
            print(response.text)
        else:
            print('Successfully updated ticket#{}'.format(tkt_id))
        #create a service recovery ticket in Zendesk if star rating is 3, 2, 1
        if star_rating in BAD_RATING:
            initial_request_id = feedback['request_id']
            tkt_body = 'Ticket #{} received a star rating of {} with these comments: {}'.format(tkt_id, star_rating, comments)
            data = {'ticket': {'subject': SUBJECT, 'comment': {'body': tkt_body} , 'custom_fields': [{'id': YOUR_REQUEST_ID_FIELD_ID, 'value': initial_request_id}]}}
            payload = json.dumps(data)
            response = session.post(CREATE_TKT_URL, data=payload)
            #check response
            if response.status_code != 201:
                print('Status:', response.status_code)
                print(response.text)
            else:
                print('Successfully created service recovery ticket for ticket#{}'.format(tkt_id))
           
   
 