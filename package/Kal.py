def tambah():
    print ('\t1. Penjumlahan')
    a = int(input('\tMasukan Nilai : '))
    b = int(input('\tMasukan Nilai : '))
    c = a+b
    print ("\tHasilnya : " , c)
def kurang():
    print ('\t2. Pengurangan')
    a = int(input('\tMasukan Nilai : '))
    b = int(input('\tMasukan Nilai : '))
    c = a-b
    print ("\tHasilnya : " , c)
def bagi():
    print ('\t3. Pembagian')
    a = int(input('\tMasukan Nilai : '))
    b = int(input('\tMasukan Nilai : '))
    c = a/b
    print ("\tHasilnya : " , c)
def kali():
    print ('\t4. Pengalian')
    a = int(input('\tMasukan Nilai : '))
    b = int(input('\tMasukan Nilai : '))
    c = a*b
    print ("\tHasilnya : " , c)

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
        
def menu():
    print("\tKalkulator Sederhana yang gak ribet ^^ ")
    print(" ")
    print("\t1. Penjumlahan")
    print("\t2. Pengurangan")
    print("\t3. Pembagian")
    print("\t4. Pengalian")
    print(" ")
    print("\tPilih salah 1 , kalo salah 4 kebanyakan : ")
    print(" ")
    pil = input("\tJadi berapa ?")
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else :
        print("\tEttt .. yang bener ! Coba lagi dah !")

menu ()
tanya ()
tanya2 ()
