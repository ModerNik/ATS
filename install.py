import tempfile, os, zipfile, io
import requests

r = requests.get('https://github.com/ModerNik/ATS/blob/main/test.zip?raw=true')

with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    archive.extractall()
