# Dinda Mutia
# 065002500020
# Kamis, 05 Novemeber 2025

def cek_kabisat (tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False 
    
def get_jumlah_hari(bulan, tahun):
    if bulan == 2:
        if cek_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in (4, 6, 9, 11):
        return 30
    else: 
        return 31
        
print("Program ini akan menentukan jumlah hari dalam bulan tertentu")
while True:
    print("Masukan 0 untuk mengehentikan program")

    bulan_input= int(input("Masukan bullan (1-12): "))
    if bulan_input == 0:
        print("Terima kasih sudah menggunakan program saya, samapai berjumpa lagi.")
        break
    if 1 <= bulan_input <= 12:

        if bulan_input == 2:
            tahun_input = int(input("Masukan tahun (e.g., 2021): "))
            hari = get_jumlah_hari(bulan_input, tahun_input)
        else:
            hari = get_jumlah_hari(bulan_input, 0)

        print(f"{hari} hari dalam sebulan")


