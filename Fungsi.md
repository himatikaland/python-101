# PYTHON 101 BY HIMATIKA

## Sejarah Fungsi
Fungsi atau prosedur adalah salah satu konsep dasar dalam pemrograman yang memungkinkan kita untuk mengorganisir kode program menjadi bagian-bagian yang lebih kecil dan terpisah, sehingga dapat digunakan kembali dalam berbagai bagian program yang berbeda. Konsep fungsi telah ada dalam pemrograman sejak awal, meskipun implementasinya mungkin berbeda-beda antara bahasa pemrograman.

Pada awalnya, bahasa pemrograman yang pertama dibuat seperti Fortran, COBOL, dan BASIC tidak memiliki konsep fungsi yang sama seperti yang kita kenal saat ini. Namun, bahasa pemrograman seperti Algol 60 dan Lisp memperkenalkan konsep fungsi yang lebih abstrak dan umum. Algol 60 memperkenalkan kata kunci "procedure" untuk mendefinisikan prosedur, sementara Lisp memperkenalkan konsep fungsi sebagai objek pertama (first-class object) yang dapat dioperasikan seperti tipe data lainnya.

Dalam bahasa pemrograman C, fungsi didefinisikan sebagai blok kode yang dapat dipanggil dari bagian program lainnya dan dapat mengembalikan nilai. Konsep fungsi di C menjadi sangat populer dan banyak bahasa pemrograman modern seperti Java, Python, dan JavaScript juga mengadopsi konsep fungsi yang sama.

Seiring perkembangan bahasa pemrograman, konsep fungsi juga telah berkembang dan mengalami beberapa perubahan dan penambahan fitur, seperti parameter default, argumen kata kunci, fungsi lambda, dan lain-lain. Fungsi juga menjadi sangat penting dalam paradigma pemrograman berorientasi objek, di mana objek dapat memiliki metode, yang pada dasarnya adalah fungsi yang terkait dengan objek tersebut.

Dalam beberapa tahun terakhir, fungsi juga menjadi sangat penting dalam pengembangan aplikasi berbasis web, di mana kerangka kerja web seperti Django, Flask, dan Ruby on Rails mengandalkan fungsi untuk mengatur logika bisnis dan menghasilkan respons HTTP.

Secara keseluruhan, konsep fungsi telah menjadi bagian integral dari pemrograman modern dan terus berkembang seiring berkembangnya bahasa pemrograman dan paradigma pemrograman baru.

## Implementasi Fungsi pada Python
Di Python, fungsi didefinisikan dengan kata kunci def diikuti oleh nama fungsi dan parameter, di dalam blok kode yang diawali dengan indentasi. Sebuah fungsi dapat mengembalikan nilai atau tidak, tergantung pada kebutuhan.

Berikut ini adalah contoh sederhana penggunaan fungsi di Python untuk menghitung jumlah dari dua bilangan:

```python
def hitung_jumlah(a, b):
    jumlah = a + b
    return jumlah

x = 5
y = 10
hasil = hitung_jumlah(x, y)
print("Hasil penjumlahan dari", x, "dan", y, "adalah", hasil)

```
Pada contoh di atas, kita mendefinisikan fungsi hitung_jumlah dengan dua parameter a dan b. Fungsi tersebut menghitung jumlah dari a dan b, lalu mengembalikan hasilnya dengan menggunakan kata kunci return. Setelah itu, kita memanggil fungsi tersebut dengan nilai x dan y sebagai argumen, dan menyimpan hasilnya ke dalam variabel hasil. Terakhir, kita mencetak hasilnya menggunakan fungsi print.

Selain itu, Python juga mendukung parameter fungsi yang opsional dan memiliki nilai default, seperti contoh berikut:

```python
def sapa(nama, sapaan="Halo"):
    print(sapaan, nama)

sapa("Andi") # akan mencetak "Halo Andi"
sapa("Budi", "Selamat pagi") # akan mencetak "Selamat pagi Budi"

```
Pada contoh di atas, fungsi sapa memiliki dua parameter, yaitu nama dan sapaan. Namun, parameter sapaan memiliki nilai default yaitu "Halo". Jika kita memanggil fungsi sapa hanya dengan satu argumen nama, maka fungsi akan mencetak "Halo" diikuti dengan nama. Namun, jika kita memanggil fungsi sapa dengan dua argumen, maka fungsi akan mencetak sapaan diikuti dengan nama.

Selain itu, Python juga mendukung fungsi lambda, yaitu fungsi anonim yang didefinisikan secara langsung tanpa nama. Berikut ini adalah contoh penggunaan fungsi lambda untuk menghitung kuadrat dari sebuah bilangan:

```python
kuadrat = lambda x: x * x
print(kuadrat(5)) # akan mencetak 25

```
Pada contoh di atas, kita mendefinisikan fungsi lambda dengan parameter x dan mengembalikan nilai x * x. Setelah itu, kita memanggil fungsi lambda tersebut dengan nilai 5 sebagai argumen dan mencetak hasilnya.

Itulah beberapa contoh penggunaan fungsi di Python, dari definisi fungsi standar hingga fungsi lambda. Fungsi sangat penting dalam Python dan digunakan secara luas dalam pengembangan aplikasi.

