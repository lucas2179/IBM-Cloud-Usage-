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
    colum = ['Service Name', 'Instance Name', 'Instance Id', 'Plan Name', 'Billable', 'Region', 'Resource Group', 'Organization Name', 'Currency', 'Metric', 'Usage Unit', 'Usage Quantity', 'Cost/unity', 'Price']
    table = {
    	'Service Name': [],
    	'Instance Name': [],
    	'Instance Id': [],
    	'Plan Name': [],
    	'Region': [],
    	'Resource Group': [],
    	'Organization Name': [],
    	'Billable': [],
    	'Currency': [],
    	'Metric': [],
    	'Usage Unit': [],
    	'Usage Quantity': [],
        'Cost/Unity': [],
    	'Price': []
    }
    
    data = dict['usage']
    for p in data["resources"]:
        for j in p['usage']:
            
            table['Service Name'].append(p['resource_name'])
            table['Instance Name'].append(p['resource_instance_name'])
            table['Instance Id'].append(p['resource_instance_id'])
            table['Plan Name'].append(p['plan_name'])
            table['Billable'].append(p['billable'])
            table['Region'].append(p['region'])
            try:
                table['Resource Group'].append(p['resource_group_name'])
            except:
                table['Resource Group'].append('-')
            try:
                table['Organization Name'].append(p['organization_name'])
            except:
                table['Organization Name'].append('-')
            table['Currency'].append(p['currency_code'])
            table['Metric'].append(j['metric'])
            table['Usage Unit'].append(j['unit'])
            table['Usage Quantity'].append(j['quantity'])
            try:
                
                table['Cost/Unity'].append(j['price'][0]['price'])
            except:
                table['Cost/Unity'].append('-')
            table['Price'].append(j['rated_cost'])

    print(table)
    df = pd.DataFrame(table, columns = colum)
    name = "usage"+str(date.today())+".csv"
    df.to_csv(name, index=False)
    cos.upload_file(name,dict['bucket'],name)
    
    return { 'message': 'Hello world' }
