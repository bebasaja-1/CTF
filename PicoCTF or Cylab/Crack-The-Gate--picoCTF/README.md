## Write UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-09%20105035.png?raw=true)

# Description
We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: ctf-player@picoctf.org. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?
Additional details will be available after launching your challenge instance.

# Hints
- Developers sometimes leave notes in the code; but not always in plain text.
- A common trick is to rotate each letter by 13 positions in the alphabet.

# penyelesaian
- buka link yang mengarah ke web soal
- setelah di view page source terdapat sebuah teks yang sepertinya sudah di enkripsi
- setelah di decrypt menggunakan ROT13 terdapat sebuah header
- gunakan burpsuite untuk memasukkan header tadi ke HTTP Request
- klik send
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-09%20104636.png?raw=true)
