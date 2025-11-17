# Dinda Mutia
# 065002500020
# Kamis, 13 November 2025

def dapatkan_akhiran_ordinal(n):
    if n == 0:
        return 'th'

    if 10 <= (n % 100) <= 20:
        return 'th'
    
    digit_terakhir = n % 10
    
    if digit_terakhir == 1:
        return 'st'
    elif digit_terakhir == 2:
        return 'nd'
    elif digit_terakhir == 3:
        return 'rd' 
    else:
        return 'th'
   
    
print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    angka = int(input("masukkan angka: "))

    akhiran = dapatkan_akhiran_ordinal(angka)
    print(f"({angka}, '{akhiran}')")
    if angka == 0:
        print("terima kasih telah menggunakan program saya")
        break