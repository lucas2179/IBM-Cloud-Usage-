#
#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
#
import sys
import json
import requests
import ibm_boto3
def main(dict):
    api_key = dict['cos-apikey']
    service_instance_id = dict['siid']
    auth_endpoint = "https://iam.cloud.ibm.com/identity/token"
    service_endpoint = dict['endpoint']
    cos = ibm_boto3.client('s3',
        	ibm_api_key_id=api_key,
        	ibm_service_instance_id=service_instance_id,
        	ibm_auth_endpoint=auth_endpoint,
        	config=Config(signature_version='oauth'),
        	endpoint_url=service_endpoint)







    authorization = 'Bearer '+ dict['token']
    url = 'https://billing.cloud.ibm.com/v4/accounts/'+dict['account_id']+'/resource_instances/usage/'+dict['month']
    headers = {
        'accept': 'application/json',
        'Authorization': authorization
    } 
    response = requests.get(url, headers=headers)
    print(response.text)
    resp = json.loads(response.text)
    with open('data.json', 'w') as outfile:
        json.dump(resp, outfile)

    cos.upload_file('data.json',dict['bucket'],'data.json')
    return resp
