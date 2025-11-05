# Dinda Mutia
# 065002500020
# Kamis, 09 Oktober 2025

print("Program menghitung jumlah hari dalam suatu bulan\n")
bulan = int(input("Masukan bulan (1-12): "))
while bulan < 1 or bulan > 12:
    print("Bulan tidak valid coba lagi")
    bulan = int(input("Masukkan bulan (1-12): "))

tahun = int(input("Masukan tahun: "))
if bulan in (1, 3, 5, 7, 8, 10, 12):
    hari = 31
elif bulan in (4, 6, 9, 11):
    hari = 30
else:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 ==0):
        hari = 29
    else:
        hari = 28
print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari")