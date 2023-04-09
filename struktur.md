# PYTHON 101 BY HIMATIKA

## struktur data ada List, tuple, dan set adalah tiga jenis struktur data yang umum digunakan dalam pemrograman:

- List adalah struktur data yang memungkinkan kita untuk menyimpan kumpulan data dengan tipe yang berbeda dalam satu variabel. List bersifat mutable, artinya isi list dapat diubah setelah dibuat.

- Tuple adalah struktur data yang mirip dengan list, namun bersifat immutable atau tidak bisa diubah setelah dibuat. Tuple digunakan untuk menyimpan data yang bersifat tetap atau konstan.

- Set adalah struktur data yang memungkinkan kita untuk menyimpan kumpulan data unik (tidak ada duplikasi) dalam satu variabel. Set bersifat mutable dan memiliki sifat matematika seperti union, intersection, dan difference.

## Dalam penggunaannya, list, tuple, dan set dapat digunakan untuk menyimpan, mengelola, dan memanipulasi data dengan lebih efisien.

## List

### List merupakan tipe data mutable, artinya kita dapat mengubah, menambah ataupun menghapus elemen

```python
var_list = [7, "Jakarta", 8, 9, "Bandung", "Surabaya"]
print(var_list[2])
print(var_list[-3])
print(var_list[0])
print(var_list[-3:])
print(var_list[:3])
```

### Menambah list

```python
kota = ["Jakarta", "Bandung", "Semarang"]
print(kota)
kota.append("Malang")
print(kota)
```

### Menghapus list

```python
del kota[2]
print(kota)
```

## Tuple

### Tuple bersifat terurut (ordered) dan immutable

```python
var_tuple = ("Jakarta", 2, "Bandung", "Semarang", 4)
print(type(var_tuple))
```

### Proses slicing

```python
print(var_tuple[2])
print(var_tuple[1:4])
print(var_tuple[:3])
```

## Set

### Set bersifat unordered (tidak berurutan)

### Contoh pengoperasian dalam himpunan matematika

```python
var_set1 = {4, 1, 2, 3, 5, 4}
var_set2 = {5, 7, 6, 8, 8}

print(var_set1.intersection(var_set2))
print(var_set1.union(var_set2))
print(var_set1.difference(var_set2))
```

### Walaupun tidak dapat diubah, tapi Set dapat ditambah ataupun dihapus elemennya

```python
var_set = {4, 1, 2, 3, 5, 5, 6}
print(var_set)
```

### menghapus

```python
var_set.remove(3)
print(var_set)
```

### menambah

```python
var_set.add(11)
print(var_set)
```
