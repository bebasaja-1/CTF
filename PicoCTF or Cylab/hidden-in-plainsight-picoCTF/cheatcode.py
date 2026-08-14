import re
import sys
import requests
import subprocess
import urllib3
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)
    url = sys.argv[1]

    # download file
    s = requests.session()
    r = s.get(url, verify=False)
    if r.status_code == 200:
        temp_file = 'temp_file'
        with open(temp_file, 'wb') as f:
            f.write(r.content)

            #cek metadata
            hasil_exif = subprocess.run(['exiftool', temp_file], capture_output=True, text=True)
            encode = re.search(r'Comment\s*:\s*(.*)',hasil_exif.stdout)

            #decode base64
            decode = base64.b64decode(encode.group(1))
            udah_decode = decode.decode('utf-8')            
            pw = udah_decode[9:21]
            decode_lagi = base64.b64decode(pw)
            
            # decode pw steghide
            subprocess.run(['steghide', 'extract', '-sf', temp_file, '-p', decode_lagi.decode('utf-8')])
            #cari flag
            subprocess.run(['cat', 'flag.txt',])

    else:
        print("Failed")

if __name__ == "__main__":
    main()
