from bs4 import BeautifulSoup
import io
import requests
import re

def login_get_cookies(usr, password, country_code, country_iso_code, base = 'https://www.netflix.com/login'):

	cookies = {}
	url = base
	response = requests.get(url, allow_redirects=False )
	if response.status_code == 302:
		# we are in the right path
		# adding new cookies, if any
		set_cookies = '{ ' + response.headers['Set-Cookie'] + ' }'
		set_cookies = str.replace(set_cookies, ';', '')
		cookies = dict(re.findall(r'(\S+)=(".*?"|\S+)', set_cookies))
		#cookies.update(response.headers['Set-Cookie'])
		print('cookies: ', cookies)
		url2 = response.headers['location']
		print("got a 302, hitting now: ", url2)
		response = requests.get(url2, allow_redirects=False )
		print(response)
		print(response.headers)
		print(response.status_code)
		try:
			set_cookies2 = '{ ' + response.headers['Set-Cookie'] + ' }'
			set_cookies2 = str.replace(set_cookies2, ';', '')
			cookies.update(dict(re.findall(r'(\S+)=(".*?"|\S+)', set_cookies2)))
		except:
			pass

		# adding new cookies, if any
		#cookies.update(response.headers['Set-Cookie'])
		print('cookies: ', cookies)

		params = {
		'userLoginId': usr, 
		'password': password, 
		'countryCode': country_code, 
		'countryIsoCode': country_iso_code, 
		'flow': 'websiteSignUp', 
		'action': 'loginAction', 
		'mode': 'login',
		'withFields': 'rememberMe,nextPage,userLoginId,password,countryCode,countryIsoCode',
		'rememberMe': 'true'}

		data = {
		'Host': 'www.netflix.com',
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language': 'en-GB,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Referer': 'https://www.netflix.com/it-en/login',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'keep-alive',
		"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}

		response = requests.post(url2, data = data, cookies = cookies, params = params)
		#print(response)
		#print(response.headers)
		#print(response.status_code)
		set_cookies = '{ ' + response.headers['Set-Cookie'] + ' }'
		set_cookies = str.replace(set_cookies, ';', '')
		cookies.update(dict(re.findall(r'(\S+)=(".*?"|\S+)', set_cookies)))

	else:
		print(response)
		print(response.status_code)
		print('Netflix probably blocked your ip')		
		cookies = None

	return cookies
