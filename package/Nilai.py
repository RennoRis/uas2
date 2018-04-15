from texttable import Texttable

def menu() :
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    while(jawab == "y"):
        nama.append(input("Masukan Nama :"))
        nim.append(input("Masukan Nim  :"))
        nilai_tugas.append(input("Nilai Tugas  :"))
        nilai_uts.append(input("Nilai UTS    :"))
        nilai_uas.append(input("Nilai UAS    :"))
        jawab = input("Tambah data (y/t)?")
        no += 1
    for i in range(no):
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100) 
        table.add_rows([['No','Nama','NIM','TUGAS','UTS','UAS','AKHIR'],[i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])                                                                                                                                                                                                                                                                                                                                                
    print (table.draw())

def tanya():
    tanya = input("\n\t Kembali Ke Menu ? (y/t)")
    if tanya == "y":
        menu()
    elif tanya == "t":
        tanya2()
    else :
        print ("\n\tYang Bener Dong Ya apa Tidak !!")
        tanya()

def tanya2():
    tanya2 = input("\n\t Kembali Ke Menu Login ? (y/t)")
    if tanya2 == "y":
        from main import login
    elif tanya2 == "t":
        exit
    else :
        print ("\n\tYang Bener Dong Ya apa Tidak !!")
        tanya2()

menu()
tanya()
tanya2()
