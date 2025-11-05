# Dinda Mutia
# 065002500020
# Kamis, 30 Oktober 2025

def konversi_nilai(huruf):
    huruf = huruf.upper()  
    if huruf == 'A':
        return 4.00
    elif huruf == 'A-':
        return 3.75
    elif huruf == 'B+':
        return 3.50
    elif huruf == 'B':
        return 3.00
    elif huruf == 'B-':
        return 2.75
    elif huruf == 'C+':
        return 2.50
    elif huruf == 'C':
        return 2.00
    elif huruf == 'C-':
        return 1.75
    elif huruf == 'D':
        return 1.50
    elif huruf == 'E':
        return 1.25
    else:
        return 0  

def rata_rata_nilai(daftar_nilai):
    if not daftar_nilai:
        return 0
    total = 0
    for nilai in daftar_nilai:
        total += konversi_nilai(nilai)
    return total / len(daftar_nilai)