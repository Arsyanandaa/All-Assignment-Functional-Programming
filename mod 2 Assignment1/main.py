nilai = [70, 80, 85]

tertinggi = nilai[0]
for x in nilai:
    if x > tertinggi:
        tertinggi = x
print("Imperatif : ", tertinggi)
print("Deklaratif : ", max(nilai))