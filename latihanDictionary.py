# latihan dictionary

import datetime
import os
import string
import random

mahasiswa_template = {
    "nama" : "nama",
    "nim" : 00000000,
    "jumlah_sks" : 0,
    "lahir" : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")

    print(f"{"SELAMAT DATANG" :^20}")
    print(f"{"DATA MAHASISWA":^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("Nama Mahasiswa : ")
    mahasiswa["nim"] = input("NIM : ")
    mahasiswa["jumlah_sks"] = input("Jumlah SKS : ")
    tahunLahir = int(input("Tahun Lahir : "))
    bulanLahir = int(input("Bulan Lahir : "))
    tanggalLahir = int(input("Tanggal Lahir : "))
    mahasiswa["lahir"] = datetime.datetime(tahunLahir, bulanLahir, tanggalLahir)

    key = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({key:mahasiswa})
    print(f"{"KEY":<10} {"NAMA":<10} {"NIM":<12} {"SKS":<5} {"LAHIR":<10}")
    print("-"*70)

    for mahasiswa in data_mahasiswa:
        key = mahasiswa
        nama = data_mahasiswa[key]["nama"]
        nim = data_mahasiswa[key]["nim"]
        sks = data_mahasiswa[key]["jumlah_sks"]
        tglLahir = data_mahasiswa[key]["lahir"].strftime("%x")
        print(f"{key:<10} {nama:<10} {nim:<12} {sks:<5} {tglLahir:<10}")

    print("\n")
    is_done = input("Apakah Ada Lagi? ") # ya/tidak
    if is_done == "tidak":
        break

print("\nAkhir Dari Program\n")