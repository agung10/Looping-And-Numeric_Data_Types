# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini

print("\t" * 5 ,"Mencetak Bilangan")
print("\t" * 4 , "=" * 25)

for i in range(100, 0, -2):
  print(i)

# PENJELASAN
# Menjalankan perintah untuk menampilkan angka 100 sampai sebelum angka 0 dengan setiap jaraknya bernilai dikurang 2

# ==========================================================

# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini

print("\n\n")
print("\t" * 5 ,"Menghitung Rata - Rata")
print("\t" * 4 , "=" * 30)

# Membuat variabel untuk menampung banyaknya angka
lotsNumber = int(input("Masukan banyaknya angka : "))
# Membuat list numbers
numbers = []
# Membuat variabel dengan nilai 0
total = 0

# Perulangan yang diambil dari banyak data
for i in range(lotsNumber):
  # Nilai yang akan diinput
  value = int(input("Masukan angka ke-%i: " % (i+1))) 
  # dimasukan ke dalam list data untuk dijumlahkan
  numbers.append(value)
  #penambahan nilai 
  total += numbers[i]

  # hasil
  result = total / lotsNumber

  # cetak hasil
print("\nRata-ratanya adalah", result)

# PENJELASAN
# Pertama kita diperintahkan untuk menginput banyak angka yang nilainya akan ditampung di lotsNumber, lalu for ini akan mengambil banyaknya angka yang diinput dari variabel lotsNumber, kemudian kita diminta untuk memasukan nilai angka sesuai banyaknya angka yang diperintahkan. Setelah itu nilai angka dimasukan ke list data menggunakan fungsi append(). Kemudian nilai akan ditambahkan dengan numbers[i], dan terakhir hasil akan dihitung dengan pembagian dari total/lotsNumber.

# ==========================================================

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

print("\n\n")
print("\t" * 6 ,"Mencetak Persegi")
print("\t" * 5 ,"=" * 24)

# Membuat variabel untuk menampung nilai bilangan bulat
numbers = int(input("Masukan sebuah bilangan bulat : "))

# perulangan dalam perulangan
for i in range(numbers):
  for j in range(numbers):
      print('*', end=' ')
  print()

# PENJELASAN
# Akan diberikan sebuah inputan masukan bilangan bulat, yang nanti kemudian akan dibuat bentuk persegi dengan karekter "*", sesuai dengan jumlah inputan.
# Jika memasukan angka 9, maka akan tampil karakter "*" dengan kolom dan baris yang sama yaitu 9