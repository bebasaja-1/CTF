## LOG-HUNTER-PICOCTF
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Annotation%202026-01-23%20163822.png?raw=true)

# Description
Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments.

# Hint
- You can use grep to filter only matching lines from the log.
- Some lines are duplicates; ignore extra occurrences.

# langkah 1 Download
- Download file server.log

# langkah 2 explore
- lihat isi server.log dengan command 'cat <file>'

# langkah 3 finding flag
- cari flag dengan command 'cat server.log | grep 'FLAGPART'
- Ketemu deh

# FLAG
![alt text](https://github.com/bebasaja-1/gambar/blob/main/Annotation%202026-01-23%20164710.png?raw=true)
