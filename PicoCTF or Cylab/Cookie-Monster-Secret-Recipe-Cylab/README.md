### WRITE UP
<img width="991" height="880" alt="Screenshot 2026-08-14 110440" src="https://github.com/user-attachments/assets/e438a552-5413-4cba-a284-ddc8f97b9db7" />

## Description
Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?

## Hint
- Sometimes, the most important information is hidden in plain sight. Have you checked all parts of the webpage?
- Cookies aren't just for eating - they're also used in web technologies!
- Web browsers often have tools that can help you inspect various aspects of a webpage, including things you can't see directly.

## Penyelesaian

### 1. Observasi Awal
Pada tahap awal pengerjaan, saya diberikan sebuah URL yang secara otomatis melakukan redirect menuju halaman login. Saya kemudian mencoba berbagai pendekatan untuk mengeksplorasi kerentanan pada halaman tersebut, namun belum membuahkan hasil.

<img width="846" height="440" alt="Screenshot 2026-08-14 111451" src="https://github.com/user-attachments/assets/ea84d835-0de5-423a-a19b-f416010dce11" />

### 2. Percobaan Login
Selanjutnya, saya mencoba melakukan login menggunakan kombinasi username dan password secara acak (random).

<img width="823" height="452" alt="Screenshot 2026-08-14 111638" src="https://github.com/user-attachments/assets/e81e42b5-2d9f-41e0-9077-f9d13c555511" />

Setelah proses login dilakukan, saya diarahkan (redirect) ke halaman `login.php`.

<img width="707" height="300" alt="Screenshot 2026-08-14 111505" src="https://github.com/user-attachments/assets/4cb0eb22-6983-4be1-91fc-5391bf56011c" />

### 3. Menemukan Petunjuk pada Cookie
Pada halaman tersebut, saya menemukan sebuah hint yang berbunyi:

> "Have you checked your cookies lately"

Berdasarkan petunjuk tersebut, saya langsung memeriksa cookie yang tersimpan pada browser. Hasilnya, ditemukan sebuah cookie dengan isi sebagai berikut:

> "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzczMTEwRUQxfQ%3D%3D"

Perlu dicatat bahwa `%3D` pada string tersebut merupakan hasil URL-encoding dari karakter `=`.

### 4. Analisis dan Decode Cookie
Setelah diamati, isi dari cookie tersebut memiliki pola yang mengindikasikan hasil encoding **Base64**. Saya kemudian melakukan proses decode terhadap teks tersebut, dan flag berhasil ditemukan.

<img width="1490" height="782" alt="Screenshot 2026-08-14 111539" src="https://github.com/user-attachments/assets/8f442925-8d00-4b08-8962-d1a53c2baed2" />
