#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:20:23 2018
@author: XXXXXXX
"""

import http.client

conn = http.client.HTTPSConnection("api.somedomain.net")

payload = "{\"do_not_send\":false,\"tags\":[\"compensation provided\"],\"employee\":{\"email\":\"email address\"},\"initial_feedback_request_id\":\"your-initial-request-id\",\"ext_interaction_id\":\"your-ext-interaction-id\",\"external_url\":\"https://your-crm.your-source-system.com/cases/your-case-id\"}"

headers = {
    'accept': "application/json",
    'x-api-key': "",
    'content-type': "application/json"
    }

conn.request("POST", "/v1/recoveries", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
