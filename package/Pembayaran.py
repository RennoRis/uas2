def spp() :
    bulan = int(input("\n\t Jumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 350000 * bulan
    print("***************************************")
    print("\tTotal bayar spp Rp. 350.000 " , bulan ," = Rp. ",total)

def uas() :
    matkul = int(input("\n\t Jumlah mata kuliah = "))
    matkul = float(matkul)
    byr_uas = 50000*matkul
    print("***************************************")
    print("\tTotal bayar uas Rp. 50000*", matkul ," = Rp. ",byr_uas)

def uts() :
    matkul_uts = int(input("\n\t Jumlah mata kuliah = "))
    matkul_uts = float(matkul_uts)
    byr_uts = 25000*matkul_uts
    print("***************************************")
    print("\tTotal bayar uas Rp. 25000*",matkul_uts," = Rp. ",byr_uts)

def spp_uas() :
    bulan = int(input("\n\t Jumlah bulan yang di bayar = "))
    matkul = int(input("\n\t Jumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 350000 *bulan
    byr_uas = 50000*matkul
    total = total_spp + byr_uas + 5000
    print("\tTotal bayar spp Rp. 350000*",bulan," = Rp. ",total_spp)
    print("\tTotal bayar uas Rp. 50000*",matkul," = Rp. ",byr_uas)
    print("\tBiaya tambahan server Rp. 5000")
    print("***************************************")
    print("\tTotal yang harus di bayar : ",total )

def spp_uts() :
    bulan = int(input("\n\t Jumlah bulan yang di bayar = "))
    matkul = int(input("\n\t Jumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 350000 *bulan
    byr_uts = 25000*matkul
    total = total_spp + byr_uts + 5000
    print("\tTotal bayar spp Rp. 350000*",bulan," = Rp. ",total_spp)
    print("\tTotal bayar uas Rp. 25000*",matkul," = Rp. ",byr_uts)
    print("\tBiaya tambahan server Rp. 5000")
    print("***************************************")
    print("\tTotal yang harus di bayar : ",total )

def menu () :
    print("\n************************************")
    nama = input("\n\tMasukan nama : ")
    nim = input("\tMAsukan NIM : ")
    semester = input("\tMasukan Semester anda sekarang : ")
    print("\n\t---Pilihan Pembayaran---")
    print("\t1 * Pembayaran SPP")
    print("\t2 * Pembayaran UTS")
    print("\t3 * Pembayaran UAS")
    print("\t4 * Pembayaran SPP & UTS")
    print("\t5 * Pembayaran SPP & UAS")
    pilih = input("\n\tSilahkan Pilih :")
    if pilih == "1" :
        spp()
    elif pilih == "2" :
        uts()
    elif pilih == "3" :
        uas()
    elif pilih == "4" :
        spp_uts()
    elif pilih == "5" :
        spp_uas()
    else:
        print("\tPilih asem !")
        menu()

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

menu ()
tanya ()
tanya2 ()
