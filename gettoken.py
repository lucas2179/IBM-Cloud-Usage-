import requests
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    # "Authorization": "{}".format(iam_token)
}

data = {
  'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
  'apikey': <apikey>
}

response = requests.post('https://iam.cloud.ibm.com/identity/token/', headers=headers, data=data, verify=False)
print(response.text)
