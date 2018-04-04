#menginput nama,Nim dan Nilai
nama=raw_input("Masukkan Nama         : ")
nim=input("Masukkan NIM          : ")
uts=input("Masukkan Nilai UTS    : ")
uas=input("Masukkan Nilai UAS    : ")
tugas=input("Masukkan Nilai Tugas  : " )

Uts=uts*40/100;
Uas=uas*40/100;
Tugas=tugas*20/100;
#Formula mencari nilai akhir
nilai_akhir=Uts+Uas+Tugas;

#Menampilkan Output nama, Nim dan Nilai yang telah diinput
print "\nNama         : %s" %nama
print "NIM          : %s" %nim
print "Nilai UTS    : %d" %uts
print "Nilai UAS    : %d" %uas
print "Nilai Tugas  : %d" %tugas
print "Nilai Akhir  :" ,float(nilai_akhir)
#Kondisi If untuk menentukan nilai huruf
if nilai_akhir >=80 :
    print "\nNilai Huruf  : A"
elif nilai_akhir >=70 :
    print "\nNilai Huruf  : B"
elif nilai_akhir >=55 :
    print "\nNilai Huruf  : C"
elif nilai_akhir >=40 :
    print "\nNilai Huruf  : D"
elif nilai_akhir <=39 :
    print "\nNilai Huruf  : E"
#Kondisi If untuk menentukan Keterangan LULUS atau TIDAK LULUS
if nilai_akhir >=60 :
    print "Keterangan   : LULUS"
else :
    print "Keterangan   : TIDAK LULUS"
