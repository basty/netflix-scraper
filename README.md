# Scraping Netflix


A Python first attempt to scrap netflix titles and links to the actual streaming (within netflix).

Work in progress as I am using this excuse to learn. Right now, using your own netflix credentials, scraps the first page of "my list".


# Installation
Git clone this to your local computer and it should be good to go.

# Instructions
Use the test.py file and copy/paste the proper section from your request header as instructed

```python
#copy & paste here the whole content of "Cookie" section from the request header to netflix using your browser with developer tools. Remember to add a backslash at the end of the line \
#resulting text should be similar to the following:
from_browser = '{ \
\
memclid=10c33f2f-1ad9-4232-aa90-07bfe6494bf7; nfvdid=BQFmAAEBEL%2FVq1nMGFDSAWykQhaa1GVgLojMz2cP5bpz76xI3y6z%2BdnEAQDJ8oa%2F%2FMyk7QNLxIHxtv25ObepyjIveNvHPPp0caCKwnKTSk0ULj4B9hdGFDSFGQgz7yL1PnLlb1vTymMuw; clSharedContext=cb6234d-4de6-4bcd-81ed-2769b52342ad; didUserInteractWithPage=true; cL=1564404884792%7C156440488453486509%7C156440488451498503%7C%7C21%7CRP4ABCBCBDDE3ACL6PY; pas=%7B%22supplementals%22%3A%7B%22muted%22%3Atrue%7D%7D; SecureNetflixId=v%3D2%26mac%3DAQEAEQABABTzrkItH0FZyY-vOtCI3vQbumpMcbwTJlc.314112t%3D1564485029917; NetflixId=ct%3DBQAOAAEBELvYxTA4_ZDJ-9kb-ySbXjWB8L8kejQwbbC-xCOLo4UEatG8Xv6ljLZwrzqXsRAWdk_Wyshz3lvCi4ak6G6xL88QB_dtBSvNkMzOL6eEs7Vau_pvqL2MQnTnAR9f-pTCwX1232312FhzfhPHkcPC06E0ehbk3SRve-em-or_JMw97WZetMXTTlCcABDJAfqT7v1n0yQsQZtMSIHxJr92YAZqPHHIkxEmigE-ELxYEBHiLPsExa7E8HNfY6TIpTL9-eFANWKpIQqQ_hoZfdH3324234-lGF0t7lJJXA23yBAvzvmQL6vWflYacHr3yQcJYfwZnNtfT_kpOb_wUCqZ_17lnUSnLnY13yPp3c2IqkJGSBk5QVX5YKaqG18w9HCuoUc1Cfo4cRndlwy5RxSRrrubY0Z1F4MOiP-YmSKCty6_c79YL76SanuWQ6iU_C7zhDYqkGoqnaH8KsyTnTFzDGsH27VahsZlc4IiZyty5cH0iam95c35pddN8IuclextsSanK4yRxuUVnt_BHIW4lvi8zaBZzUtXyA5QnlF_5QqoETJkhEWg7GccJ6YNqm_7fA4iNcf4ITsTqL4YXnfLXodLEONKF8B7WC08LyFkj5jrgf3IEmfWPuWtYNDw08TPccZB50gev8pzZqr5S4E8sK328JBmhALNvoAdiwlk.%26bt%3Ddbl%26ch%3DAQEAEAABABQq6sTFoWLilpAyvygZTo5t5bbtsNC1zSU.%26v%3D2%26mac%3DAABABABAEAEAABABQNIxEALEDALQhynImy7wDtNhDs55shdyI.; playerPerfMetrics=%7B%22uiValue%22%3A%7B%22throughput%22%3A30430%2C%22throughputNiqr%22%3A1.2412812128555244%7D%2C%22mostRecentValue%22%3A%7B%22throughput%22%3A30430%2C%22throughputNiqr%22%3A1.2412812128555244%7D%7D; profilesNewSession=0; lhpuuidh-browse-RP42MU3MGNAMNM7F6DE3ACL6PY=IT%3AEN-IT%3A662bc225-260a-49fb-a21a-d9476b912d77_ROOT; lhpuuidh-browse-RP42MU3MGNAMNM7F6DE3ACL6PY-T=1564485036506 \
\
}' 
```
Check out the test.py file. E-mail any specific questions to <the.basty@gmail.com>

# All Available Functions
<table class="tg">
  <tr>
    <th class="tg-s6z2">__Functions__</th>
    <th class="tg-s6z2">__Return Data Type__</th>
    <th class="tg-s6z2">__Description__</th>
  </tr>
  <tr>
    <td class="tg-s6z2">get_list_titles_with_links</td>
    <td class="tg-s6z2">dictionary</td>
    <td class="tg-s6z2">Returns a dictionary with key:value, where key is the title and value the url</td>
  </tr>
</table>
