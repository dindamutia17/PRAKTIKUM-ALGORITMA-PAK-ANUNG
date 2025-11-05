# Dinda Mutia
# 065002500020
# Program perhitungan diskon pembelanjaan 
# Kamis, 25 September 2025

print("----Program Perhitungan Diskonan Pembelanjaan USAKTIF---\n")
kupon_terpakai = False
nama = str(input("Masukan Nama: "))
nim = str(input("Masukan NIM: "))
total_belanja = float(input("Masukan Total Belanja Anda: "))
kupon = str(input("Bayar pakai kupon y/n: "))

if total_belanja < 0:
    print("!-Masukan total belanja dengan benar-!")
    exit()

if kupon not in ('y', 'n', 'Y', 'N', 'yes', 'no', 'Yes', 'No', 'YES', 'NO'):
    print("!-Masukan pilihan degan benar-!")
    exit()

if kupon == "y" or kupon == "yes":
    kode_kupon = str(input("Masukan Kode Kupon: "))
    if kode_kupon == "IKL6309":
        kupon_terpakai = True
    else:
       print("!-Maaf kode yang anda pakai salah atau expired-!") 
       exit()


if kupon_terpakai:
    diskon = int(100/100 * total_belanja)
    print("\n--SELAMAT ANDA MENDAPATKAN DISKON 100%--\n")
elif total_belanja >= 390000:
    diskon = int(80/100 * total_belanja)
    print("\n--SELAMAT ANDA MENDAPATKAN DISKON 80%--\n")
elif total_belanja >= 190000:
    diskon = int(60/100 * total_belanja)
    print("\n--SELAMAT ANDA MENDAPATKAN DISKON 60%--\n")
elif total_belanja >= 90000:
    diskon = int(40/100 * total_belanja)
    print("\n--SELAMAT ANDA MENDAPATKAN DISKON 40%--\n")
elif total_belanja >= 40000:
    diskon = int(20/100 * total_belanja)
    print("\n--SELAMAT ANDA MENDAPATKAN DISKON 20%--\n")
else:
    diskon = int(0/100 * total_belanja)
    print("\n--ANDA TIDAK MENDAPATKAN DISKON--\n")

if int(total_belanja - diskon) == 0:
    total = "GRATIS TIS TIS"
else:
    total = int(total_belanja - diskon)

print("-------------Rincian Belanja-------------")
print(f"{nama} - {nim}")
print(f"Total belanja anda: Rp.{total_belanja}")
print(f"Potongan harga: Rp.{diskon}")
print(f"Total pembayaran: Rp.{total}\n")
print("Terimakasih sudah belanja :)\n")