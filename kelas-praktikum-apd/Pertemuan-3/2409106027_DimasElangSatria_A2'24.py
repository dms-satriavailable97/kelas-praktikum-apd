# input("""
# =====================
# Kalkulator Sederhana)
# =====================   
      
# 1. +
# 2. -
# 3. *
# 4. /
# """)

# fitur = int(input("Pilih Fitur :"))
# match fitur :
#     case 1:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a + b
#         print(f"Hasil Pertambahan Angka 1 dan Angka 2 adalah {c}")
#     case 2:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a - b
#         print(f"Hasil Pengurangan Angka 1 dan Angka 2 adalah {c}")
#     case 3:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a * b
#         print(f"Hasil Perkalian Angka 1 dan Angka 2 adalah {c}")
#     case 4:
#         a = int(input("Masukkan Angka 1 : "))
#         b = int(input("Masukkan Angka 2 : "))
#         c = a / b
#         print(f"Hasil Pembagian Angka 1 dan Angka 2 adalah {c}")



# # Studi Kasus 1
# Toko buku Blue ingin membuat diskon buku kepada pembelinya yang membeli  minimal 5 buku dengan total pembelian lebih dari 100.000, sebesar 20%. Maka buatlah program diskon untuk membantu Toko buku blue

# buku = int(input("Masukkan jumlah buku = "))
# harga = int(input("Masukkan harga buku = "))
# diskon = 0.20
# total_harga = buku * harga


# if buku >= 5 and total_harga > 100000 :
#     harga_diskon = total_harga * diskon
#     total_harga_setelah_diskon = total_harga - harga_diskon
#     print(f"diskon yang diterima sebanyak {harga_diskon:}")
#     print(f"Anda harus membayar sebanyak {total_harga_setelah_diskon:} setelah mendapat diskon 20%")

# else : 
#     print("Anda tidak mendapat diskon")



# # Studi Kasus 2
# Pak Kades sedang mendata penduduknya berdasarkan jenis kelamin, buatlah program sederhana untuk menentukan jenis kelamin seseorang dengan menggunakan ternary operator.

# jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :")
# hasil = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"

# print(hasil)



# # Menghitung Nilai
# Nilai = int(input("Masukkan Nilai = "))
# if Nilai > 100 :
#     print("kondisi tidak memenuhi syarat")
# if Nilai >= 80 : 
#     if Nilai >= 90 and Nilai <= 100 :
#         print("Nilai anda A+")
#     if Nilai >= 80 and Nilai <= 89 :
#         print("Nilai anda A-")
# if Nilai >= 70 : 
#     if Nilai >= 75 and Nilai <= 79 :
#         print("Nilai anda B+")
#     if Nilai >= 70 and Nilai <= 74 :
#         print("Nilai anda B-")
# else :
#     print("kondisi tidak memenuhi syarat")

