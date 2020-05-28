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
import pandas as pd
import ibm_boto3
from ibm_botocore.client import Config
from datetime import date

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
    colum = ['Service Name', 'Plan Name', 'Plan Id', 'Currency', 'Plan cost', 'Plan Rated Cost', 'Metric', 'Unit', 'Quantity', 'Usage Rated Cost', 'Usage Cost', 'Month']
    table = {
    	'Service Name': [],
    	'Plan Name': [],
    	'Plan Id': [],
    	'Currency': [],
    	'Plan cost': [],
    	'Plan Rated Cost': [],
    	'Metric': [],
    	'Unit': [],
    	'Quantity': [],
        'Usage Rated Cost': [],
    	'Usage Cost': [],
    	'Month': []
    }
    print(dict)
    data = dict['usage']
    for i in dict['usage']['resources']:
        for j in i['plans']: 
            for x in j['usage']: 
                table['Service Name'].append(i['resource_name'])
                table['Plan Name'].append(j['plan_name'])
                table['Plan Id'].append(j['plan_id'])
                table['Plan cost'].append(j['cost'])
                table['Plan Rated Cost'].append(j['rated_cost'])
                table['Metric'].append(x['metric'])
                table['Unit'].append(x['unit'])
                table['Quantity'].append(x['quantity'])
                table['Usage Rated Cost'].append(x['rated_cost'])
                table['Usage Cost'].append(x['cost'])
                table['Currency'].append(dict['usage']['currency_code'])
                table['Month'].append(dict['usage']['month'])
    print(table)
    df = pd.DataFrame(table, columns = colum)
    name = "usage"+str(date.today())+".csv"
    df.to_csv(name, index=False)
    cos.upload_file(name,dict['bucket'],name)
    
    return { 'message': 'Hello world' }
