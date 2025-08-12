import os
def header():
    '''fungsi header'''
    os.system('cls')
    print(f'{'SELAMAT DATANG DI PROGRAM' : ^40}')
    print(f'{'DATA REPORT' : ^40}')
    print(f'{'STOK MATERIAL GUDANG' : ^40}')
    print(f'{'='*40 : ^40}')

menuList = ['1. Report Stock Material Gudang',
            '2. Menambah Data Material Gudang',
            '3. Mengubah Data Material Gudang', 
            '4. Menghapus Data Material Gudang',
            '5. Keluar']



stockgudang = [
    {'SN' : '001', 'NAMAMATERIAL' : 'PENSIL', 'SPESIFIKASI' : 'JOYKO', 'JENISMATERIAL' : 'ATK', 'POSISI' : 'A1-1-1-1'},
{'SN' : '002', 'NAMAMATERIAL' : 'PRINTER', 'SPESIFIKASI' : ' Epson L3210 ', 'JENISMATERIAL' : 'ATK', 'POSISI' : 'A1-1-1-2'},
{'SN' : '003', 'NAMAMATERIAL' : 'BAUT', 'SPESIFIKASI' : 'M16x5cm ', 'JENISMATERIAL' : 'MATERIAL KONSUMABEL', 'POSISI' : 'A1-1-2-1'},
{'SN' : '004', 'NAMAMATERIAL' : 'TANG KOMBINASI', 'SPESIFIKASI' : '6"', 'JENISMATERIAL' : 'MATERIAL KONSUMABEL', 'POSISI' : 'A1-1-2-2'},
{'SN' : '005', 'NAMAMATERIAL' : 'SELANG AIR', 'SPESIFIKASI' : '1" @50m', 'JENISMATERIAL' : 'MATERIAL KONSUMABEL', 'POSISI' : 'A1-1-4-4'},
{'SN' : '006', 'NAMAMATERIAL' : 'FUEL', 'SPESIFIKASI' : 'B40', 'JENISMATERIAL' : 'RAW MATERIAL', 'POSISI' : 'A3'},
{'SN' : '007', 'NAMAMATERIAL' : 'BUKU TULIS', 'SPESIFIKASI' : 'SIKOLA , 38 LEMBAR', 'JENISMATERIAL' : 'ATK', 'POSISI' : 'A1-1-1-3'},
{'SN' : '008', 'NAMAMATERIAL' : 'SEPATU SAFETY', 'SPESIFIKASI' : 'KRUSHER (40)', 'JENISMATERIAL' : 'APD', 'POSISI' : 'A2-1-1'},
{'SN' : '009', 'NAMAMATERIAL' : 'SERAGAM', 'SPESIFIKASI' : 'M', 'JENISMATERIAL' : 'APD', 'POSISI' : 'A2-2-1'},
{'SN' : '010', 'NAMAMATERIAL' : 'MASKER', 'SPESIFIKASI' : 'KN95', 'JENISMATERIAL' : 'APD', 'POSISI' : 'A1-3-1'}
]

header()
def reportdata() :
    userinput1 = '1'
    while userinput1 != '3':
        print('\n===REPORT STOK MATERIAL===\n')
        print('1. Tampilkan Semua Stok Material')
        print('2. Tampilkan Stok Material Sesuai SN')
        print('3. Tampilkan Jenis Material')
        print('4. Kembali ke Menu Utama')
        userinput1 = input(f'Silahkan pilih menu (Masukkan angka 1-3) : ')
        if userinput1 == '1' :
            print('Tampilkan Semua Stok Material')
            if len(stockgudang) == 0 :
                print('Data Stok Kosong')
            else :
                for index, value in enumerate(stockgudang) :
                    print(f'{index+1:4}. SN : {value['SN']} | Nama Material : {value['NAMAMATERIAL']}| Spesifikasi : {value['SPESIFIKASI']}   | Jenis Material : {value['JENISMATERIAL']} | Posisi : {value['POSISI']} ')
            continue
        elif userinput1 == '2' :
            print('Tampilkan Stok Material Sesuai SN')
            if len(stockgudang) == 0 :
                print('Data Stok Kosong')
            else :
                sninput = (input('Masukkan SN :'))
                for index, value in enumerate(stockgudang) :
                    if value['SN'] == sninput :
                        print(f'{index+1}. SN : {value['SN']} ,\nNama Material : {value['NAMAMATERIAL']} , \nSpesifikasi : {value['SPESIFIKASI']} , \nJenis Material : {value['JENISMATERIAL']} , \nPosisi : {value['POSISI']} ')
                        break
                else :
                    print('\n***Data stok yang Anda cari tidak ditemukan***')
            continue
        elif userinput1 == '3' :
            print('Tampilkan Jenis Material')
            a = []
            for index,value in enumerate(stockgudang) :
                datajenismaterial = print(value['JENISMATERIAL'])
                a.append(datajenismaterial)
                print(a)
        elif userinput1 == '4' :
            quit
        else :
            print('\n***Menu yang Anda masukkan salah***')


