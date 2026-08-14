## Write Up
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-25%20123158.png?raw=true)

# Description
Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
The website is running picoCTF News.

# Hints
- Explore backend development with us
- The head was dumped.

Penyelesaian 
- pertama tama buka website yang diberikan 
- setelah dicek ada salah satu tag yaitu api documentation yang mengarah ke swagger
- setelah dibuka  terdapat /heapdump yang akan mendownload file dump 
- gunakan kombinasi cat dan grep agar flag ketemu

![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-25%20123153.png?raw=true)
