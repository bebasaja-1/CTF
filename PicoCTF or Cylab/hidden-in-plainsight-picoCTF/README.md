## Write up
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-02%20122436.png?raw=true)

# Description
You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.
Download the jpg image here.

# Hints
- Download the jpg image and read its metadata

# Langkah 1 Download
- Download img.jpg nya dulu

# Langkah 2 Explore
- cek metadata img.jpg menggunakan 'exiftool <filename>'
- dicode tulisan base64 menggunakan 'echo "teks" | base64 -d'
- decode lagi password steghide dengan metode yang sama

# Langkah 3 getting flag
- extract steghide dengan menggunakan ' steghide extract -sf <filename>
- masukkan passwordnya
- cat flag.txt yang diapet tadi
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-01-29%20104218.png?raw=true)
