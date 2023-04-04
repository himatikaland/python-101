# PYTHON 101 BY HIMATIKA

## Sejarah Class 
Konsep kelas adalah salah satu konsep yang paling fundamental dalam pemrograman berorientasi objek (OOP). Ide dasar kelas adalah untuk menggabungkan data dan fungsi yang berkaitan dengan data ke dalam satu unit yang disebut kelas.

Konsep kelas pertama kali diperkenalkan dalam bahasa pemrograman Simula pada tahun 1960-an. Simula adalah bahasa pemrograman pertama yang mendukung OOP dan mengenalkan konsep kelas sebagai bagian dari model simulasi berorientasi objek.

Pada tahun 1970-an, bahasa pemrograman Smalltalk diperkenalkan dengan dukungan penuh untuk OOP dan konsep kelas menjadi salah satu fitur utama bahasa tersebut. Smalltalk menjadi bahasa pemrograman OOP yang populer dan mempengaruhi banyak bahasa pemrograman modern yang mendukung OOP.

Selama tahun 1980-an dan 1990-an, bahasa pemrograman seperti C++ dan Java mengadopsi konsep kelas dan OOP dari Smalltalk. C++ adalah bahasa pemrograman pertama yang mendukung OOP di lingkungan bahasa pemrograman C dan menggabungkan beberapa fitur dari bahasa pemrograman OOP seperti Smalltalk dan Simula. Java, yang diperkenalkan pada tahun 1995, juga didasarkan pada konsep OOP dan menggunakan kelas sebagai unit dasar dalam pemrograman.

Dalam bahasa pemrograman modern seperti Python dan Ruby, kelas juga menjadi fitur utama dalam OOP. Bahasa-bahasa ini menyederhanakan sintaksis kelas dan menyediakan fitur-fitur lain yang membuat OOP lebih mudah dipahami dan digunakan.

Dalam ringkasan, konsep kelas dalam pemrograman berasal dari bahasa pemrograman Simula pada tahun 1960-an. Kemudian, Smalltalk menjadi bahasa pemrograman pertama yang mendukung OOP secara penuh dan mengenalkan konsep kelas sebagai bagian dari model simulasi berorientasi objek. Saat ini, kelas merupakan konsep utama dalam pemrograman berorientasi objek dan digunakan dalam bahasa pemrograman modern seperti C++, Java, Python, dan Ruby.

## Implementasi Class pada Python
Untuk mengimplementasikan konsep kelas pada bahasa pemrograman Python, kita dapat menggunakan kata kunci class. Kita dapat mendefinisikan kelas dengan menentukan atribut dan metode yang dimilikinya. Berikut adalah contoh sederhana untuk mengimplementasikan kelas pada Python:

```python
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def info(self):
        print("Nama hewan:", self.nama)
        print("Jenis hewan:", self.jenis)

hewan1 = Hewan("kucing", "mamalia")
hewan1.info()
```
Dalam contoh di atas, kita telah membuat kelas Hewan dengan dua atribut yaitu nama dan jenis. Selanjutnya, kita juga mendefinisikan metode info yang mencetak atribut nama dan jenis dari objek hewan. Selain itu, kita juga membuat sebuah objek hewan1 dari kelas Hewan dengan nilai nama dan jenis tertentu, dan mencetak informasi tentang objek menggunakan metode info.

Kita juga dapat menggunakan pewarisan (inheritance) untuk membuat kelas baru dengan mewarisi atribut dan metode dari kelas yang sudah ada. Berikut adalah contoh sederhana penggunaan pewarisan pada Python:

```python
class Kucing(Hewan):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna

    def info(self):
        super().info()
        print("Warna kucing:", self.warna)

kucing1 = Kucing("Kitty", "kucing", "putih")
kucing1.info()
```
Dalam contoh di atas, kita telah membuat kelas Kucing yang merupakan turunan dari kelas Hewan. Kita menggunakan kata kunci super() untuk memanggil metode __init__ dari kelas induk. Selanjutnya, kita menambahkan atribut warna pada kelas Kucing. Kita juga mengganti metode info pada kelas Kucing dengan menambahkan informasi tentang warna kucing. Kemudian, kita membuat objek kucing1 dari kelas Kucing dengan nilai nama, jenis, dan warna tertentu, dan mencetak informasi tentang objek menggunakan metode info.

Dengan menggunakan konsep kelas pada Python, kita dapat membuat kode yang lebih terstruktur, mudah dimengerti, dan mudah dipelihara.