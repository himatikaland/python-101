# PYTHON 101 BY HIMATIKA

## Dalam Python, ada beberapa sintaks dasar yang perlu kamu ketahui untuk menulis kode yang rapi dan mudah dipahami. Berikut adalah penjelasan mengenai indentasi, komentar, dan baris perintah dalam Python.

Mengapa penting: Memahami sintaks dasar Python penting untuk menulis kode yang rapi, mudah dibaca, dan bebas dari kesalahan sintaksis.

### Indentasi

Indentasi sangat penting dalam Python. Berbeda dengan bahasa pemrograman lain yang menggunakan tanda kurung atau kata kunci tertentu untuk mengindikasikan blok kode, Python menggunakan indentasi (spasi atau tab) untuk menentukan struktur kode. Blok kode yang memiliki indentasi yang sama akan dianggap berada dalam satu blok.

Contoh penggunaan indentasi dalam Python:

```python
def fungsi_contoh():
    print("Ini adalah contoh fungsi.") # Indentasi sejajar menunjukkan kode dalam blok yang sama

    if 5 > 2:
        print("Lima lebih besar dari dua.") # Indentasi yang lebih dalam menunjukkan blok kode baru

print("Ini adalah contoh kode di luar fungsi.") # Kode dengan indentasi awal berada di luar fungsi
```

Dalam contoh di atas, kode yang memiliki indentasi yang sama berada dalam satu blok. Jika kamu tidak mengikuti aturan indentasi, Python akan menampilkan IndentationError.

### Komentar

Komentar adalah bagian dari kode yang tidak akan dijalankan oleh interpreter Python. Komentar digunakan untuk membuat catatan dalam kode, menjelaskan bagian kode tertentu, atau menonaktifkan bagian kode sementara waktu. Dalam Python, ada dua jenis komentar:

Single-line comment: Untuk membuat komentar dalam satu baris, gunakan tanda pagar (#) di awal baris komentar. Contoh:

```python
# Ini adalah komentar dalam satu baris
print("Halo, dunia!") # Komentar bisa juga berada di sebelah kode
```

Multi-line comment: Untuk membuat komentar yang meliputi beberapa baris, kamu bisa menggunakan tanda kutip ganda atau tunggal sebanyak tiga kali di awal dan akhir komentar. Contoh:

```python
"""
Ini adalah komentar
yang meliputi
beberapa baris
"""
print("Halo, dunia!")
```

### PEP8

PEP8 adalah singkatan dari Python Enhancement Proposal 8. Ini adalah pedoman gaya pemrograman Python yang mencakup konvensi penamaan, komentar, dan pemformatan kode. PEP8 bertujuan untuk meningkatkan keterbacaan kode dan konsistensi gaya di seluruh komunitas Python.

Beberapa aturan PEP8 yang umum meliputi:

Gunakan 4 spasi untuk setiap level indentasi, bukan tab.
Batasi panjang baris kode hingga 79 karakter.
Gunakan spasi setelah koma dan sebelum operator dalam ekspresi.
Gunakan kata_kunci_lowercase_untuk_nama_fungsi_dan_variabel.
