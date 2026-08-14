## Write UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-11%20084949.png?raw=true)

# Description
This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
Download the file here.

# Hints
- Try checking the file’s header
- JPEG
- Tools like xxd or hexdump can help you inspect and edit file bytes.

# penyelesaian
- Download file
- karena salah satu hintnya bilang filenya corrupt maka kita cek dulu hexnya pake hex editor
- setelah dilihat ternyata headernya tidak sesuai header jpg maka itu harus diganti
- setelah diganti kita ganti juga format filenya jadi jpg
- untuk mempermudah kita gunakan image to text untuk mengeluarkan flag

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-11%20084927.png?raw=true)
