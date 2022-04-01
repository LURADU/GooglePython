def add(*args):
    add2 = []
    for n in args:
        try:
            add2.append(int(n))
        except:
            continue
    suma = sum(add2)
    print("Numerele din tuple sunt:", add2)
    print("Suma este", suma)


add(1, 5, -3, 'abc', [12, 56, 'cad'])


def suma0_n(n):
    if n == 0:
        return 0
    else:
        return n + suma0_n(n - 1)
print("Suma este:" , suma0_n(28))


def citire():
    n = input("Introduceti de la tastatura:")
    if n.isdigit():
        return n
    else:
        return 0

print(citire())






