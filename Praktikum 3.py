# Dinda Mutia
# 065002500020
# Kamis, 02 Oktober 2025

print("Menghitung luas segitigas sama sisi, sama kaki, dan segitiga siku-siku")

print("")
a= float(input("Masukan pajang sisi a :"))
b= float(input("Masukan panjang sisi b : "))
c= float(input("Masukan panjang sisi c : "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Bukan segitiga")
elif a == b == c:
    print("Segitiga sama sisi")
elif a == b or a == c or b == c:
    print("Segitiga sama kaki")
elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b** 2 + c** 2 == a ** 2:
    print("Segitiga siku - siku")
else:
    print("Segitiga sembarang")