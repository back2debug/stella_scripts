import requests
import numpy as np
import pandas as pd
from time import time
from IPython.display import display # Allows the use of display() for DataFrames

# Load the scoring dataset
data = pd.read_csv("stellainputs.csv")

# Success - Display the first record
# display(data.head(n=1))

url = 'https://api.stellaconnect.net/v1/requests'
headers = {
    'x-api-key': '',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

for index, row in data.iterrows():
    payload = {
        'customer': {
        'name': row["Customer Name"],
        'email': row["Customer's Email Address"]  # required
    },
    'employee': {
        'custom_id': row["Agent Email"]  # custom_id or email required
    },
    'do_not_send': False,
    'tags': [''],  #['billing question', 'vip']
    'country': 'US',
    'brand': '',  # multibrand only
    'channel': row["Channel"],  # phone, email, or chat and required
    'ext_interaction_id': row["SR Number"], #SR number
#'external_url': 'https://crm.dell.com/case/12345678',
    }
    
    # Print the entries for debug purposes
    print ("Customer Name")
    print ("Customer's Email Address")
    print ("Agent Email")
    print ("Channel")
    print ("SR Number")
    
    r = requests.post(url, headers=headers, json=payload)
    assert r.status_code == 200
    print (r.json())  # returns request_id