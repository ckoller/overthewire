import requests as r
import time as t

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://' + username + '.natas.labs.overthewire.org/index-source.html'

session = r.Session()
response = session.get(url, auth = (username, password))
print(response.text)

# Run code and get pw -> xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
