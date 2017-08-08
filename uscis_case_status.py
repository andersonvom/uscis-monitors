#!/usr.bin.env python
import re
import sys
import urllib.request


app_receipt_num=sys.argv[1]
current_status=sys.argv[2]

url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
data = 'appReceiptNum=%s' % app_receipt_num

with urllib.request.urlopen(url, data=bytes(data, 'utf-8')) as res:
    page = str(res.read())

single_line_page = page.replace('\\r\\n', ' ').replace('\\t', ' ')
match = re.search('<h1>(.*?)</h1>', single_line_page)
new_status = match.group(1)

if new_status != current_status:
    print('%s: %s' % (app_receipt_num, new_status), end='')
