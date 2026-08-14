import sys
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <url>")
        sys.exit(-1)
    # mendownload file server.log
    url = sys.argv[1]
    s = requests.Session()
    r = s.get(url, verify=False)
    res = r.text
    # Kumpulkan semua baris yang mengandung FLAGPART
    flagpart_lines = []
    for line in res.split("\n"):
        if "FLAGPART" in line:
            flagpart_lines.append(line.strip())
            print(line.strip())
    
    # Ambil baris ke-1, 2, 3, dan 5 (index 0, 1, 2, 4)
    if len(flagpart_lines) >= 1:
        pertama = flagpart_lines[0]
  
    if len(flagpart_lines) >= 2:
        kedua = flagpart_lines[1]
    
    if len(flagpart_lines) >= 3:
        ketiga = flagpart_lines[2]
    
    if len(flagpart_lines) >= 5:
        kelima = flagpart_lines[4]

    print(pertama[37:], kedua[37:], ketiga[37:], kelima[37:])
    
    

if __name__ == "__main__":

    main()
