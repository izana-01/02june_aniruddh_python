import urllib.request
import time

urls = ['http://127.0.0.1:8000/', 'http://127.0.0.1:8000/assi/']
for url in urls:
    last_err = None
    for i in range(6):
        try:
            with urllib.request.urlopen(url, timeout=5) as r:
                print(url, '->', r.status)
                data = r.read(200).decode('utf-8', errors='ignore')
                print(data[:300].replace('\n',' '))
            last_err = None
            break
        except Exception as e:
            last_err = e
            time.sleep(1)
    if last_err:
        print(url, '-> ERROR:', last_err)
