# ulang = 10 
# for i in range(ulang):  
#     print("Perulangan ke-" + str(i))

# for j in range(2,12,2) :
#     print("Halo")
# print ("Hai")

# print("Menu Rumah Makan Informatika 24 : ")
# print("----------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"] 
# for i in simpan: 
#     print(i)

# print("Menu Rumah Makan Informatika 24 : ")
# print("----------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"] 
# for i in simpan: 
#     print(i)
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}. {menu}")

# print("Menu Rumah Makan Informatika 24 : ")
# print("----------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"] 
# for i in range(len(simpan)) :
#     print(f"{i+1}. {simpan[i]}")

# for i in range(1, 4): 
#     for j in range(1, 4): 
#         print(f"{i} x {j} = {i * j}") 
#     print() 

# makanan = ["mie" , "sop", "bakso"]
# minuman = ["es teh", "air putih", "es jeruk"]
# for i in makanan: 
#     for j in minuman: 
#         print(f"{i} & {j}") 

# jawab = "ya"
# hitung = 0
# while (jawab == "ya" or jawab == "Ya") :
#     hitung += 1
#     jawab = input ("Ulang lagi tidak ?")
#     print(f"Total Perulangan : {hitung}")

# i = 0
# while i < 5 :
#     print (i)
#     i += 1

# i = 0
# while i < 5 :
#     print (i)
#     break
#     i += 1

# hitung = 0
# while True :
#     hitung += 1
#     ulang = input ("Masi ingin mengulang ?")
#     if ulang == "tidak" or ulang =="Tidak": 
#         print("Oke kita Udahan")
#         break 
#     print(f"Total Perulangan: {hitung}")

# hitung = 0
# while True :
#     hitung += 1
#     ulang = input ("Masi ingin lanjut ?")
#     if ulang == "y" or ulang =="Y": 
#         print("Oke kita lanjut")
#         continue

# print("Daftar bilangan ganjil dari 1-10") 
# for i in range(10): 
#     if i % 2 == 0: 
#         print(f"{i} genap")
#         continue 
#     else :
#         print(f"{i} ganjil")
#         continue

# Studi Kasus 
# 1. Buatlah program yang dapat menentukan dan menghitung jumlah bilangan prima 
# dengan range bilangan mulai dari 1! 
# 2. Buatlah program perulangan while yang menjumlahkan semua inputan integer positif, 
# jika diinput negatif maka program berhenti!

#studi kasus 1
# range_maksimal = int(input("Masukkan range maksimal: "))
# hitung_prima = 0

# for angka in range(1, range_maksimal):
#     angka += 1
#     apakah_prima = True  

#     for i in range(2, angka):
#         if angka % i == 0:
#             apakah_prima = False  
#             break
#     if apakah_prima == True:
#         print(f"{angka} prima")
#         hitung_prima += 1

# print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")

#studi kasus 2
# total = 0
# while True :
#     angka = int(input("Masukkan angka positif (input negatif jika ingin berhenti) : "))
#     if angka < 0 :
#         break
#     total += angka
# print("jumlah total adalah : ", total)


