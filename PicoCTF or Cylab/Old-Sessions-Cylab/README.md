### WRITE UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-12%20093203.png?raw=true)
## Description
Proper session timeout controls are critical for securing user accounts. If a user logs in on a public or shared computer but doesn’t explicitly log out (instead simply closing the browser tab), and session expiration dates are misconfigured, the session may remain active indefinitely.

This then allows an attacker using the same browser later to access the user’s account without needing credentials, exploiting the fact that sessions never expire and remain authenticated.

## hint
- Do you know how to use the web inspector?
- Where are cookies stored?

## penyelesaian

# 1. Registrasi dan Login
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-11%20103649.png?raw=true)

Langkah awal yang dilakukan adalah melakukan registrasi akun baru,


![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-11%20103700.png?raw=true)

kemudian login ke dalam aplikasi menggunakan akun tersebut.

# 2. Menemukan Petunjuk
Setelah berhasil login, ditemukan sebuah komentar pada aplikasi yang berbunyi:

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-11%20104105.png?raw=true)

Komentar ini mengindikasikan adanya endpoint tersembunyi yang berpotensi memiliki celah keamanan.

# 3. Eksplorasi Endpoint `/sessions`
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-11%20104136.png?raw=true)
Berdasarkan petunjuk tersebut, dilakukan pengecekan pada endpoint `/sessions`. Hasilnya, endpoint ini menampilkan daftar session dari seluruh pengguna yang pernah login ke aplikasi, termasuk salah satu session milik akun **admin**.

### 4. Session Hijacking dengan Burp Suite
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-12%20094539.png?raw=true)
Menggunakan **Burp Suite**, request yang dikirim oleh browser diintersepsi, kemudian nilai session milik akun sendiri diganti dengan nilai session milik admin yang ditemukan sebelumnya.

### 5. Akses Akun Admin
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-12%20094458.png?raw=true)
Setelah session berhasil diganti, akses ke akun admin berhasil diperoleh. Di dalam akun tersebut ditemukan flag yang menjadi tujuan akhir dari challenge ini.