def adddata() :
    userinput2 = '1'
    while userinput2 != '2':
        print('\n====TAMBAH DATA STOK====\n')
        print('1. Tambah Data Material')
        print('2. Kembali ke Menu Sebelumnya')
        userinput2 = input(f'Silahkan pilih menu (Masukkan angka 1-2) : ')
        if userinput2 == '1':
            datapertama = input(f'Masukkan data SN : ')
            for index, value in enumerate(stockgudang) :
                if value['SN'] == datapertama :
                    print(f'{index+1}. SN : {value['SN']} ,\nNama Material : {value['NAMAMATERIAL']} , \nSpesifikasi : {value['SPESIFIKASI']} , \nJenis Material : {value['JENISMATERIAL']} , \nPosisi : {value['POSISI']} ')
                    print('\n***Data sudah ada***')
                    break
            else :
                datakedua = input(f'Masukkan data Nama Material : ')
                dataketiga = input(f'Masukkan data Spesifikasi : ')
                datakeempat = input(f'Masukkan data Jenis Material : ')
                datakelima = input(f'Masukkan data Posisi : ')
                save1 = input(f'Apakah sudah yakin ? (y/n) : ')
                if save1 == 'y' :
                    #memasukkan ke database
                    newdata = {'SN' : datapertama, 'NAMAMATERIAL' : datakedua, 'SPESIFIKASI' : dataketiga, 'JENISMATERIAL' : datakeempat, 'POSISI' : datakelima}
                    stockgudang.append(newdata)
                    print('\n***data berhasil disimpan***')
                else :
                    print( '\n***Data tidak disimpan***')
        elif userinput2 == '2' :
            quit
        else :
            print('\n***Menu yang Anda masukkan salah***')
def updatedata() :
    userinput3 = 1
    while userinput3 != '2': 
        print('\n=====UBAH DATA STOK=====\n')
        print('1. Ubah Data Material')
        print('2. Kembali ke Menu Sebelumnya')
        userinput3 = input(f'Silahkan pilih menu (Masukkan angka 1-2) : ')
        if userinput3 == '1':
            sninput2 = (input('Masukkan SN :'))
            for index, value in enumerate(stockgudang) :
                if value['SN'] == sninput2 :
                    print(f'{index+1}. --SN : {value['SN']} ,\n--Nama Material : {value['NAMAMATERIAL']} , \n--Spesifikasi : {value['SPESIFIKASI']} , \n--Jenis Material : {value['JENISMATERIAL']} , \n--Posisi : {value['POSISI']} ')
                    print('1. Nama Materail')
                    print('2. Spesifikasi')
                    print('3. Jenis Material')
                    print('4. Posisi')
                    print('Kolom yang bisa diedit')
                    kolom = input(f'Masukkan Nomor yang ingin diubah : ')
                    if kolom == '1' :
                        kolomedit = input(f'Masukkan Data yang baru :')
                        value['NAMAMATERIAL']  = kolomedit
                        save2 = input(f'Apakah sudah yakin ? (y/n) : ')
                        if save2 == 'y' :
                            print('\n***Data Berhasil disimpan***')
                        else :
                            print('\n***Data tidak disimpan***')
                    elif kolom == '2' :
                        kolomedit = input(f'Masukkan Data yang baru :')
                        value['SPESIFIKASI']  = kolomedit
                        save2 = input(f'Apakah sudah yakin ? (y/n) : ')
                        if save2 == 'y' :
                            print('\n***Data Berhasil disimpan***')
                        else :
                            print('\n***Data tidak disimpan***')
                    elif kolom == '3' :
                        kolomedit = input(f'Masukkan Data yang baru :')
                        value['JENISMATERIAL']  = kolomedit
                        save2 = input(f'Apakah sudah yakin ? (y/n) : ')
                        if save2 == 'y' :
                            print('\n***Data Berhasil disimpan***')
                        else :
                            print('\n***Data tidak disimpan***')
                    elif kolom == '4' :
                        kolomedit = input(f'Masukkan Data yang baru :')
                        value['POSISI']  = kolomedit
                        save2 = input(f'Apakah sudah yakin ? (y/n) : ')
                        if save2 == 'y' :
                            print('\n***Data Berhasil disimpan***')
                        else :
                            print('\n***Data tidak disimpan***')
                    else :
                        print('\n***Data yang dimasukkan tidak sesuai***')
            
                    break
                else :
                    print('\n***Data tidak ditemukan***')
                    break
        elif userinput3 == '2' :
            quit
        else :
            print('\n***Menu yang Anda masukkan salah***')

def deletdata() :
    userinput4 = '1'
    while userinput4 != '2': 
        print('\n====HAPUS DATA STOK====\n')
        print('1. Hapus Data Material')
        print('2. Kembali ke Menu Sebelumnya')
        userinput4 = input(f'Silahkan pilih menu (Masukkan angka 1-2) : ')
        if userinput4 == '1':
            sninput3 = (input('Masukkan SN :'))
            for index, value in enumerate(stockgudang) :
                if value['SN'] == sninput3 :
                    save3 = input('Apakah anda yakin untuk menghapus data ? (y/n) : ')
                    if save3 == 'y' :
                        posisiindex =  stockgudang.index(value)
                        stockgudang.pop(posisiindex)
                        print('\n***data berhasil dihapus***')
                    else :
                        print( '\n***Data tidak dihapus***')
                    break
                else :
                    print('\n***Data tidak ditemukan***')
                    break   
        elif userinput4 == '2' :
            quit
        else :
            print('\n***Menu yang Anda masukkan salah***')

userInput = 1
while userInput != '5':
    print(f'\n===DATA REPORT STOK MATERIAL GUDANG===\n')
    for menu in menuList :
        print(menu)
    userInput = input('Silahkan pilih menu (pilih angka 1-5) = ')
    if userInput == '1' :
        reportdata()
    elif userInput == '2' :
        adddata()
    elif userInput == '3' :
        updatedata()
    elif userInput == '4' :
        deletdata()
    elif userInput == '5' :
        print('\n===Anda sudah keluar dari Aplikasi===\n')
        quit
    else :
        print('***Data yang anda masukkan tidak tersedia***')
   




            







    