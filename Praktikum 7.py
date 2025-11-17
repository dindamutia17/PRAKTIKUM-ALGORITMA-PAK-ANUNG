# Dinda Mutia
# 065002500020
# Kamis, 13 Novemeber 2025

def cek_prima(angka_input):
    if angka_input <= 1:
        return False
        
    if angka_input == 2:
        return True
        
    for i in range(2, angka_input):
       
        if angka_input % i == 0:
            return False
            
    return True

def tampil_hasil_prima(angka, status_prima):
    if status_prima == True:
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")
        
angka_input = int(input("Masukkan angka: "))
status = cek_prima(angka_input)
tampil_hasil_prima(angka_input, status)