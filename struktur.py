#struktur data
#List
#List merupakan tipe data mutable, artinya kita dapat mengubah, menambah ataupun menghapus elemen

var_list = [7, 'Jakarta', 8, 9, 'Bandung', 'Surabaya']
print(var_list[2])
print(var_list[-3])
print(var_list[0])
print(var_list[-3:])
print(var_list[:3])

#Menambah list
kota = ['Jakarta', 'Bandung', 'Semarang']
print(kota)
kota.append('Malang')
print(kota)

#Menghapus list
del kota[2]
print(kota)

#Tuple
#Tuple bersifat terurut (ordered) dan immutable

var_tuple = ('Jakarta', 2, 'Bandung', 'Semarang', 4)
print(type(var_tuple))

#Proses slicing
print(var_tuple[2])
print(var_tuple[1:4])
print(var_tuple[:3])

#Set
#Set bersifat unordered (tidak berurutan)
#Contoh pengoperasian dalam himpunan matematika
var_set1 = {4, 1, 2, 3, 5, 4}
var_set2 = {5, 7, 6, 8, 8}

print(var_set1.intersection(var_set2))
print(var_set1.union(var_set2))
print(var_set1.difference(var_set2))

#Walaupun tidak dapat diubah, tapi Set dapat ditambah ataupun dihapus elemennya
var_set = {4, 1, 2, 3, 5, 5, 6}
print(var_set)

#menghapus
var_set.remove(3)
print(var_set)

#menambah
var_set.add(11)
print(var_set)

