# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

#Key tidak boleh sama, tapi valuenya boleh (ketimpa yang paling bawah)
#pake koma kecuali yg terakhir

# daftar_buku = {}
# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"
# print(daftar_buku)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata["Social Media"]["Discord"])
# print(Biodata["KRS"][0:])
# print(Biodata.get('KRS'))
#kalau pke get pake kuurng biasa aja

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")
# i j bisa diganti
# for mapel, nilai in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Nilai["Sejarah"] = 100
# print(Nilai)

# Nilai.update(Nilai{"Biologi" : 80})
# print(Nilai)

# del Nilai["Kimia"]
# simpan = Nilai.pop("Fisika")
# print(Nilai)
# print(simpan)

# print("Jumlah data =", len(Nilai))

# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for penyanyi, playlist in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for lagu in playlist:
#         print(lagu)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# #Sebelum Dilakukan Perubahan
# print(mahasiswa)

# #Menambahkan Item pada Nested Dictionary
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[101]["Umur"]
# print(mahasiswa)


# STUDI KASUS 1
# mahasiswa = {
# 25 : {"Nama" : "Rasyid",  "Umur" : 19, "Nim" : 25, "Jurusan" : "Informatika", "Angkatan" : 34},
# }
# #Menambahkan Item pada Nested Dictionary
# mahasiswa[25]["Jenis Kelamin"] = "Pria"
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[25]["Nama"] = "Zifa"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[25]["Angkatan"]
# print(mahasiswa)


#STUDI KASUS 2
# Nilai = {
# "Matematika" : 90,
# "Fisika" : 80,
# "Biologi" : 80,
# "Kimia" : 70
# }

# total = sum (Nilai.values())
# print("Nilai total : ", total)
# rata = total / len(Nilai)
# print("Nilai Akhir : ", rata)