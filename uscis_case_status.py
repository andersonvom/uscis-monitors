#!/usr/bin/env python
import re
import sys
import urllib.request


app_receipt_num=sys.argv[1]
current_status=sys.argv[2]
current_action_date=sys.argv[3]

url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
data = 'appReceiptNum=%s' % app_receipt_num

with urllib.request.urlopen(url, data=bytes(data, 'utf-8')) as res:
    page = str(res.read())

single_line_page = page.replace('\\r\\n', ' ').replace('\\t', ' ')

match = re.search('has been locked out', single_line_page)
if match is not None:
    print('[ERROR] Too many requests')
    sys.exit(1)

match = re.search('<h1>(.*?)</h1>', single_line_page)
new_status = match.group(1)
match = re.search('On (\w+ \d+, \d+),', single_line_page)
new_action_date = match.group(1)

if new_status != current_status or new_action_date != current_action_date:
    print('%s: %s - %s' % (app_receipt_num, new_status, new_action_date), end='')
