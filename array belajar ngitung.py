#deklarasi array
array = []
#membuat variabel total
total = 0
#membuat variable n untuk menampung jumlah array yang di inputkan

n =int(input("Masukan Jumlah Elemen Array :"))
for x in range(n) :
    #menginput nilai yang akan bertambah 1
    nilai = float(input("Masukan Nilai ke- {} :".format(x+1)))
    array.append(nilai)
    #maenampilkan jumlah dari nilai
    print("\nHasil nilai total adalah : {}".format(sum(array)))
    #menampilkan nilai rata rata
    print("Hasil rata rata adalah : {}".format(sum(array)/n))
