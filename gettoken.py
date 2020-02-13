#
#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
#
import json
import sys
import requests
def main(dict):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        
    }
    data = {
      'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
      'apikey': dict['apikey']
    }
    response = requests.post('https://iam.cloud.ibm.com/identity/token/', headers=headers, data=data, verify=True)
    print(response.__getattribute__('content'))
    content = response.__getattribute__('content')
    content = json.loads(content)
    
    dict['token'] = content['access_token']
    return dict
