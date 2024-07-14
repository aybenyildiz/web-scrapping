import urllib.request, urllib.parse, urllib.error
import json
import ssl

total = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')


info = json.loads(data)
myinfo = info['comments']

for item in myinfo:
    total += int(item['count'])

print (total)
