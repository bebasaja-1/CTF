### WRITE UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20110440.png?raw=true)

## Description
Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?

## Hint
- Sometimes, the most important information is hidden in plain sight. Have you checked all parts of the webpage?
- Cookies aren't just for eating - they're also used in web technologies!
- Web browsers often have tools that can help you inspect various aspects of a webpage, including things you can't see directly.

## Penyelesaian

### 1. Observasi Awal
Pada tahap awal pengerjaan, saya diberikan sebuah URL yang secara otomatis melakukan redirect menuju halaman login. Saya kemudian mencoba berbagai pendekatan untuk mengeksplorasi kerentanan pada halaman tersebut, namun belum membuahkan hasil.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20111451.png?raw=true)

### 2. Percobaan Login
Selanjutnya, saya mencoba melakukan login menggunakan kombinasi username dan password secara acak (random).

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20111638.png?raw=true)

Setelah proses login dilakukan, saya diarahkan (redirect) ke halaman `login.php`.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20111505.png?raw=true)

### 3. Menemukan Petunjuk pada Cookie
Pada halaman tersebut, saya menemukan sebuah hint yang berbunyi:

> "Have you checked your cookies lately"

Berdasarkan petunjuk tersebut, saya langsung memeriksa cookie yang tersimpan pada browser. Hasilnya, ditemukan sebuah cookie dengan isi sebagai berikut:

> "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzczMTEwRUQxfQ%3D%3D"

Perlu dicatat bahwa `%3D` pada string tersebut merupakan hasil URL-encoding dari karakter `=`.

### 4. Analisis dan Decode Cookie
Setelah diamati, isi dari cookie tersebut memiliki pola yang mengindikasikan hasil encoding **Base64**. Saya kemudian melakukan proses decode terhadap teks tersebut, dan flag berhasil ditemukan.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20111539.png?raw=true)
