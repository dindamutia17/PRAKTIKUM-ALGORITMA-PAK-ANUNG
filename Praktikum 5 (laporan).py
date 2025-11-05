# Dinda Mutia
# 065002500020
# Kamis, 30 Oktober 2025

total_harga = 0.00
jumlah_tiket= int(input("Jumlah tiket: "))
for x in range(jumlah_tiket):
    umur= int(input("Masukan umur: "))
    if umur <= 2:
        total_harga += 0
        print("Gratis")
        print(f"Running total: {total_harga}")
    elif umur >= 3 and umur <= 12:
        total_harga += 14.00
        print("Harga $14.00")
        print(f"Running total: {total_harga}")
    elif umur >= 65:
        total_harga += 18.00
        print("Harga $18.00")
        print(f"Running total: {total_harga}")
    else:
        total_harga += 23.00
        print("Harga $23.00")
        print(f"Running total: {total_harga}")

bayar= float(input("Masukan jumlah uang: "))
kembalian= bayar - total_harga
print(f"Running kembalian: {kembalian}")