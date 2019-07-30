import requests
import io
import scraper as s
import re

def get_page(cookies_set, page = 'my-list'):
	if page.lower() == 'my-list': page = 'https://www.netflix.com/browse/my-list' 
	r = requests.get(
	page, cookies = cookies_set, 
	data={
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,it;q=0.7,nl;q=0.6,pt;q=0.5,fr;q=0.4',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive', 
	'Host': 'www.netflix.com',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
	})
	
	return r.text


#copy & paste here the whole content of "Cookie" section from the request header to netflix using your browser with developer tools. Remember to add a backslash at the end of the line \
from_browser = '{ \
\
memclid=10c33f2f-1ad9-4232-aa90-07bfe6494bf7; nfvdid=BQFmAAEBEL%2FVq1nMGFDSAWykQhaa1GVgLojMz2cP5bpz76xI3y6z%2BdnEAQDJ8oa%2F%2FMyk7QNLxIHxtv25ObepyjIveNvHPPp0caCKwnKTSk0ULj4B9hdGFDSFGQgz7yL1PnLlb1vTymMuw; clSharedContext=cb6234d-4de6-4bcd-81ed-2769b52342ad; didUserInteractWithPage=true; cL=1564404884792%7C156440488453486509%7C156440488451498503%7C%7C21%7CRP4ABCBCBDDE3ACL6PY; pas=%7B%22supplementals%22%3A%7B%22muted%22%3Atrue%7D%7D; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABTzrkItH0FZyY-vOtCI3vQbumpMcbwTJlc.314112t%3D1564485029917; NetflixId=ct%3DBQAOAAEBELvYxTA4_ZDJ-9kb-ySbXjWB8L8kejQwbbC-xCOLo4UEatG8Xv6ljLZwrzqXsRAWdk_Wyshz3lvCi4ak6G6xL88QB_dtBSvNkMzOL6eEs7Vau_pvqL2MQnTnAR9f-pTCwX1232312FhzfhPHkcPC06E0ehbk3SRve-em-or_JMw97WZetMXTTlCcABDJAfqT7v1n0yQsQZtMSIHxJr92YAZqPHHIkxEmigE-ELxYEBHiLPsExa7E8HNfY6TIpTL9-eFANWKpIQqQ_hoZfdH3324234-lGF0t7lJJXA23yBAvzvmQL6vWflYacHr3yQcJYfwZnNtfT_kpOb_wUCqZ_17lnUSnLnY13yPp3c2IqkJGSBk5QVX5YKaqG18w9HCuoUc1Cfo4cRndlwy5RxSRrrubY0Z1F4MOiP-YmSKCty6_c79YL76SanuWQ6iU_C7zhDYqkGoqnaH8KsyTnTFzDGsH27VahsZlc4IiZyty5cH0iam95c35pddN8IuclextsSanK4yRxuUVnt_BHIW4lvi8zaBZzUtXyA5QnlF_5QqoETJkhEWg7GccJ6YNqm_7fA4iNcf4ITsTqL4YXnfLXodLEONKF8B7WC08LyFkj5jrgf3IEmfWPuWtYNDw08TPccZB50gev8pzZqr5S4E8sK328JBmhALNvoAdiwlk.%26bt%3Ddbl%26ch%3DAQEAEAABABQq6sTFoWLilpAyvygZTo5t5bbtsNC1zSU.%26v%3D2%26mac%3DAABABABAEAEAABABQNIxEALEDALQhynImy7wDtNhDs55shdyI.; playerPerfMetrics=%7B%22uiValue%22%3A%7B%22throughput%22%3A30430%2C%22throughputNiqr%22%3A1.2412812128555244%7D%2C%22mostRecentValue%22%3A%7B%22throughput%22%3A30430%2C%22throughputNiqr%22%3A1.2412812128555244%7D%7D; profilesNewSession=0; lhpuuidh-browse-RP42MU3MGNAMNM7F6DE3ACL6PY=IT%3AEN-IT%3A662bc225-260a-49fb-a21a-d9476b912d77_ROOT; lhpuuidh-browse-RP42MU3MGNAMNM7F6DE3ACL6PY-T=1564485036506 \
\
}' 
from_browser = str.replace(from_browser, ';', '')
cookie_dict = dict(re.findall(r'(\S+)=(".*?"|\S+)', from_browser))

content = get_page(cookie_dict)

print('Items from my-list:\n')
for item, url in s.get_list_titles_with_links(content).items():
	print(item+':', url)
