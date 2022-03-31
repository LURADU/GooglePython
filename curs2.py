list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

sort_list = sorted(list)
def_list = sorted(list, reverse=True)
slice_par = sort_list[1::2]
slice_impar = sort_list[::2]
list2 = []

for n in list:
    if n % 3 == 0:
        list2.append(n)
    else:
        continue

print("Lista principala:", list)
print("Lista crescatoare:", sort_list)
print("Lista descrescatoare:", def_list)
print("Numere pare:", slice_par)
print("Numere impare:", slice_impar)
print("Multipli de 3:", list2)
