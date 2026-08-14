import sys
import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    if len(sys.argv) !=2:
        print('masukkan url filenya')
        sys.exit(-1)

    url = sys.argv[1]
    s = requests.Session()
    r = s.get(url, verify=False)
    if r.status_code == 200:
        print('berhasil download') # mendownload file
        
        # Ambil content sebagai hex string
        hex_content = r.content.hex()
        
        # Ganti 3 karakter hex pertama menjadi 'ffd'
        new_hex = 'ffd' + hex_content[3:]
        
        try:
            # Ubah kembali menjadi bytes
            new_content = bytes.fromhex(new_hex)
            
            with open('file.jpg', 'wb') as f: 
                f.write(new_content)
            print('file berhasil disimpan sebagai file.jpg')
            os.startfile('file.jpg') # membuka file.jpg
        except ValueError as e:
            print(f"Error konversi hex: {e}")

    else:
        print('gagal download')


if __name__ == '__main__':

    main()
