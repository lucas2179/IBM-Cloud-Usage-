import sys
import json
import requests
import ibm_boto3
from ibm_botocore.client import Config
import pandas as pd
from datetime import date

def main(dict):






    month = str(date.today())[:-3]
    authorization = 'Bearer '+ dict['token']
    url = 'https://billing.cloud.ibm.com/v4/accounts/'+dict['account_id']+'/resource_instances/usage/'+month+'?_names=true'
    headers = {
        'accept': 'application/json',
        'Authorization': authorization
    } 
    response = requests.get(url, headers=headers)
    print(dir(response))
    # print(response.text)
    resp = json.loads(response.text)
    with open('data.json', 'w') as outfile:
        json.dump(resp, outfile)

    # cos.upload_file('data.json',dict['bucket'],'data.json')
    dict['usage'] = resp
    return dict
