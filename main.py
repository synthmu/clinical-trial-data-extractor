import requests
url = "https://clinicaltrials.gov/api/v2/studies"
parameters = {
    'format': 'json', 'query.cond': "Alzheimer's Disease AND curcumin",
              'pageSize': 10, 'query.intr': 'curcumin'
              }
response = requests.get(url, params=parameters)
print(response.status_code)