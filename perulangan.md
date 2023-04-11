# PYTHON 101 BY HIMATIKA

## Perulangan

Loop atau perulangan adalah sebuah konstruksi dalam pemrograman yang memungkinkan sebuah program untuk menjalankan serangkaian instruksi atau blok kode secara berulang-ulang sampai kondisi tertentu terpenuhi atau sampai batas perulangan tertentu tercapai. Dalam penggunaannya, loop dapat membantu menghemat penulisan kode dan memudahkan pengulangan tugas yang sama secara berulang kali. Ada beberapa jenis loop yang umum digunakan dalam pemrograman, seperti for loop, while loop, dan do-while loop.

### for loop -> digunakan ketika mengetahui banyaknya looping yang akan digunakan
```python
for i in range(0, 10):
    print("angka yang ke " + str(i))
```

### contoh lain

```python
array = ['Liverpool', 'Real Madrid', 'AC Milan']
for i in array:
    print(i)
```

### while loop -> digunakan ketika belum mengetahui banyaknya looping yang akan dilakukan

```python
i = 1
while i < 10:
    print(i)
    i += 1
```
