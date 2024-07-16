import requests
URL = ""

#make a session object (improves performance by reusing TCP connection)
#s = requests.Session()

# Making a GET request
#response = requests.get('https://api.github.com/users/Sunshinepunch')

#s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

response = requests.get(URL)

print (response.content)
# check status code for response received
# success code - 200
#print(response.url)

# print content of request
#print(response.status_code)
