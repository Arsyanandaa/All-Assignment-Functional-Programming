raw_grades = [
    ["Amel", 78, 80],
    ["Dika", 78, 82],
    ["Nisrina", 57, 65],
    ["Nayla", 60, 70],
    ["Fatih", 77, 72],
    ["Rani", 68, 55],
]


def hitungNilaiAkhir(data):
    hasil = []

    for x in data:
        final_nilai = round(x[1] * 0.4 + x[2] * 0.6, 2)
        x_baru = x + [final_nilai]
        hasil.append(x_baru)
    return hasil

def filterKelulusan(data):
    lulus = []
    tidakLulus = []

    for x in data:
        if x[2] >= 60 and x[3] >= 70:
            lulus.append(x[0])
        else:
            tidakLulus.append(x[0])

    return lulus, tidakLulus

hasilAkhir = hitungNilaiAkhir(raw_grades)
for s in hasilAkhir:
    print(s)

yangLulus, yangTidakLulus = filterKelulusan(hasilAkhir)
print("Lulus : ", yangLulus)
print("Tidak Lulus : ", yangTidakLulus)

data_tuple = tuple(yangTidakLulus)
print(data_tuple)
print(type(data_tuple))

def verify_student(data, nama):
    try:
        posisi = data.index(nama)
    except ValueError:
        print(f"Error: {nama} tidak ditemukan di dalam daftar.")
    else:
        print(f"{nama} ditemukan di posisi {posisi}.")

verify_student(data_tuple, "Nayla")
verify_student(data_tuple, "Dika")

def count_students_recursive(data, index=0):
    if data[index:] == ():
        return 0
    else:
        return 1 + count_students_recursive(data, index + 1)
print("Jumlah Mahasiswa : ", count_students_recursive(data_tuple))