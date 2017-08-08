#!/usr.bin.env python
import re
import sys
import urllib.request


# e.g. current_date = 'December 10, 2016'
service_center = sys.argv[1]
classification = sys.argv[2]
current_date = sys.argv[3]

service_center_codes = {
    'CSC': "991", # California
    'NSC': "992", # Nebraska
    'TSC': "993", # Texas
    'VSC': "990", # Vermont
    'YSC': "1031", # Potomac
}

cookie_url = 'https://egov.uscis.gov/cris/processTimesDisplayInit.do'
url = 'https://egov.uscis.gov/cris/processingTimesDisplay.do'
data = 'serviceCenter=%s&displaySCProcTimes=Service+Center+Processing+Dates'
code = service_center_codes[service_center]

res = urllib.request.urlopen(cookie_url)
set_cookie_header = res.getheader('Set-Cookie')
cookie = set_cookie_header.split(';')[0]

req = urllib.request.Request(url, data=bytes(data % code, 'utf-8'))
req.add_header('Cookie', cookie)

with urllib.request.urlopen(req) as res:
    page = str(res.read())

single_line_page = page.replace('\\r\\n', ' ').replace('\\t', ' ')
match = re.search('%s.*?(\w+ \d+, \d{4})' % classification, single_line_page)
date = match.group(1)

if date != current_date:
    print('%s: %s' % (classification, date), end='')
