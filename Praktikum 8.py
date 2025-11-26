# Dinda Mutia
# 065002500020
# Kamis, 20 Novemeber 2025

def jumlah_rekursif(n, total=0, index=1):
    if n == 0:
        return total
    
    angka = int(input(f"Masukkan bilangan ke-{index}: "))
    return jumlah_rekursif(n - 1, total + angka, index + 1)

jumlah = int(input("Masukkan Jumlah: "))
hasil = jumlah_rekursif(jumlah)

print(f"Hasil dari penjumlahan adalah: {hasil}")