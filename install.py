import tempfile, os, zipfile, io
import requests

r = requests.get('https://github.com/ModerNik/ATS/blob/main/test.zip?raw=true')

with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    archive.extractall()
url = 'https://raw.githubusercontent.com/ModerNik/ATS/main/server.py'  
r = requests.get(url)

print(r.status_code)  
print(r.headers['content-type'])  
print(r.encoding)

ok = r.text

file = open("server.py", "w", encoding='utf-8')
file.write(ok)
file.close()

print('DONE')
