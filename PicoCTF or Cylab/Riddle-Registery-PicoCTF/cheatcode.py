import requests
import urllib3
import subprocess
import sys
import os
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) != 2:
        print("Usage: python cheatcode.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    s = requests.Session()
    r = s.get(url, verify=False)
    
    if r.status_code == 200:
        print("[+] Success!")
        
        # Simpan file sementara
        temp_file = "temp_downloaded_file"
        with open(temp_file, "wb") as f:
            f.write(r.content)  # Gunakan .content untuk binary
        
        # Jalankan exiftool pada file
        hasil_exif = subprocess.run(["exiftool", temp_file], capture_output=True, text=True)
        print(hasil_exif.stdout)
        
        # Split output menjadi lines
        lines = hasil_exif.stdout.split('\n')
        
        # Cari baris terakhir yang mengandung "Author"
        author_line = None
        for line in lines:
            if "Author" in line or "author" in line:
                author_line = line
        
        if author_line:
            # Extract value setelah ":"
            author_value = author_line.split(':', 1)[1].strip() if ':' in author_line else author_line
            print(f"\nAuthor ditemukan: {author_value}")
            
            # Ambil nilai setelah "=" dan decode base64
            decode = base64.b64decode(author_value)
            print(decode.decode('utf-8'))
        else:
            print("\nAuthor tidak ditemukan")
        
        # Hapus file sementara
        os.remove(temp_file)
    else:
        print("[-] Failed!")
    

if __name__ == "__main__":
    main()
