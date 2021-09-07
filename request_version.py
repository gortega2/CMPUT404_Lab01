import requests
print(requests.__version__)

#response = requests.get('https://www.google.com')

#print(response.text[0:100])

response = requests.get('https://raw.githubusercontent.com/gortega2/CMPUT404_Lab01/main/request_version.py')

print(response.text)