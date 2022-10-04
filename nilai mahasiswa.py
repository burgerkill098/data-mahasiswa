print("------------------------------------------")
print("PROGRAM MENGHITUNG NILAI AKHIR MAHASISWA ")
print("------------------------------------------")
nama=input("masukkan nama :")
nim=input("masukkan nim :")
kelas=input("masukkan kelas :")
matkul=input("msukkan mata kuliah :")
presensi=float(input("masukkan nilai presensi : "))
tugas=float(input("masukkan nilai tugas : "))
quis=float(input("masukkan nilai quis : "))
perkum=float(input("msukkan nilai peraktikum : "))
uts=float(input("masukkan nilai uts :"))
uas=float(input("msukkan nilai uas :"))

na=(presensi* 0.1 ) + (tugas *0.3 ) + (quis *0.1 ) + (perkum * 0.2) + (uts * 0.1 ) + (uas * 0.2 )

print("======================== HASIL PERHITUNGAN =====================================")

print("Nama :",nama)
print(" NIM :",nim)
print("Kelas :",kelas)
print("mata kuliah :",matkul)
print("Nilai Kehadiran :",presensi)
print("Nilai Tugas :",tugas)
print("Nilai Quis : ",quis)
print("Nilai Praktikum :",perkum)
print("Nilai UTS :",uts)
print("Nilai UAS : ",uas)

print(" Nilai Akhir :",na)

if na >= 81:
    print("bobot huruf : A ")
elif na>= 76 :
    print("bobot huruf : B+")
elif na>= 66 :
    print("bobot huruf : B")
elif na>= 61 :
    print("bobot huruf : C+")
elif na>= 51 :
    print("bobot huruf : C")
elif na>= 26 :
    print("bobot huruf : D")
elif na<= 25 :
    print("bobot huruf: E")

if na >= 51 :
    print("status : LULUS ")
else:
    print ("status : TIDAK LULUS")