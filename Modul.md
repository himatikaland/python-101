# PYTHON 101 BY HIMATIKA

## Sejarah Modul
Modul adalah komponen penting dalam pemrograman yang memungkinkan programmer untuk mengelompokkan kode berdasarkan fungsionalitasnya dan menggunakannya kembali di tempat lain dalam program atau bahkan dalam program lain.

Konsep modul sudah ada dalam bahasa pemrograman sejak awal, tetapi terkadang dikenal dengan istilah yang berbeda seperti "library" atau "package". Bahasa pemrograman Fortran, salah satu bahasa pemrograman tertua, telah menggunakan modul sejak 1960-an. Bahasa pemrograman COBOL, BASIC, dan Pascal juga telah menggunakan konsep modul sejak lama.

Dalam bahasa pemrograman modern seperti Python, konsep modul sangat penting dan banyak digunakan. Pada awalnya, Python hanya menyediakan beberapa modul standar yang terintegrasi, seperti modul math untuk operasi matematika, modul os untuk interaksi dengan sistem operasi, dan modul sys untuk mengakses informasi tentang interpreter Python itu sendiri.

Namun, seiring waktu, banyak modul lain yang dikembangkan oleh komunitas pengembang Python dan dibagikan melalui repositori seperti PyPI (Python Package Index). Saat ini, ada ribuan modul dan paket yang tersedia di PyPI, dan bahkan modul dan paket yang dibuat oleh pengembang lain dapat diimpor dan digunakan di program Python.

Modul dalam Python sangat berguna untuk menghindari duplikasi kode, meningkatkan keterbacaan kode, dan memungkinkan pengembang untuk fokus pada fungsi tertentu dari program tanpa harus memikirkan semua detail implementasi. Modul juga memungkinkan pengembang untuk mengorganisir kode mereka dengan cara yang lebih terstruktur dan mudah dipahami.

Dalam ringkasan, konsep modul sudah ada sejak lama dalam pemrograman dan saat ini merupakan bagian integral dari bahasa pemrograman modern seperti Python. Modul memungkinkan programmer untuk mengelompokkan kode berdasarkan fungsionalitasnya dan menggunakannya kembali di tempat lain dalam program atau bahkan dalam program lain.

## Implementasi Modul pada Python
Modul adalah bagian penting dari bahasa pemrograman Python, yang memungkinkan pengguna untuk mengelompokkan kode berdasarkan fungsionalitasnya dan menggunakannya kembali di tempat lain dalam program atau bahkan dalam program lain.

Untuk mengimplementasikan modul pada Python, pertama-tama kita perlu membuat file Python terpisah yang berisi fungsi, variabel, dan kelas yang ingin kita kemas sebagai modul. Nama file harus diakhiri dengan ekstensi ".py". Misalnya, jika kita ingin membuat modul yang berisi fungsi matematika, kita dapat membuat file bernama "math_functions.py".

Berikut adalah contoh isi file "math_functions.py":

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

```
Setelah file modul dibuat, kita dapat mengimpor modul ke dalam program Python utama dengan menggunakan pernyataan "import". Misalnya, jika kita ingin mengimpor modul "math_functions" ke dalam program utama, kita dapat menulis kode berikut:

```py
import math_functions

print(math_functions.add(2, 3))
print(math_functions.multiply(4, 5))

```
Kita juga dapat mengimpor fungsi atau variabel tertentu dari modul menggunakan sintaks "from ... import". Misalnya, jika kita hanya ingin mengimpor fungsi "add" dari modul "math_functions", kita dapat menulis kode berikut:

```csharp
from math_functions import add

print(add(2, 3))
```
Jika kita ingin memberikan alias untuk modul atau fungsi yang diimpor, kita dapat menggunakan sintaks "as". Misalnya, jika kita ingin memberikan alias untuk modul "math_functions", kita dapat menulis kode berikut:

```python
import math_functions as mf

print(mf.add(2, 3))
```
Dengan menggunakan modul dalam Python, kita dapat memisahkan kode menjadi bagian yang lebih kecil dan lebih mudah dikelola, meningkatkan keterbacaan kode, menghindari duplikasi kode, dan memungkinkan pengembang untuk fokus pada fungsi tertentu dari program tanpa harus memikirkan semua detail implementasi.