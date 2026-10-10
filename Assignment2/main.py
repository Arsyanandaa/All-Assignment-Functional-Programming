akun = {
    "nanda": "nanda123",
    "arsya": "arsya123",
    "abi": "abi123",
}

profil = {
    "nanda": {"nama": "Nanda", "telepon": "081234567890", "peran": "Peserta"},
    "arsya": {"nama": "Arsya", "telepon": "081298765432", "peran": "Peserta"},
    "abi":   {"nama": "Abi",   "telepon": "081311112222", "peran": "Peserta"},
}

catatan_latihan = [
    {"user_id": "nanda", "tanggal": "2026-10-01", "skill": "Reading",   "band": 6.0, "durasi": 60},
    {"user_id": "nanda", "tanggal": "2026-10-02", "skill": "Writing",   "band": 5.5, "durasi": 45},
    {"user_id": "nanda", "tanggal": "2026-10-03", "skill": "Listening", "band": 7.0, "durasi": 30},
    {"user_id": "arsya", "tanggal": "2026-10-01", "skill": "Speaking",  "band": 6.5, "durasi": 15},
    {"user_id": "arsya", "tanggal": "2026-10-02", "skill": "Reading",   "band": 7.0, "durasi": 60},
    {"user_id": "arsya", "tanggal": "2026-10-03", "skill": "Writing",   "band": 6.0, "durasi": 50},
    {"user_id": "abi",   "tanggal": "2026-10-01", "skill": "Listening", "band": 5.5, "durasi": 30},
    {"user_id": "abi",   "tanggal": "2026-10-02", "skill": "Speaking",  "band": 6.0, "durasi": 15},
    {"user_id": "abi",   "tanggal": "2026-10-03", "skill": "Reading",   "band": 6.5, "durasi": 60},
]

MENU = (
    "Registrasi", "Login", "Keluar",
    "Lihat Progres", "Catat Latihan", "Revisi Skor",
    "Hapus Latihan", "Lihat Profil", "Logout",
)

def tampilkan_menu(sudah_login):
    if sudah_login:
        pilihan = MENU[3:]
    else:
        pilihan = MENU[:3]

    print("\n=== MENU ===")
    nomor = 1
    for m in pilihan:
        print(nomor, m)
        nomor = nomor + 1
    return pilihan

def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan))
        except ValueError:
            print("Input harus angka! Coba lagi.")
        else:
            return nilai

def input_pilihan(pesan, jumlah):
    while True:
        try:
            n = int(input(pesan))
        except ValueError:
            print("Masukkan nomor, bukan huruf!")
        else:
            if n >=1 and n <= jumlah:
                return n
            print("Nomor tidak ada di menu")

def registrasi():
    username = (input("Username baru : "))
    if username in akun:
        print("Username sudah dipakai!")
        return
    password = input("Password : ")
    nama = input("Nama Lengkap : ")
    telepon = input("Nomor Telepon : ")

    akun[username] = password
    profil[username] = {"nama": nama, "telepon": telepon, "peran": "Peserta"}
    print("Registrasi Berhasil! Silahkan Login.")

def login():
        username = input("Username: ")
        password = input("Password: ")
        if username in akun and akun[username] == password:
            print(f"Login berhasil. Selamat datang, {profil[username]['nama']}!")
            return username
        print("Username atau password salah")
        return None

#session lock
def ambil_catatan_milik(user_id):
    milik = []

    for c in catatan_latihan:
        if c["user_id"] == user_id:
            milik.append(c)
    return milik

def lihat_progres(user_id):
    milik = ambil_catatan_milik(user_id)
    if milik == []:
        print("belum ada catatan latihan.")
        return milik
    print("\n=== PROGRES LATIHAN ===")
    nomor = 1
    for c in milik:
        print(nomor, c["tanggal"], c["skill"], "| Band:", c["band"], "| Durasi:", c["durasi"], "menit")
        nomor = nomor + 1
    return milik

def catat_latihan(user_id):
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    skill = input("Skill (Reading/Listening/Writing/Speaking): ")
    band = input_angka("Band score: ")
    durasi = int(input_angka("Durasi (menit): "))
    catatan_latihan.append({
        "user_id": user_id,
        "tanggal": tanggal,
        "skill": skill,
        "band": band,
        "durasi": durasi,
    })
    print("Catatan berhasil disimpan.")

def revisi_skor(user_id):
    milik = lihat_progres(user_id)
    if milik == []:
        return
    n = input_pilihan("Nomor catatan yang direvisi: ", len(milik))
    band_baru = input_angka("Band score baru: ")
    milik[n - 1]["band"] = band_baru
    print("Skor berhasil direvisi.")


def hapus_latihan(user_id):
    milik = lihat_progres(user_id)
    if milik == []:
        return
    n = input_pilihan("Nomor catatan yang dihapus: ", len(milik))
    catatan_latihan.remove(milik[n - 1])
    print("Catatan berhasil dihapus.")


def lihat_profil(user_id):
    p = profil[user_id]
    print("\n=== PROFIL ===")
    print("Username:", user_id)
    print("Nama    :", p["nama"])
    print("Telepon :", p["telepon"])
    print("Peran   :", p["peran"])

#session lock
user_login = None

while True:
    sudah_login = user_login != None
    pilihan = tampilkan_menu(sudah_login)
    n = input_pilihan("Pilih menu: ", len(pilihan))
    menu = pilihan[n - 1]

    if menu == "Registrasi":
        registrasi()
    elif menu == "Login":
        user_login = login()
    elif menu == "Keluar":
        print("Sampai jumpa!")
        break
    elif menu == "Lihat Progres":
        lihat_progres(user_login)
    elif menu == "Catat Latihan":
        catat_latihan(user_login)
    elif menu == "Revisi Skor":
        revisi_skor(user_login)
    elif menu == "Hapus Latihan":
        hapus_latihan(user_login)
    elif menu == "Lihat Profil":
        lihat_profil(user_login)
    elif menu == "Logout":
        print("Logout berhasil.")
        user_login = None

# Alasan struktur: list of dictionaries dipilih karena tiap catatan latihan
# punya beberapa atribut dengan tipe berbeda (str, float, int), dan jumlah
# catatan bisa bertambah/berkurang. Key "user_id" dipakai untuk mengunci
# data per akun (session lock).