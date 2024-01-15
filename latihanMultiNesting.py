import datetime

mahasiswa = {
    "nama" : "nama01",
    "nim" : "123456",
    "jumlah sks" : 130,
    "beasiswa" : False,
    "lahir" : datetime.datetime(1999, 6, 11)
}

mahasiswaSatu = {
    "nama" : "nama02",
    "nim" : "654321",
    "jumlah sks" : 148,
    "beasiswa" : True,
    "lahir" : datetime.datetime(1998, 5, 10)
}

mahasiswaDua = {
    "nama" : "nama03",
    "nim" : "789012",
    "jumlah sks" : 125,
    "beasiswa" : False,
    "lahir" : datetime.datetime(2000, 7, 21)
}


dataMahasiswa = {
    'maha001' : mahasiswa,
    'maha002' : mahasiswaSatu,
    'maha003' : mahasiswaDua
}

print(f"{"KEY":<10} {"NAMA":<10} {"NIM":<9} {"SKS":<5} {"BEASISWA":<9} {"LAHIR":<10}")
print("-"*70)


for mahasiswa in dataMahasiswa:
    key = mahasiswa
    nama = dataMahasiswa[key]["nama"]
    nim = dataMahasiswa[key]["nim"]
    sks = dataMahasiswa[key]["jumlah sks"]
    beasiswaMahasiswa = dataMahasiswa[key]["beasiswa"]
    tglLahir = dataMahasiswa[key]["lahir"].strftime("%x")
    print(f"{key:<10} {nama:<10} {nim:<9} {sks:<5} {beasiswaMahasiswa:^9} {tglLahir:<10}")
