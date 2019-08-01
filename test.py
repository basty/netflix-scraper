import requests
import io
import scraper as s
import re
import netflix as n
import sys

def get_page(cookies_set, page = 'my-list'):
	if page.lower() == 'my-list': page = 'https://www.netflix.com/browse/my-list' 
	r = requests.get(
	page, cookies = cookies_set)
	
	return r.text

if len(sys.argv) < 5:
	print("\nExpected parameters are, <user> <password> <country_code +XX> <country_iso_code XX>\n\nExample: python test.py myuser mypas +1 US\n")
	exit(1)
cookie_dict = n.login_get_cookies(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
if cookie_dict:
	content = get_page(cookie_dict)

	print('Items from my-list:\n')
	for item, url in s.get_list_titles_with_links(content).items():
		print(item+':', url)
else:
	print('failed')

