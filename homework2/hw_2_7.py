import sys
import requests
u = sys.argv[1]
url = 'http://'+u
response = requests.get(url)
print(response.headers.get('Server'))