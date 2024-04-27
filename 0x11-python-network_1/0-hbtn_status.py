#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()

ans = f'''Body response:
    - type: {type(html)}
    - content: {html}
    - utf8 content: {str(html, 'utf-8')}'''
print(ans)
