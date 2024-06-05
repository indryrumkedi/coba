# contoh.py
from bangun_ruang import balok, kubus_limas, bola

# Contoh penggunaan
print("Balok:")
print("Volume:", balok.hitung_volume(2, 3, 4))
print("Luas Permukaan:", balok.hitung_luas_permukaan(2, 3, 4))

print("\nKubus:")
print("Volume:", kubus_limas.hitung_volume(5))
print("Luas Permukaan:", kubus_limas.hitung_luas_permukaan(5))

print("\nBola:")
print("Volume:", bola.hitung_volume(7))
print("Luas Permukaan:", bola.hitung_luas_permukaan(7))