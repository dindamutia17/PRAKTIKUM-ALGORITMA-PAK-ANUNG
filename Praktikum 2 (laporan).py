# Dinda Mutia
# 065002500020
# Kamis, 25 September 2025

import math
print("Silahkan isi lattitude dan longitudenya untuk menentukan jarak antara 2 titik yang dicari:")
R= 6371
titik_1= str(input("Masukan nama titik pertama permukaannya = "))
titik_2= str(input("Masukan nama titik kedua permukaannya = "))
lat1 = float(input("Masukan lattitude 1 = "))
lon1 = float(input("Masukan longitude 1 = "))
lat2 = float(input("Masukan lattitude 2 = "))
lon2 = float(input("Masukan longitude 2 = "))
lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)
dlon = (lon2_rad - lon1_rad)
dlat = (lat2_rad - lat1_rad)
a = (math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2) 
c = 2 * math.atan2 (math.sqrt (a), math.sqrt (1 - a))
jarak =  R * c
print(f"Jarak antara {titik_1} dan {titik_2} adalah {jarak} kilometer ")