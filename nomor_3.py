Biaya_Pesan = 50000
Kebutuhan_Tahunan = 1000
Biaya_Simpan = 400
EOQ = int(((2 * Biaya_Pesan * Kebutuhan_Tahunan) / Biaya_Simpan) ** 0.5)

print(EOQ)