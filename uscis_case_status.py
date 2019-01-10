#!/usr/bin/env python
import re
import sys
import urllib.request


def get_page_as_single_line(url, post_data):
    with urllib.request.urlopen(url, data=bytes(post_data, 'utf-8')) as res:
        page = str(res.read())

    return page.replace('\\r\\n', ' ').replace('\\t', ' ')


def exit_on_error(page):
    match = re.search('has been locked out', page)
    if match is not None:
        print('[ERROR] Too many requests')
        sys.exit(1)


def get_status(page):
    return re.search('<h1>(.*?)</h1>', page).group(1)


def get_date(page):
    months = '(January|February|March|April|May|June|July|August|September|October|November|December)'
    return re.search('(%s \d+, \d+),' % months, page).group(1)


def get_case_status(receipt_number):
    url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
    post_data = 'appReceiptNum=%s' % receipt_number
    page = get_page_as_single_line(url, post_data)
    exit_on_error(page)
    return get_status(page), get_date(page)


if __name__ == '__main__':
    receipt_number = sys.argv[1]
    last_case_status = (sys.argv[2], sys.argv[3])
    current_case_status = get_case_status(receipt_number)
    if last_case_status != current_case_status:
        info = (receipt_number,) + current_case_status
        print('%s: %s - %s' % info, end='')
