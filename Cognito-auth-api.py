
import boto3
import requests

// enter your cognito details

auth_data = { 'USERNAME': username , 'PASSWORD': password }
provider_client = boto3.client('cognito-idp', region_name='region')
resp = provider_client.admin_initiate_auth(UserPoolId=<user-pool-id>, AuthFlow='ADMIN_NO_SRP_AUTH', AuthParameters=auth_data, ClientId=<client-id>)
token = resp['AuthenticationResult']['IdToken']
print(token)
headers = {
    'Authorization':token,
}

//call api 
response = requests.get('<your-api>', headers=headers)

print(response.text)


