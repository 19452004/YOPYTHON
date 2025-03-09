from services import dataBase as DB
from time import sleep

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = int(input('harga_barang: '))
    stok_barang = int(input("stok barang: "))
    
    DB.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
    
def check():
    items = DB.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        
        print(f'''
kode {kode_barang}
{nama_barang} | Rp {harga_barang}
Stok: {stok_barang}
              ''')
  
def exit_program():
    print("program akan dihentikan")
    sleep(1)
    print('3...')
    sleep(2)
    print('2..')
    sleep(1)
    print('1.')
    print('program berhasil di hentikan')
    exit()
    
def start():
    while(True):
        menu = int(input("MENU:\n\n1. Tambah Barang\n2. Cek Barang\n3. Exit\nsilahkan pilih: "))
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            exit_program()
        
    
    
if __name__ == '__main__':
    start()