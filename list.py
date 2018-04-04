nm = []
nim =[]
tgs =[]
uts =[]
uas =[]
Stop = False
no=0
while(not Stop):
    nama = raw_input("Nama:")
    nm.append(nama)
    Nim = int(raw_input("Nim:"))
    nim.append(nim)
    Tugas = int(raw_input("Tugas:"))
    tgs.append(tgs)
    Uts = int(raw_input("Uts:"))
    uts.append(uts)
    Uas = int(raw_input("Uas:"))
    uas.append(uas)
    data = raw_input("Tambah Data lagi?[Y/T]")
    if (data == 'T'):
        Stop = True
    akhir = float(Tugas+Uts+Uas)/3
    no+=1
garis = "======================================================================"
print garis
print "|   Nama   |   NIM   |   TUGAS |   UTS   |   UAS  |   Akhir   |"
print garis
print " |",nama,"  |  ",Nim,"   |  ",Tugas,"   |  ",Uts,"   |  ",Uas,"   |  ",akhir,  "|"



    
 
