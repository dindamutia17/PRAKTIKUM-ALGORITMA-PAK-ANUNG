# Dinda Mutia
# 065002500020
# Kamis, 20 November 2025

def pangkat(base, power):
    if power == 0:
        return 1
    elif power > 0:
        return base * pangkat(base, power - 1)
    else:
        return 1 / pangkat(base, -power)

while True:
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    angka = input("Masukkan Angka: ")
    if angka == "":
        print("Program Selesai")
        break

    base = int(angka)
    power = int(input("Masukkan Pangkatnya: "))

    hasil = pangkat(base, power)
    print(f"Hasilnya adalah: {hasil}\n")